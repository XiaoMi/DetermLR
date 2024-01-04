# Logicaldeduction with tot
# args.tot is true and bfs is the number visited per round.
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
import queue
os.environ["OPENAI_API_KEY"] = 'sk------'
from logicdeduction_prompt import *

TRY_CNT = 16


def get_parser():
    parser = argparse.ArgumentParser(description="tree of thought")
    parser.add_argument('--temperature', type=float, default=0.1, help='temperature')
    parser.add_argument('--propnum', type=int, choices=range(0, 21), default=5, help='numbers of props')
    parser.add_argument('--reasoningnum', type=int, choices=range(0, 21), default=4,
                        help='numbers of reasoning, when > 1, majority voting is used')
    parser.add_argument('--choices', type=int, choices=range(0, 21), default=4, help='numbers of premises to be chosen')
    parser.add_argument('--trycnt', type=int, choices=range(1, 1001), default=16, help='numbers of try times')
    parser.add_argument('--exploration_prob', type=float, default=1.00, help='exploration probability')
    parser.add_argument('--min_score', type=float, default=0.5, help='min score')
    parser.add_argument('--verified_reasoning', type=ast.literal_eval, default=True,
                        help='self verified reasoning, may not work well for small models')
    parser.add_argument('--model', type=str, default='gpt-4', help='model to use')
    parser.add_argument('--dataset', type=str, default='data/logicdeduction/Logicdeduction-dev.json', help='dataset to use')
    parser.add_argument('--verbose', type=ast.literal_eval, default=True, help='verbose mode')
    parser.add_argument('--con_select', default=False, help='random or prompt')
    parser.add_argument('--memory', default=False, help='use memory or not')
    parser.add_argument('--infer_history', default=False, help='history default in memory.')
    parser.add_argument('--useful_judgement', default=False, help='the forth judgement')
    parser.add_argument('--condition_divide', default=False, help='the forth judgement')
    parser.add_argument('--tot', default=True, help='tot baseline')
    parser.add_argument('--bfs', type=int, default=5, help='tot bfs')
    return parser


parser = get_parser()
args = parser.parse_args()

guidance.llm = guidance.llms.OpenAI(args.model)


def main():

    # Load the data from the JSON file
    with open(args.dataset, 'r', encoding='utf-8') as file:
        data = json.load(file)


    t = time.localtime()


    dataset_name = args.dataset.split('/')[2].split('.')[0]
    model_name = args.model.replace('/', '-')
    logfilename = 'results/logicdeduction/results-tot-openai--' + model_name + '--t' + str(
        args.temperature) + '--' + dataset_name + '--n_' + str(args.propnum) + '--' + time.strftime("%Y-%m-%d-%H-%M-%S",
                                                                                                    t) + '.jsonl'
    with open(logfilename, 'w') as f:
        f.write(time.strftime("%Y-%m-%d %H:%M:%S", t) + '\n')  # write each result as a new line
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

        print("-------------------------\n### Example ID: ", example['id'], "\t ( ", cnt, "/", total_cnt, " )")
        context = example['context']
        question = example['question']
        options = ' '.join(example['options'])
        if args.verbose:
            print("context:", example['context'])
            print("question:", example['question'])
            print("options:", ' '.join(example['options']))

        memory = []
        propositions = []
        que = queue.Queue()
        determinate_premise = []
        indeterminate_premise = []
        Last_infer_history = ['There is no information, because this is the first reasoning.']
        last_relevant_premise = " "
        infer_history = []
        failed_cnt = 0
        # premise extraction
        try_cnt = 0
        while try_cnt < TRY_CNT:
            try:
                result = condition_extra(examples=condition_extra_examples, context=context,
                                temperature=args.temperature)
                break
            except Exception as e:
                print("validate_deduction() local failed, try again... (No. {})".format(try_cnt + 1), "Error:",
                        e)
                try_cnt += 1
                time.sleep(min(100, 2 ** (try_cnt / 2)))
                continue
        clauses = result['premise'].split('.')
        premises = [clause.strip() + '.' for clause in clauses if clause.strip()]
        topic = result['topic']
        boundary_condition = result['boundary_condition']



        if args.verbose: print("[Topic]: \t", topic)
        if args.verbose: print("[Premises]: \t", premises)
        if args.verbose: print("[Boundary_condition]: \t", boundary_condition)
        # memory using
        if args.condition_divide:
            for premise in premises:
                # premise identification base on format
                if "below" in premise:
                    print("indeterminate_premise:", premise)
                    indeterminate_premise.append(premise)
                    continue
                if "above" in premise:
                    print("indeterminate_premise:", premise)
                    indeterminate_premise.append(premise)
                    continue
                if "than" in premise:
                    print("indeterminate_premise:", premise)
                    indeterminate_premise.append(premise)
                    continue
                if "to the" in premise:
                    print("indeterminate_premise:", premise)
                    indeterminate_premise.append(premise)
                    continue
                if "-to-" in premise:
                    print("indeterminate_premise:", premise)
                    indeterminate_premise.append(premise)
                    continue
                if "most" in premise:
                    memory.append(premise)
                    print("determinate_premise:", premise)
                    determinate_premise.append(premise)
                    continue
                if "est" in premise:
                    memory.append(premise)
                    print("determinate_premise:", premise)
                    determinate_premise.append(premise)
                    continue
                if "from the" in premise:
                    memory.append(premise)
                    print("determinate_premise:", premise)
                    determinate_premise.append(premise)
                    continue
                try_cnt = 0
                while try_cnt < TRY_CNT:
                    try:
                        judgement = \
                            useful_deduction(examples=useful_deduction_examples, Premise=premise, temperature=args.temperature,
                                             topic=topic,
                                             valid_validation=premise_divide_judgement)['usefulness']
                        break
                    except Exception as e:
                        print("validate_deduction() local failed, try again... (No. {})".format(try_cnt + 1), "Error:",
                              e)
                        try_cnt += 1
                        time.sleep(min(100, 2 ** (try_cnt / 2)))
                        continue
                if judgement == 'True':
                    memory.append(premise)
                    print("determinate_premise:", premise)
                    determinate_premise.append(premise)
                else:
                    print("indeterminate_premise:", premise)
                    indeterminate_premise.append(premise)
            trans_premises = []

            for premise in premises:
                try_cnt = 0
                while try_cnt < TRY_CNT:
                    try:
                        result = \
                            condition_transformation(examples=condition_transformation_examples, premise=premise,
                                                     topic=topic, premises=determinate_premise, question=question + ' '.join(options),
                                                     boundary_condition=boundary_condition,
                                                     temperature=args.temperature)
                        break
                    except Exception as e:
                        print("validate_deduction() local failed, try again... (No. {})".format(try_cnt + 1), "Error:",
                              e)
                        try_cnt += 1
                        time.sleep(min(100, 2 ** (try_cnt / 2)))
                        continue

                if result['premise'] != 'None.':
                    print("trans_premise:", result['premise'])
                    trans_premises.append(result['premise'])
            determinate_premise += trans_premises

        # logs.append({"determinate_premise:", ' '.join(determinate_premise)})
        # logs.append({"indeterminate_premise:", ' '.join(indeterminate_premise)})
        flag = True
        visited_nodes = 0
        deter_num = 0
        indeter_num = 0
        while (len(propositions) < args.propnum and failed_cnt < args.trycnt):  
            # visited_nodes += 1
            failed_cnt += 1
            explanation = ""
            if args.verbose: print("\t# <No. {}>".format(len(propositions) + 1))

            if args.con_select:
                # # args.exploration_prob determines the probability of using premises + propositions as the input of gen_proposition
                if failed_cnt >= (args.trycnt / 2):
                    if numpy.random.rand() < args.exploration_prob:  
                        tmp = numpy.random.choice(premises + propositions,
                                                  size=min(len(premises + propositions), args.choices), replace=False)
                    else:
                        tmp = numpy.random.choice(premises, size=min(len(premises), args.choices), replace=False)

                # # premise_prioritization
                if failed_cnt < (args.trycnt / 2):
                    try_cnt = 0
                    while try_cnt < TRY_CNT:  
                        try:
                            if args.infer_history:
                                tmp = condition_select_history(examples=conditions_scores_examples,
                                                               determinate_premise=' '.join(determinate_premise),
                                                               indeterminate_premise=' '.join(indeterminate_premise),
                                                               infer_history=infer_history,
                                                               temperature=args.temperature)[
                                    'results'].strip()
                            else:
                                if len(Last_infer_history) == 1:
                                    tmp = condition_select_score_3(examples=conditions_scores_examples_3,
                                                                   determinate_premise=' '.join(determinate_premise),
                                                                   indeterminate_premise=' '.join(
                                                                   indeterminate_premise),
                                                                   topic=topic,
                                                                   boundary_condition=boundary_condition,
                                                                   temperature=args.temperature)
                                else:
                                    tmp = condition_select_score_2(examples=conditions_scores_examples_2,
                                                                   determinate_premise=' '.join(determinate_premise),
                                                                   indeterminate_premise=' '.join(
                                                                       indeterminate_premise),
                                                                   topic=topic, last_false_history=" ".join(Last_infer_history),
                                                                   boundary_condition=boundary_condition,
                                                                   temperature=args.temperature)
                            print("[count results]:", tmp['count'])
                            print("[explanation]:", tmp['explanation'])
                            explanation = tmp['explanation']
                            tmp = tmp['results'].strip()
                            break
                        except Exception as e:
                            print("gen_proposition() failed, try again... (No. {})".format(try_cnt + 1), "Error:", e)
                            try_cnt += 1
                            time.sleep(min(1, 2 ** (try_cnt / 2)))
                            continue
            else:
                if args.tot:
                    tmp = []
                    for i in range(0, args.bfs):
                        if numpy.random.rand() < args.exploration_prob:  
                            tmp.append(numpy.random.choice(premises + propositions,
                                                           size=min(len(premises + propositions), args.choices),
                                                           replace=False))
                        else:
                            tmp.append(
                                numpy.random.choice(premises, size=min(len(premises), args.choices), replace=False))
            my_tmp = tmp

            # generate propositions
            if args.tot:
                for i in range(0, args.bfs):
                    visited_nodes += 1
                try_cnt = 0
                while try_cnt < TRY_CNT: 
                    try:
                        t = gen_proposition(examples=gen_proposition_examples, premises=' '.join(my_tmp[i]),
                                            question=question + ' '.join(options), boundary_condition=boundary_condition,
                                            topic=topic, temperature=args.temperature)
                        break
                    except Exception as e:
                        print("gen_proposition() failed, try again... (No. {})".format(try_cnt + 1), "Error:", e)
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

                if prop in premises or prop in propositions:  # 是否有重复的prop生成，此轮生成的不作数。
                    if args.verbose:
                        Last_infer_history.append("In the last round," + explanation + "But we did not get a correct proposition.")
                        print("\t[Raw propositions]\t", prop)
                        print("\t\t[Is not duplicated]:\t", 'False (literally)')
                    continue

                if args.verbose:
                    print("\t[Raw propositions]\t", prop)
                    print("\t\t[Deduced from Premises]:\t", tmp[i])

                # is something to be deduced
                is_something_selection = 'False'  
                # invalid format as following:
                # if prop begin with 'There is no' or 'No valid' or 'None of the' , then skip
                if prop.startswith('There is no') or prop.startswith('There are no') or prop.startswith(
                        'No valid') or prop.startswith(
                        'None of the') or 'new proposition' in prop or 'no proposition' in prop or 'New Proposition' in prop or 'No proposition' in prop or 'It is not possible to' in prop or 'the correctness of the hypothesis' in prop or 'new Proposition' in prop or 'new proposition' in prop:
                    if args.verbose:
                        Last_infer_history.append("In the last round," + explanation + "But we did not get a correct proposition.")
                        print("\t\t[Deduced something]:\t", is_something_selection)
                    continue

                # source validation 
                try_cnt = 0
                while try_cnt < TRY_CNT:
                    try:
                        sourced_local = \
                        sourced_deduction(examples=sourced_deduction_examples, premises=' '.join(tmp[i]), proposition=prop, boundary_condition=boundary_condition,
                                          valid_sourced=valid_sourced)['sourced']
                        break
                    except Exception as e:
                        print("sourced_deduction() local failed, try again... (No. {})".format(try_cnt + 1), "Error:", e)
                        try_cnt += 1
                        time.sleep(min(100, 2 ** (try_cnt / 2)))
                        continue

                if args.verbose: print("\t\t[Sourced local]:\t", sourced_local)
                if sourced_local == 'False':
                    Last_infer_history.append("In the last round," + explanation + "But we did not get a correct proposition.")
                    continue

                # logical validation and conflict validation
                try_cnt = 0
                while try_cnt < TRY_CNT:
                    try:
                        validation_local = \
                        validate_deduction(examples=validate_deduction_examples, premises=' '.join(tmp[i]), proposition=prop, boundary_condition=boundary_condition,
                                           valid_validation=valid_validation)['validation']
                        break
                    except Exception as e:
                        print("validate_deduction() local failed, try again... (No. {})".format(try_cnt + 1), "Error:", e)
                        try_cnt += 1
                        time.sleep(min(100, 2 ** (try_cnt / 2)))
                        continue

                if args.verbose: print("\t\t[Validation local]:\t", validation_local)
                if validation_local == 'False':
                    Last_infer_history.append(
                    "In the last round," + explanation + "But we did not get a correct proposition.")
                    continue
                
                try_cnt = 0
                while try_cnt < TRY_CNT:
                    try:
                        validation_global = \
                        validate_deduction(examples=validate_deduction_examples, premises=' '.join(premises + propositions), boundary_condition=boundary_condition,
                                           proposition=prop, valid_validation=valid_validation)['validation']
                        break
                    except Exception as e:
                        print("validate_deduction() global failed, try again... (No. {})".format(try_cnt + 1), "Error:", e)
                        try_cnt += 1
                        time.sleep(min(100, 2 ** (try_cnt / 2)))
                        continue

                if args.verbose: print("\t\t[Validation global]:\t", validation_global)
                if validation_global == 'False':
                    Last_infer_history.append("In the last round," + explanation + "But we did not get a correct proposition.")
                    continue

                try_cnt = 0
                while try_cnt < TRY_CNT:
                    try:
                        boundary_judgement = \
                            boundary_deduction(examples=boundary_deduction_examples, boundary_condition=boundary_condition,
                                               premises=' '.join(premises + propositions),
                                               proposition=prop, valid_duplicated=valid_validation)['judgement']
                        break
                    except Exception as e:
                        print("validate_deduction() global failed, try again... (No. {})".format(try_cnt + 1), "Error:", e)
                        try_cnt += 1
                        time.sleep(min(100, 2 ** (try_cnt / 2)))
                        continue

                if args.verbose: print("\t\t[Boundary_deduction]:\t", boundary_judgement)
                if boundary_judgement == 'False':
                    Last_infer_history.append("In the last round," + explanation + "But we did not get a correct proposition.")
                    continue

                # new premise identification
                if args.useful_judgement:
                    if "than" in prop or "below" in prop or "above" in prop or "to the" in prop or "-to-" in prop:
                        print("indeterminate_prop:", prop)
                        indeterminate_premise.append(prop)
                        indeter_num += 1
                    elif "most" in prop or "est" in prop or "from the" in prop:
                        memory.append(prop)
                        deter_num += 1
                        print("determinate_prop:", prop)
                        determinate_premise.append(prop)
                    else:
                        try_cnt = 0
                        while try_cnt < TRY_CNT:
                            try:
                                judgement = \
                                    useful_deduction(examples=useful_deduction_examples, Premise=prop, temperature=args.temperature,
                                                     topic=topic,
                                                     valid_validation=valid_validation)['usefulness']
                                break
                            except Exception as e:
                                print("validate_deduction() local failed, try again... (No. {})".format(try_cnt + 1), "Error:",
                                      e)
                                try_cnt += 1
                                time.sleep(min(100, 2 ** (try_cnt / 2)))
                                continue
                        if args.verbose: print("\t\t[Validation Determine]:\t", judgement)
                        if judgement == 'true':
                            memory.append(prop)
                            deter_num += 1
                            print("determinate_prop:", prop)
                            determinate_premise.append(prop)
                        else:
                            print("indeterminate_prop:", prop)
                            indeterminate_premise.append(prop)
                            indeter_num += 1

                    if args.condition_divide:
                        try_cnt = 0
                        while try_cnt < TRY_CNT:
                            try:
                                result = \
                                    condition_transformation(examples=condition_transformation_examples, premise=prop,
                                                             topic=topic, premises=determinate_premise, question=question + ' '.join(options),
                                                             boundary_condition=boundary_condition,
                                                             temperature=args.temperature,
                                                             valid_duplicated=premise_divide_judgement)
                                break
                            except Exception as e:
                                print("validate_deduction() local failed, try again... (No. {})".format(try_cnt + 1),
                                      "Error:",
                                      e)
                                try_cnt += 1
                                time.sleep(min(100, 2 ** (try_cnt / 2)))
                                continue
                        if result['premise'] != 'None.':
                            print("trans_premise:", result['premise'])
                            determinate_premise.append(result['premise'])

                # all validation passed
                if args.verbose: print("\t\t<All Test Passed>: \t", prop)
                que.put(prop)
                # we put a 'bfs' number of propositions into queue pre round
                infer_history.append(
                    "In the NO:{} round,".format(len(propositions)) + " we use these \"premises\": \"" + ' '.join(
                        my_tmp[i]) + "\"" + "and got a \"New Proposition\": \"" + prop + "\"\n")
                Last_infer_history = ['There is no information, because this is the first reasoning.']
                # memory recording 
            if que.empty():
                break
            else:
                propositions.append(que.get())
            if len(propositions) == args.propnum:
                break
            failed_cnt = 0

        if args.verbose: print("[Generated Propositions]: \t", propositions)

        reasoning_num = 0
        reasoning_try_cnt = 0
        judgement_cnt = {"A": 0, "B": 0, "C": 0, "D": 0, "E": 0, "F": 0, "G": 0}
        reasoning_list = []
        while (reasoning_num < args.reasoningnum and reasoning_try_cnt < args.trycnt / 4):
            if len(options) == 3:
                choose = choose_3
            elif len(options) == 5:
                choose = choose_5
            else:
                choose = choose_7
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
                            context=context,
                            question=question + ' '.join(options),
                            premises=' '.join(my_premises),
                            boundary_condition=boundary_condition,
                            propositions=' '.join(propositions),
                            memory=infer_history,
                            choose=choose,
                            temperature=t,
                        )
                    else:
                        out = structure_program(
                            examples=examples,
                            context=context,
                            question=question+' '.join(options),
                            premises=' '.join(my_premises),
                            boundary_condition=boundary_condition,
                            propositions=' '.join(propositions),
                            choose=choose,
                            temperature=t,
                        )
                    if args.verbose:  # print [Reasoning No. reasoning_num]

                        print("\t[Reasoning <No. {}>]:\t".format(reasoning_num + 1), out["reasoning"])
                    break
                except Exception as e:
                    print("structure_program() failed, try again... (No. {})".format(try_cnt + 1), "Error:", e)
                    try_cnt += 1
                    time.sleep(min(100, 2 ** (try_cnt / 2)))
                    continue

            if args.verified_reasoning == True:
                try_cnt = 0
                while try_cnt < TRY_CNT:
                    try:
                        verified_reasoning = validate_deduction(examples=validate_deduction_examples,
                                                                premises=' '.join(premises + propositions), boundary_condition=boundary_condition,
                                                                proposition=out["reasoning"],
                                                                valid_validation=valid_validation)['validation']
                        break
                    except Exception as e:
                        print("validate_deduction() reasoning failed, try again... (No. {})".format(try_cnt + 1),
                              "Error:", e)
                        try_cnt += 1
                        time.sleep(min(100, 2 ** (try_cnt / 2)))
                        continue

                if args.verbose: print("\t\t[Verified reasoning]:\t", verified_reasoning)
                if verified_reasoning == 'False':
                    continue
            reasoning_num += 1
            reasoning_list.append(out["reasoning"])
            if out["judgement"] in judgement_cnt:
                judgement_cnt[out["judgement"]] += 1
            else:
                judgement_cnt["K"] += 1
            reasoning_try_cnt = 0

        if args.reasoningnum == 0:
            try_cnt = 0
            if len(options) == 3:
                choose = choose_3
            elif len(options) == 5:
                choose = choose_5
            else:
                choose = choose_7
            while try_cnt < TRY_CNT:
                try:
                    t = 0 if args.reasoningnum <= 1 else args.temperature
                    out = structure_program_wocot(
                        examples=examples,
                        context=context,
                        question=question + ' '.join(options),
                        premises=' '.join(premises),
                        boundary_condition=boundary_condition,
                        propositions=' '.join(propositions),
                        choose=choose,
                        temperature=t,
                    )
                    break
                except Exception as e:
                    print("structure_program() failed, try again... (No. {})".format(try_cnt + 1), "Error:", e)
                    try_cnt += 1
                    time.sleep(min(100, 2 ** (try_cnt / 2)))
                    continue
            if out["judgement"] in judgement_cnt:
                judgement_cnt[out["judgement"]] += 1
            else:
                judgement_cnt["K"] += 1

        # select the one with the highest count
        majority_judgement = max(judgement_cnt, key=judgement_cnt.get)

        # calculate the number of correct predictions
        if majority_judgement == example["answer"]:
            correct_predictions += 1

        print("[Prediction]: ", majority_judgement)
        print("[Actual]: ", example["answer"])

        # Calculate and print the running accuracy
        accuracy = correct_predictions / cnt
        total_nodes += visited_nodes
        print("[Running Average Accuracy]: ", accuracy)
        print("[Average visited nodes]:", total_nodes/cnt)

        result = {
            "example_id": example["id"],
            "context": context,
            "question": question,
            "options": options,
            "prediction": out["judgement"],
            "actual": example["answer"],
            "accuracy": accuracy,
            "determinate_premise:": ' '.join(determinate_premise),
            "indeterminate_premise:": ' '.join(indeterminate_premise),
            "generated_propositions": propositions,
            "reasoning": reasoning_list,
            "reasoning history": infer_history,
            "visited nodes": total_nodes/cnt,
        }

        with open(logfilename, 'a', encoding="utf-8") as f:
            # Use json.dump() with indent=4 to write with indentation
            json.dump(result, f, ensure_ascii=False, indent=4)
            f.write('\n')  # Add a newline to separate each result

if __name__ == "__main__":
    main()
