# logicdeduction with Chain-of-Thought
# -*- coding: utf-8 -*-
import re
import guidance
import json
import time
from tqdm import tqdm
import argparse
import os

os.environ["OPENAI_API_KEY"] = 'sk-----'

TRY_CNT = 16


def get_parser():
    parser = argparse.ArgumentParser(description="CoT or CoT-SC")
    parser.add_argument('--temperature', type=float, default=0.7, help='temperature')
    parser.add_argument('--majoritycnt', type=int, choices=range(1, 101), default=16,
                        help='numbers of majority voting times')
    parser.add_argument('--verbose', type=bool, default=True, help='verbose mode')
    parser.add_argument('--model', type=str, default='gpt-4', help='model to use')
    parser.add_argument('--dataset', type=str, default='data/logicdeduction/Logicdeduction-dev.json', help='dataset to use')
    return parser


parser = get_parser()
args = parser.parse_args()

guidance.llm = guidance.llms.OpenAI(args.model, caching=False)

examples = [
    {
        'context': 'The following paragraphs each describe a set of seven objects arranged in a fixed order. The statements are logically consistent within each paragraph.\n\nOn a branch, there are seven birds: a falcon, a crow, a hawk, a hummingbird, a blue jay, a robin, and a raven. The blue jay is to the right of the robin. The hawk is to the left of the hummingbird. The robin is the second from the right. The falcon is the third from the left. The crow is to the right of the hummingbird. The raven is the second from the left.',
        'premises': 'The blue jay is to the right of the robin. The hawk is to the left of the hummingbird. The robin is the second from the right. The falcon is the third from the left. The crow is to the right of the hummingbird. The raven is the second from the left.',
        'boundary_condition': 'On a branch, there are seven birds: a falcon, a crow, a hawk, a hummingbird, a blue jay, a robin, and a raven.',
        'question': 'Which of the following is true? A) The falcon is the third from the right.B) The crow is the third from the right.C) The hawk is the third from the right.D) The hummingbird is the third from the right.E) The blue jay is the third from the right.F) The robin is the third from the right.G) The raven is the third from the right.',
        'propositions': 'Hummingbird is the forth from the left. The blue jay is the first from the right. The hawk is the first from the left.',
        'options': 'A) The falcon is the third from the right.B) The crow is the third from the right.C) The hawk is the third from the right.D) The hummingbird is the third from the right.E) The blue jay is the third from the right.F) The robin is the third from the right.G) The raven is the third from the right.',
        "reasoning": "We know that Hummingbird is the forth from the left.However, there are seven objects, which means there are seven positions, which is the fourth from the left and the third from the right. So we know that Hummingbird is the third from the right.So we know the answer is D.",
        'ans': 'D',
    },
    {
        'context': 'The following paragraphs each describe a set of five objects arranged in a fixed order. The statements are logically consistent within each paragraph.\n\nIn a golf tournament, there were five golfers: Dan, Amy, Eve, Ana, and Mya. Dan finished above Eve. Dan finished below Mya. Amy finished third. Ana finished second-to-last.',
        'question': 'Which of the following is true? A) Dan finished last.B) Amy finished last.C) Eve finished last.D) Ana finished last.E) Mya finished last.',
        'premises': 'Dan finished above Eve. Dan finished below Mya. Amy finished third. Ana finished second-to-last.',
        'boundary_condition': 'In a golf tournament, there were five golfers: Dan, Amy, Eve, Ana, and Mya.',
        'propositions': 'Ana does not finish first. Amy does not finish first. Eve does not finish first. Dan does not finish first. Mya finish first.',
        'options': 'A) Dan finished last.B) Amy finished last.C) Eve finished last.D) Ana finished last.E) Mya finished last.',
        "reasoning": "Ana does not finish first. Amy does not finish first. Eve does not finish first. Dan does not finish first. Mya finish first.Then,we know that Amy finished third.Mya finished first.So there are three positions remained.And we know from premises that Dan finished above Eve and Dan finished below Mya. So we know that Dan is located in the mid of these three positions,he finished forth.Additionally, Dan finished above Eve, so Eve finished last. The anwser is C.",
        'ans': 'C'},
    {
        'context': 'The following paragraphs each describe a set of three objects arranged in a fixed order. The statements are logically consistent within each paragraph.\n\nIn a golf tournament, there were three golfers: Mel, Ada, and Ana. Mel finished last. Ana finished second.',
        'question': 'Which of the following is true? A) Mel finished second. B) Ada finished second. C) Ana finished second.',
        'premises': 'Mel finished last. Ana finished second.',
        'boundary_condition': 'In a golf tournament, there were three golfers: Mel, Ada, and Ana.',
        'propositions': 'Ada finished last.',
        'options': 'A) Mel finished second. B) Ada finished second. C) Ana finished second.',
        "reasoning": "From the premises, we know that Ana finished second.So the answer is C.",
        'ans': 'C'},
]
# Define the guidance program
structure_program = guidance(
    '''
    {{#system}}
    Suppose you are one of the greatest AI scientists, logicians, and mathematicians. Let's think about it step by step.
    Read and analyze the "context" first, then use the information provided in the context to reason about which of the options given is the answer to the question.
    Please note that this is a single choice question.
   ----{{/system}}

    {{~#each examples}}
    {{#user}}
    ---
    "context": "{{this.context}}"
    "question": "{{this.question}}"
    "options": "{{this.options}}"
    {{/user}}
    {{#assistant}}"reasoning": "Let's think step by step,{{this.reasoning}}"{{/assistant}}
    {{#assistant}}Now, we know that the answer is:{{this.ans}}{{/assistant}}
    {{~/each}}

    {{#user}}
    ---
    "context": "{{context}}"
    "question": "{{question}}"
    "options": "{{options}}"
    {{/user}}
    {{#assistant}}"reasoning": "Let's think step by step,{{/assistant}}
    {{#assistant}}{{gen "thoughts" temperature=temperature max_tokens=500 stop=['\\n\"']}}{{/assistant}}
    {{#assistant}}Now, we know that the answer is:{{/assistant}}
    {{#assistant}}{{select "judgement" options=choose}}{{/assistant}}
    ''')
# we can pre-define valid option sets
choose = ["A", "B", "C", "D", "E", "F", "G"]
# Define the guidance program

def main():
    # Load the data from the JSON file
    with open(args.dataset, 'r', encoding='utf-8') as file:
        data = json.load(file)


    t = time.localtime()

   
    dataset_name = args.dataset.split('/')[2].split('.')[0]
    
    model_name = args.model.replace('/', '-')
    logfilename = 'results/logicdeduction/results-LOGICQA-cot-openai--' + model_name + '--' + dataset_name + '--k_' + str(
        args.majoritycnt) + '--' + time.strftime("%Y-%m-%d-%H-%M-%S", t) + '.jsonl'
    with open(logfilename, 'w') as f:
        f.write(time.strftime("%Y-%m-%d %H:%M:%S", t) + '\n')  # write each result as a new line
        f.write("Model: " + args.model + "\n")
        f.write("Temperature: " + str(args.temperature) + "\n")
        f.write("Majority Cnt: " + str(args.majoritycnt) + "\n")
        f.write("Dataset: " + args.dataset + "\n")
        f.write("bf16: True\n")
        f.write("--------------------------------\n")
    # Initialize counter for correct predictions
    correct_predictions = 0
    cnt = 0
    total_cnt = len(data)

    # Iterate over the data from the JSON file and call the solve function
    for example in tqdm(data, desc="Evaluating", unit="example"):
        cnt += 1

        print("-------------------------\n### Example ID: ", example["id"], "\t ( ", cnt, "/", total_cnt, " )")
        context = example['context']
        question = example['question']
        options = ' '.join(example['options'])

        # Majority vote for out['judgement']
        # count the number of three/five/seven options
        judgement_cnt = {"A": 0, "B": 0, "C": 0, "D": 0, "E": 0, "F": 0, "G": 0}
        thoughts_list = []

        for i in range(0, args.majoritycnt):
            try_cnt = 0
            while try_cnt < TRY_CNT:
                try:
                    out = structure_program(
                        examples=examples,
                        context=context,
                        question=question,
                        options=options,
                        choose=choose
                    )
                    break
                except Exception as e:
                    print("structure_program() failed, try again... (No. {})".format(try_cnt + 1), "Error:", e)
                    try_cnt += 1
                    time.sleep(min(1024, 2 ** (try_cnt / 2)))
                    continue

            # notice that judgement may contains blanks, remove it
            my_judgement = out["judgement"].strip()
            judgement_cnt[my_judgement] += 1
            thoughts_list += [out["thoughts"]]

            if args.verbose:
                print("Thoughts [", i, "]", out["thoughts"])
                print("\t\t[Judgement Cnt]: ", judgement_cnt)

        # select the one with the highest count
        majority_judgement = max(judgement_cnt, key=judgement_cnt.get)

        # calculate the number of correct predictions
        if majority_judgement == example["answer"]:
            correct_predictions += 1

        print("[Prediction]: ", majority_judgement)
        print("[Actual]: ", example["answer"])

        # Calculate and print the running accuracy
        accuracy = correct_predictions / cnt

        print("[Running Average Accuracy]: ", accuracy)

        result = {
            "example_id": example["id"],
            "prediction": majority_judgement,
            "actual": example["answer"],
            "accuracy": accuracy,
            "judgement_cnt": judgement_cnt,
            "thoughts_list": thoughts_list,
        }

        # Write the result to a JSON file, note that we open the file in append mode ('a')
        with open(logfilename, 'a') as f:
            f.write(json.dumps(result) + '\n')  # write each result as a new line


if __name__ == "__main__":
    main()
