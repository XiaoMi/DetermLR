# lOGIQA with CR
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

os.environ["OPENAI_API_KEY"] = '----'
from logicqa_prompt import *

TRY_CNT = 16


def get_parser():
    parser = argparse.ArgumentParser(description="Cumulative Reasoning")
    parser.add_argument('--temperature', type=float, default=0.1, help='temperature')
    parser.add_argument('--propnum', type=int, choices=range(0, 21), default=5, help='numbers of props')
    parser.add_argument('--reasoningnum', type=int, choices=range(0, 21), default=16,
                        help='numbers of reasoning, when > 1, majority voting is used')
    parser.add_argument('--choices', type=int, choices=range(0, 21), default=2, help='numbers of premises to be chosen')
    parser.add_argument('--trycnt', type=int, choices=range(1, 1001), default=16, help='numbers of try times')
    parser.add_argument('--exploration_prob', type=float, default=1.00, help='exploration probability')
    parser.add_argument('--min_score', type=float, default=0.5, help='min score')
    parser.add_argument('--verified_reasoning', type=ast.literal_eval, default=False,
                        help='self verified reasoning, may not work well for small models')
    parser.add_argument('--model', type=str, default='gpt-4', help='model to use')
    parser.add_argument('--dataset', type=str, default='data/logiQA/logicqa-hard.json', help='dataset to use')
    parser.add_argument('--verbose', type=ast.literal_eval, default=True, help='verbose mode')
    parser.add_argument('--con_select', default=False, help='random or prompt')
    parser.add_argument('--memory', default=False, help='use memory or not')
    parser.add_argument('--boundary_validation', default=False, help='use boundary or not')
    parser.add_argument('--global_validation', default=True, help='use validation global or not')
    parser.add_argument('--useful_judgement', default=False, help='the forth judgement')
    parser.add_argument('--condition_divide', default=False, help='the forth judgement')
    return parser


parser = get_parser()
args = parser.parse_args()

guidance.llm = guidance.llms.OpenAI(args.model)


def main():
    # Load the data from the JSON file
    with open(args.dataset, 'r', encoding='utf-8') as file:
        data = json.load(file)
    for item in data:
        # translate the format of the ans
        if item['answer'] == 1:
            item['label'] = 'A'
        if item['answer'] == 2:
            item['label'] = 'B'
        if item['answer'] == 3:
            item['label'] = 'C'
        if item['answer'] == 4:
            item['label'] = 'D'
        del item['answer']

    t = time.localtime()

    dataset_name = args.dataset.split('/')[2].split('.')[0]
    model_name = args.model.replace('/', '-')
    logfilename = 'results/logiqa/results-determlr-openai--' + model_name + '--t' + str(
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
        f.write("global_validation:" + str(args.global_validation) + "\n")
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
        context = example['text']
        question = example['question']
        options = ' '.join(example['options'])
        if args.verbose:
            print("context:", example['text'])
            print("question:", example['question'])
            print("options:", ' '.join(example['options']))

        memory = []
        propositions = []
        determinate_premise = []
        indeterminate_premise = []
        Last_infer_history = "还没有历史信息。"
        last_relevant_premise = " "
        last_prop = " "
        infer_history = []
        failed_cnt = 0
        logs = []
        # premise extraction
        try_cnt = 0
        while try_cnt < TRY_CNT:
            try:
                result = condition_extra(examples=condition_extra_examples, context=context + ' ' + question,
                                temperature=args.temperature)
                break
            except Exception as e:
                print("validate_deduction() local failed, try again... (No. {})".format(try_cnt + 1), "Error:",
                        e)
                try_cnt += 1
                time.sleep(min(100, 2 ** (try_cnt / 2)))
                continue
        clauses = result['premise'].split('。')
        premises = [clause.strip() + '。' for clause in clauses if clause.strip()]
        topic = result['topic']
        boundary_condition = result['boundary_condition']



        if args.verbose: print("[Topic]: \t", topic)
        if args.verbose: print("[Premises]: \t", premises)
        if args.verbose: print("[Boundary_condition]: \t", boundary_condition)
        if args.condition_divide:
            for premise in premises:
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

            for premise in determinate_premise:
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

                if result['premise'] != '无。':
                    print("trans_premise:", result['premise'])
                    trans_premises.append(result['premise'])
            determinate_premise += trans_premises

        flag = True
        visited_nodes = 0
        deter_num = 0
        indeter_num = 0
        while (len(propositions) < args.propnum and failed_cnt < args.trycnt):  
            visited_nodes += 1
            failed_cnt += 1
            explanation = ""
            if args.verbose: print("\t# <No. {}>".format(len(propositions) + 1))

            if args.con_select:
                # # args.exploration_prob determines the probability of using premises + propositions as the input of gen_proposition
                if failed_cnt >= (args.trycnt / 2):
                    if numpy.random.rand() < args.exploration_prob:  # random choose
                        tmp = numpy.random.choice(premises + propositions,
                                                  size=min(len(premises + propositions), args.choices), replace=False)
                    else:
                        tmp = numpy.random.choice(premises, size=min(len(premises), args.choices), replace=False)

                # # args.exploration_prob determines the probability of using premises + propositions as the input of gen_proposition
                if failed_cnt < (args.trycnt / 2):
                    try_cnt = 0
                    # New premise exploration base on these premises
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
                                if "历史信息" in Last_infer_history:
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
                                                                   topic=topic, last_false_history=Last_infer_history,
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
                if numpy.random.rand() < args.exploration_prob:  # random choose;
                    tmp = numpy.random.choice(premises + propositions,
                                              size=min(len(premises + propositions), args.choices), replace=False)
                else:
                    tmp = numpy.random.choice(premises, size=min(len(premises), args.choices), replace=False)

            if failed_cnt < (args.trycnt / 4) and args.con_select:
                filter_conditions = tmp
                clauses = tmp.split('.')
                my_tmp = [clause.strip() + '.' for clause in clauses if clause.strip()]
                random.shuffle(my_tmp)
            else:
                my_tmp = tmp
            print("filtered conditions:", my_tmp)

            # generate proposition
            try_cnt = 0
            while try_cnt < TRY_CNT:  
                try:
                    t = gen_proposition(examples=gen_proposition_examples, premises=' '.join(my_tmp),
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
            # a format question from guidance.
            if len(prop) > 0 and prop[-1] == '"':
                prop = prop[:-1]

            if prop in premises or prop in propositions:  # if there are two same premises, skip.
                if args.verbose:
                    Last_infer_history = "上一轮中，" + explanation + "但是没有得到有效的命题。"
                    print("\t[Raw propositions]\t", prop)
                    print("\t\t[Is not duplicated]:\t", 'False (literally)')
                continue

            if args.verbose:
                print("\t[Raw propositions]\t", prop)
                print("\t\t[Deduced from Premises]:\t", tmp)

            # is something to be deduced
            is_something_selection = 'False'  
            # invalid premise with the following formats.
            if prop.startswith('There is no') or prop.startswith('There are no') or prop.startswith(
                    'No valid') or prop.startswith(
                    'None of the') or '没有前提' in prop or '没有命题' in prop or '新前提' in prop or '新命题' in prop or 'It is not possible to' in prop or 'the correctness of the hypothesis' in prop or 'new Proposition' in prop or 'new proposition' in prop:
                if args.verbose:
                    Last_infer_history = "上一轮中，" + explanation + "但是没有得到有效的命题。"
                    print("\t\t[Deduced something]:\t", is_something_selection)
                continue

            # # duplicate judgement
            # try_cnt = 0
            # while try_cnt < TRY_CNT:
            #     try:
            #         is_duplicated = duplicated_deduction(examples=duplicated_deduction_examples, premises=' '.join(my_tmp),
            #                                              temperature=args.temperature,
            #                                              proposition=prop, valid_duplicated = valid_duplicated)['duplicated']
            #         break
            #     except Exception as e:
            #         print("duplicated_deduction() failed, try again... (No. {})".format(try_cnt+1), "Error:", e)
            #         try_cnt += 1
            #         time.sleep(min(100, 2 ** (try_cnt / 2)))
            #         continue

            # if args.verbose: print("\t\t[Is not duplicated]:\t", 'True' if is_duplicated=='False' else 'False')
            # if is_duplicated=='True':
            #     Last_infer_history = "上一轮中，" + explanation + "但是没有得到有效的命题。"
            #     continue

            # source validation
            try_cnt = 0
            while try_cnt < TRY_CNT:
                try:
                    sourced_local = \
                    sourced_deduction(examples=sourced_deduction_examples, premises=' '.join(tmp), proposition=prop,
                                      valid_sourced=valid_sourced)['sourced']
                    break
                except Exception as e:
                    print("sourced_deduction() local failed, try again... (No. {})".format(try_cnt + 1), "Error:", e)
                    try_cnt += 1
                    time.sleep(min(100, 2 ** (try_cnt / 2)))
                    continue

            if args.verbose: print("\t\t[Sourced local]:\t", sourced_local)
            if sourced_local == 'False':
                Last_infer_history = "上一轮中，" + explanation + "但是没有得到有效的命题。"
                continue

            # logical validation
            try_cnt = 0
            while try_cnt < TRY_CNT:
                try:
                    validation_local = \
                    validate_deduction(examples=validate_deduction_examples, premises=' '.join(tmp), proposition=prop,
                                       valid_validation=valid_validation)['validation']
                    break
                except Exception as e:
                    print("validate_deduction() local failed, try again... (No. {})".format(try_cnt + 1), "Error:", e)
                    try_cnt += 1
                    time.sleep(min(100, 2 ** (try_cnt / 2)))
                    continue

            if args.verbose: print("\t\t[Validation local]:\t", validation_local)
            if validation_local == 'False':
                Last_infer_history = "上一轮中，" + explanation + "但是但是没有得到有效的命题。"
                continue

            try_cnt = 0
            while try_cnt < TRY_CNT:
                try:
                    validation_global = \
                    validate_deduction(examples=validate_deduction_examples, premises=' '.join(premises + propositions),
                                       proposition=prop, valid_validation=valid_validation)['validation']
                    break
                except Exception as e:
                    print("validate_deduction() global failed, try again... (No. {})".format(try_cnt + 1), "Error:", e)
                    try_cnt += 1
                    time.sleep(min(100, 2 ** (try_cnt / 2)))
                    continue

            if args.verbose: print("\t\t[Validation global]:\t", validation_global)
            if validation_global == 'False':
                Last_infer_history = "上一轮中，" + explanation + "但是但是没有得到有效的命题。"
                continue

            if args.boundary_validation:
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
                    Last_infer_history = "上一轮中，" + explanation + "但是没有得到有效的命题。"
                    continue

            # all validation passed
            if args.verbose: print("\t\t<All Test Passed>: \t", prop)
            propositions.append(prop)  
            last_prop = prop

            # memory recording not used in CR
            infer_history.append(
                "在NO:{}轮推理中,".format(len(propositions)) + " 我们使用\"前提\": \"" + ' '.join(
                    my_tmp) + "\"" + "并获得了\"新确定命题\": \"" + prop + "\"\n")
            Last_infer_history = "还没有历史信息。"
            Last_relevant_premise = last_relevant_premise  
            

            failed_cnt = 0

        if args.verbose: print("[Generated Propositions]: \t", propositions)

        reasoning_num = 0
        reasoning_try_cnt = 0
        judgement_cnt = {"A": 0, "B": 0, "C": 0, "D": 0, "K": 0}   # use K represent "no ans" 
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
                            context=context,
                            question=question + ' '.join(options),
                            premises=' '.join(my_premises),
                            boundary_condition=boundary_condition,
                            propositions=' '.join(propositions),
                            memory=' '.join(determinate_premise),
                            infer_history=infer_history,
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
                    if args.verbose: 

                        print("\t[Reasoning <No. {}>]:\t".format(reasoning_num + 1), out["reasoning"])
                    break
                except Exception as e:
                    print("structure_program() failed, try again... (No. {})".format(try_cnt + 1), "Error:", e)
                    try_cnt += 1
                    time.sleep(min(100, 2 ** (try_cnt / 2)))
                    continue
            # Optional verification 
            if args.verified_reasoning == True:
                try_cnt = 0
                while try_cnt < TRY_CNT:
                    try:
                        verified_reasoning = validate_deduction(examples=validate_deduction_examples,
                                                                premises=' '.join(premises + propositions),
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

        majority_judgement = max(judgement_cnt, key=judgement_cnt.get)

        if majority_judgement == example["label"]:
            correct_predictions += 1

        print("[Prediction]: ", majority_judgement)
        print("[Actual]: ", example["label"])

        # result
        accuracy = correct_predictions / cnt
        total_nodes += visited_nodes
        print("[Running Average Accuracy]: ", accuracy)
        print("[Average visited nodes]:", total_nodes / cnt)

        result = {
            "example_id": example["example_id"],
            "context": context,
            "question": question,
            "options": options,
            "prediction": out["judgement"],
            "actual": example["label"],
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
            f.write('\n')  
            # Add a newline to separate each result

if __name__ == "__main__":
    main()
