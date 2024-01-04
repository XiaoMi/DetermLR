# FOLIO with Cumulative Reasoning
import requests
import guidance
import ast
import argparse
import json
import time
import numpy
from tqdm import tqdm
from string import Template
import os
import re
import random
os.environ["OPENAI_API_KEY"] = '---'
from folio_guidance_prompt import *
TRY_CNT = 16

def get_parser():
    parser = argparse.ArgumentParser(description="Cumulative Reasoning")
    parser.add_argument('--temperature', type=float, default=0.1, help='temperature')
    parser.add_argument('--propnum', type=int, choices=range(0, 21), default=4, help='numbers of props')
    parser.add_argument('--reasoningnum', type=int, choices=range(0, 21), default=16, help='numbers of reasoning, when > 1, majority voting is used')
    parser.add_argument('--choices', type=int, choices=range(0, 21), default=5, help='numbers of premises to be chosen')
    parser.add_argument('--trycnt', type=int, choices=range(1, 1001), default=16, help='numbers of try times')
    parser.add_argument('--exploration_prob', type=float, default=1.00, help='exploration probability')
    parser.add_argument('--min_score', type=float, default=0.5, help='min score')
    parser.add_argument('--verified_reasoning', type=ast.literal_eval, default=False, help='self verified reasoning, may not work well for small models')
    parser.add_argument('--model', type=str, default='gpt-4', help='model to use')
    parser.add_argument('--dataset', type=str, default='data/folio/folio-dev.json', help='dataset to use')
    parser.add_argument('--verbose', type=ast.literal_eval, default=True, help='verbose mode')
    parser.add_argument('--con_select', default=False, help='random or prompt')
    parser.add_argument('--memory', default=False, help='use memory or not')
    parser.add_argument('--infer_history', default=False, help='use FOL or not')
    parser.add_argument('--useful_judgement', default=False, help='the forth judgement')
    return parser

parser = get_parser()
args = parser.parse_args()

guidance.llm = guidance.llms.OpenAI(args.model)

def main():

    # Load the data from the JSON file
    with open(args.dataset, 'r', encoding='utf-8') as file:
        data = json.load(file)
    for item in data:
        conclusion = re.search(r"\? ?(.*?)$", item['question'], re.S)
        conclusion = conclusion.group(1)
        
        # translate the ans' format
        clauses = item['context'].split('.')
        results = re.search(r'If (.*), (?:then )(.*)(?=$)', conclusion, re.S)
        item['premises'] = [clause.strip() + '.' for clause in clauses if clause.strip()]
        if results:
            premise = results.group(1)
            hypothesis = results.group(2)
            item['conclusion'] = hypothesis
            item['premises'].append(premise)
        else:
            item['conclusion'] = conclusion
        # add . in the end of each sentence
        if item['answer'] == 'A':
            item['label'] = 'True'
        if item['answer'] == 'B':
            item['label'] = 'False'
        if item['answer'] == 'C':
            item['label'] = 'Unknown'
        item['example_id'] = item['id']
        del item['id']
        del item['answer']
        del item['context']
        del item['question']

    # # fast random test
    # data = random.sample(data, 50)
    # random.shuffle(data)

    t = time.localtime()

    # extract 'folio-train' from args.dataset in format 'data/folio/folio-train.jsonl'
    dataset_name = args.dataset.split('/')[2].split('.')[0]
    # args.model in format 'huggyllama/llama-65b' to 'huggyllama-llama-65b'
    model_name = args.model.replace('/', '-')
    logfilename = 'results/folio/results-folio-cr-openai--' + model_name + '--t' + str(args.temperature) + '--' + dataset_name + '--n_' + str(args.propnum) + '--' + time.strftime("%Y-%m-%d-%H-%M-%S", t) + '.jsonl'
    with open(logfilename, 'w') as f:
        f.write(time.strftime("%Y-%m-%d %H:%M:%S", t) + '\n') # write each result as a new line
        f.write('propnum: ' + str(args.propnum) + '\n')
        f.write('reasnoningnum: ' + str(args.reasoningnum) + '\n')
        f.write('choices: ' + str(args.choices) + '\n')
        f.write('exploration_prob: ' + str(args.exploration_prob) + '\n')
        f.write('trycnt: ' + str(args.trycnt) + '\n')
        f.write("Model: " + args.model + "\n")
        f.write("Temperature: " + str(args.temperature) + "\n")
        f.write("Dataset: " + args.dataset + "\n")
        f.write("condition filter:" + str(args.con_select) + "\n")
        f.write("memory:" + str(args.memory) + "\n")
        f.write("infer_history:" + str(args.infer_history) + "\n")
        f.write("useful_judgment:" + str(args.useful_judgement) + "\n")
        f.write("--------------------------------\n")

    # Initialize counter for correct predictions
    correct_predictions = 0
    cnt = 0
    total_cnt = len(data)
    total_nodes = 0

    # Iterate over the data from the JSON file and call the solve function
    for example in tqdm(data, desc="Evaluating", unit="example"):
        cnt += 1
        
        print("-------------------------\n### Example ID: ", example['example_id'], "\t ( ", cnt, "/", total_cnt, " )")
        conclusion = example['conclusion']
        premises = example['premises']
        # premises = [p for p in premises if useful_deduction(examples=useful_deduction_examples, premises=' '.join(premises), proposition=p, conclusion=conclusion, valid_usefulness = valid_usefulness)['usefulness'] == 'True']        

        memory = []
        propositions = []
        determinate_premise = []
        indeterminate_premise = []
        Last_infer_history = "There's no Last_reasoning_history yet, because this is the first derivation"
        last_relevant_premise = " "
        last_prop = " "
        infer_history = []
        failed_cnt = 0
        logs = []
        if args.verbose: print("[Premises]: \t", premises)
        if args.verbose: print("[Hypothesis]: \t", conclusion)

        # memory use
        if args.memory:
            for premise in premises:
                try_cnt = 0
                while try_cnt < TRY_CNT:
                    try:
                        judgement = \
                            useful_deduction(examples=useful_deduction_examples, Premise=premise,
                                             conclusion=conclusion,
                                             valid_validation=premise_divide_judgement)['usefulness']
                        break
                    except Exception as e:
                        print("validate_deduction() local failed, try again... (No. {})".format(try_cnt + 1), "Error:",
                              e)
                        try_cnt += 1
                        time.sleep(min(100, 2 ** (try_cnt / 2)))
                        continue
                # print("judgment:", judgement)
                if judgement == 'True':
                    memory.append(premise)
                    print("determinate_premise:", premise)
                    determinate_premise.append(premise)
                else:
                    print("indeterminate_premise:", premise)
                    indeterminate_premise.append(premise)
        # logs.append({"determinate_premise:", ' '.join(determinate_premise)})
        # logs.append({"indeterminate_premise:", ' '.join(indeterminate_premise)})
        flag = True
        visited_nodes = 0
        deter_num = 0
        indeter_num = 0
        while (deter_num < args.propnum and indeter_num < args.propnum and failed_cnt < args.trycnt):   # 生成的个数和失败次数。
            visited_nodes += 1
            failed_cnt += 1

            if args.verbose: print("\t# <No. {}>".format(len(propositions) + 1))

            if args.con_select:
                # # args.exploration_prob determines the probability of using premises + propositions as the input of gen_proposition
                if failed_cnt >= (args.trycnt / 4):
                    if numpy.random.rand() < args.exploration_prob:  # 随机选择一组条件。
                        tmp = numpy.random.choice(premises + propositions, size=min(len(premises + propositions), args.choices), replace=False)
                    else:
                        tmp = numpy.random.choice(premises, size=min(len(premises), args.choices), replace=False)

                # # args.exploration_prob determines the probability of using premises + propositions as the input of gen_proposition
                # # conditions_filter
                if failed_cnt < (args.trycnt / 4):
                    try_cnt = 0
                    while try_cnt < TRY_CNT: 
                        try:
                            if args.infer_history:
                                tmp = condition_select_history(examples=conditions_scores_examples, determinate_premise=' '.join(determinate_premise), indeterminate_premise=' '.join(indeterminate_premise), infer_history=infer_history,
                                            Hypothesis=conclusion, temperature=args.temperature)['results'].strip()
                            else:
                                if len(propositions) == 0:
                                    tmp = condition_select_score_1(examples=conditions_scores_examples, last_history=Last_infer_history,
                                                                 determinate_premise=' '.join(determinate_premise),
                                                                 indeterminate_premise=' '.join(indeterminate_premise),
                                                                 Hypothesis=conclusion, temperature=args.temperature)
                                else:
                                    tmp = condition_select_score_2(examples=conditions_scores_examples, determinate_premise=' '.join(determinate_premise), indeterminate_premise=' '.join(indeterminate_premise), last_history=Last_infer_history,
                                                   Hypothesis=conclusion, temperature=args.temperature)
                                tmp = tmp['results'].strip()
                            break
                        except Exception as e:
                            print("gen_proposition() failed, try again... (No. {})".format(try_cnt + 1), "Error:", e)
                            try_cnt += 1
                            time.sleep(min(1, 2 ** (try_cnt / 2)))
                            continue
            else:
                if numpy.random.rand() < args.exploration_prob:  
                    tmp = numpy.random.choice(premises + propositions,
                                              size=min(len(premises + propositions), args.choices), replace=False)
                else:
                    tmp = numpy.random.choice(premises, size=min(len(premises), args.choices), replace=False)

            if failed_cnt < (args.trycnt / 4):
                clauses = tmp.split('.')
                my_tmp = [clause.strip() + '.' for clause in clauses if clause.strip()]
                random.shuffle(my_tmp)
            else:
                my_tmp = tmp
            print("filtered conditions:", my_tmp)

            # generate propositions
            try_cnt = 0
            while try_cnt < TRY_CNT:
                try:
                    t = gen_proposition(examples=gen_proposition_examples, premises=' '.join(my_tmp), conclusion=conclusion, temperature=args.temperature)
                    break
                except Exception as e:
                    print("gen_proposition() failed, try again... (No. {})".format(try_cnt+1), "Error:", e)
                    try_cnt += 1
                    time.sleep(min(100, 2 ** (try_cnt / 2)))
                    continue
            prop = t['proposition'].strip()
            if 'Proposition\": \"' in prop:
                prop = prop.split('Proposition\": \"')[1].split('\"')[0]
            # if the first char of prop is ", then remove it
            if len(prop) > 0 and prop[0] == '"':
                prop = prop[1:]
            # if the last char of prop is ", then remove it
            if len(prop) > 0 and prop[-1] == '"':
                prop = prop[:-1]

            if prop in premises or prop in propositions:
                if args.verbose:
                    print ("\t[Raw propositions]\t", prop)
                    print("\t\t[Is not duplicated]:\t", 'False (literally)')
                continue

            if args.verbose: 
                print("\t[Raw propositions]\t", prop)
                print("\t\t[Deduced from Premises]:\t", tmp)

            # is something to be deduced
            is_something_selection = 'False'  
            # if prop begin with 'There is no' or 'No valid' or 'None of the' , then skip
            if prop.startswith('There is no') or prop.startswith('There are no') or prop.startswith('No valid') or prop.startswith('None of the') or 'no information' in prop or 'No information' in prop or 'No direct' in prop or 'No proposition' in prop or 'It is not possible to' in prop or 'the correctness of the hypothesis' in prop or 'new proposition' in prop or 'cannot deduce a new proposition' in prop:
                if args.verbose:
                    print("\t\t[Deduced something]:\t", is_something_selection)
                continue
            # soucred deduction 
            try_cnt = 0
            while try_cnt < TRY_CNT:
                try:
                    sourced_local = sourced_deduction(examples=sourced_deduction_examples, premises=' '.join(tmp), proposition = prop, valid_sourced = valid_sourced)['sourced']
                    break
                except Exception as e:
                    print("sourced_deduction() local failed, try again... (No. {})".format(try_cnt+1), "Error:", e)
                    try_cnt += 1
                    time.sleep(min(100, 2 ** (try_cnt / 2)))
                    continue        

            if args.verbose: print("\t\t[Sourced local]:\t", sourced_local)
            if sourced_local=='False':
                continue

            # validate propositions
            try_cnt = 0
            while try_cnt < TRY_CNT:
                try:
                    validation_local = validate_deduction(examples=validate_deduction_examples, premises=' '.join(tmp), proposition = prop, valid_validation = valid_validation)['validation']
                    break
                except Exception as e:
                    print("validate_deduction() local failed, try again... (No. {})".format(try_cnt+1), "Error:", e)
                    try_cnt += 1
                    time.sleep(min(100, 2 ** (try_cnt / 2)))
                    continue
        
            if args.verbose: print("\t\t[Validation local]:\t", validation_local)
            if validation_local=='False':
                continue

            try_cnt = 0
            while try_cnt < TRY_CNT:
                try:
                    validation_global = validate_deduction(examples=validate_deduction_examples, premises=' '.join(premises + propositions), proposition = prop, valid_validation = valid_validation)['validation']
                    break
                except Exception as e:
                    print("validate_deduction() global failed, try again... (No. {})".format(try_cnt+1), "Error:", e)
                    try_cnt += 1
                    time.sleep(min(100, 2 ** (try_cnt / 2)))
                    continue   
        
            if args.verbose: print("\t\t[Validation global]:\t", validation_global)
            if validation_global=='False':
                continue

            # ALL test passed
            if args.verbose: print("\t\t<All Test Passed>: \t", prop)
            propositions.append(prop)

            failed_cnt = 0

        if args.verbose: print("[Generated Propositions]: \t", propositions)

        reasoning_num = 0
        reasoning_try_cnt = 0
        judgement_cnt = {"True": 0, "False": 0, "Unknown": 0}
        reasoning_list = []
        while (reasoning_num < args.reasoningnum and reasoning_try_cnt < args.trycnt / 4):
            reasoning_try_cnt += 1
            try_cnt = 0
            my_premises = premises.copy()
            if (reasoning_try_cnt > 0): numpy.random.shuffle(my_premises)
            while try_cnt < TRY_CNT:
                try:

                    t = 0 if args.reasoningnum <= 1 else args.temperature
                    if args.memory:
                        out = structure_program_memory(
                            examples=examples,
                            premises=' '.join(my_premises),
                            propositions=' '.join(propositions),
                            memory=' '.join(determinate_premise),
                            # memory=infer_history,
                            conclusion=conclusion,
                            valid_judgement=valid_judgement,
                            temperature=t,
                        )
                    else:
                        out = structure_program(
                            examples = examples,
                            premises = ' '.join(my_premises),
                            propositions = ' '.join(propositions),
                            conclusion = conclusion,
                            valid_judgement = valid_judgement,
                            temperature = t
                        )
                    if args.verbose: # print [Reasoning No. reasoning_num]

                        print("\t[Reasoning <No. {}>]:\t".format(reasoning_num + 1), out["reasoning"])
                    break
                except Exception as e:
                    print("structure_program() failed, try again... (No. {})".format(try_cnt+1), "Error:", e)
                    try_cnt += 1
                    time.sleep(min(100, 2 ** (try_cnt / 2)))
                    continue 

            if args.verified_reasoning == True:
                try_cnt = 0
                while try_cnt < TRY_CNT:
                    try:
                        verified_reasoning = validate_deduction(examples=validate_deduction_examples, premises=' '.join(premises + propositions), proposition = out["reasoning"], valid_validation = valid_validation)['validation']
                        break
                    except Exception as e:
                        print("validate_deduction() reasoning failed, try again... (No. {})".format(try_cnt+1), "Error:", e)
                        try_cnt += 1
                        time.sleep(min(100, 2 ** (try_cnt / 2)))
                        continue   
        
                if args.verbose: print("\t\t[Verified reasoning]:\t", verified_reasoning)
                if verified_reasoning=='False':
                    continue  
            
            reasoning_num += 1
            reasoning_list.append(out["reasoning"])
            judgement_cnt[out["judgement"]] += 1
            reasoning_try_cnt = 0

        if args.reasoningnum == 0:
            try_cnt = 0
            while try_cnt < TRY_CNT:
                try:
                    t = 0 if args.reasoningnum <= 1 else args.temperature
                    out = structure_program_wocot(
                        examples = examples,   
                        premises = ' '.join(premises),
                        propositions = ' '.join(propositions),
                        conclusion = conclusion,
                        valid_judgement = valid_judgement,
                        temperature = t
                    ) 
                    break
                except Exception as e:
                    print("structure_program() failed, try again... (No. {})".format(try_cnt+1), "Error:", e)
                    try_cnt += 1
                    time.sleep(min(100, 2 ** (try_cnt / 2)))
                    continue 
            judgement_cnt[out["judgement"]] += 1
            
        # select the one with the highest count
        majority_judgement = max(judgement_cnt, key=judgement_cnt.get)

        # calculate the number of correct predictions
        if majority_judgement == example["label"]:
            correct_predictions += 1

        print("[Prediction]: ", majority_judgement)
        print("[Actual]: ", example["label"])


        # Calculate and print the running accuracy
        accuracy = correct_predictions / cnt

        print("[Running Average Accuracy]: ", accuracy)
        print("[Average visited nodes]:", visited_nodes)
        total_nodes += visited_nodes
        result = {
            "example_id": example["example_id"],
            "prediction": out["judgement"],
            "actual": example["label"],
            "accuracy": accuracy,
            "determinate_premise:": ' '.join(determinate_premise),
            "indeterminate_premise:": ' '.join(indeterminate_premise),
            "conclusion": conclusion,
            "generated_propositions": propositions,
            "reasoning": reasoning_list,
            "reasoning history": infer_history,
            "visited nodes": total_nodes / cnt,
        }

        # # Write the result to a JSON file, note that we open the file in append mode ('a')
        with open(logfilename, 'a') as f:
            f.write(json.dumps(result) + '\n') # write each result as a new line
            
if __name__ == "__main__":
    main()
