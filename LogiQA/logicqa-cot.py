# LogiQA with Chain-of-Thought
# -*- coding: utf-8 -*-
import re
import guidance
import json
import time
from tqdm import tqdm
import argparse
import os

os.environ["OPENAI_API_KEY"] = 'sk-'

TRY_CNT = 16


def get_parser():
    parser = argparse.ArgumentParser(description="Chain-of-Thought or CoT-SC")
    parser.add_argument('--temperature', type=float, default=0.7, help='temperature')
    parser.add_argument('--majoritycnt', type=int, choices=range(1, 101), default=16, help='numbers of majority voting times')
    parser.add_argument('--verbose', type=bool, default=True, help='verbose mode')
    parser.add_argument('--model', type=str, default='gpt-4', help='model to use')
    parser.add_argument('--dataset', type=str, default='data/logiQA/logicqa-hard.json', help='dataset to use')
    return parser


parser = get_parser()
args = parser.parse_args()

guidance.llm = guidance.llms.OpenAI(args.model, caching=False)

direct_examples = [
    {
        'context': '办公室里有一个教育学硕士，一个教育学士，一个哲学硕士，一个哲学学士。四个人中，A是既不是教育学硕士也不是哲学学士；A和C学的是同一学科；B只有学士学位；D不学哲学。',
        'question': '如果以上说法正确，下列哪项?',
        'options': 'A是教育学士。B是哲学学士。C是哲学学士。D是教育学士。',
        "reasoning": "根据题意，让我们一步一步的分析回答这个问题：1.因为A不是教育学硕士也不是哲学学士，因此A的学位可能是哲学硕士或者教育学学士。2.因为A和C学的是同一学科，A的学位可能是哲学硕士或者教育学学士，因此C的学位也可能是哲学学士或者教育学硕士。3.因为B只有学士学位，因此B的学位可能是教育学士或者哲学学士。4.因为D不学哲学，因此D的学位可能是教育学硕士或者教育学学士。5.因为D的学位可能是教育学硕士或者教育学学士，A的学位可能是哲学硕士或者教育学学士，C的学位也可能是哲学学士或者教育学硕士，6.但是只有两个学士，所以若D的学位是教育学硕士，C的学位是哲学学士；若D是教育学学士，A是哲学硕士，因此C的学位是哲学学士。7.D的学位无论是教育学硕士或者教育学学士，C的学位都是哲学学士。",
        'ans': 'C'},
    {
        'context': '四个人在谈论老田的存款.甲说：\"老田至少有五千元存款.\"乙说：\"不对,至少有一万元.\"丙说：\"他的存款不到两万.\"丁说：\"老田的存折上最少有一百元钱.\"实际上他们只有一个人说得对.',
        'question': '据此,可以得到：',
        'options': 'A.甲说得对。B.丁说得对。C.老田的存款连一百元钱都不到。D.老田的存款在五千元到两万元之间。',
        "reasoning": "让我们一步一步的分析回答这个问题：假设四个人中只有一个人说得对，那么其他三个人都是错的。考虑每个人的说法：1.甲说老田至少有五千元存款，如果他说得对，那么老田家里至少有五千，因此也肯定至少有一百，那么丁说的也是对的，但这与题目假设不符，因此甲说的不对。2.乙说老田至少有一万元存款，如果他说得对，因此也肯定至少有一百，那么丁说的也是对的，但这与题目假设不符，因此乙说的也不对。3.丙说老田的存款不到两万，如果他说得对，那么其他三个人说的话对错无法判断。4.丁说老田的存折上最少有一百元钱，如果他说得对，丙的对错无法判断。5.因为从1和2知道甲乙说的话不对，因此作出假设，如果丁说的是对的，丙的对错无法判断，但如果他说的是错的，丁一定是对的，这和题设符合，所以，丙是对的，丁是错的。综上所述，甲错，乙错，丁错，丙对。最终答案是C。",
        'ans': 'C'},
    {
        'context': '最聪明的骗子可能在某一时刻欺骗所有人，也可能在任何时候都欺骗一部分人，但绝对不可能在任何时刻欺骗所有人 .',
        'question': '根据上述说法，以下哪项是不正确的？',
        'options': '不可能在任何时刻欺骗所有人。一个人可能在任何时候都被欺骗。一个人可能在任何时候都不会被欺骗。在某个时刻，每个人都不可能被欺骗。',
        "reasoning": "最聪明的骗子可能在某一时刻欺骗所有人，由此可知，任何人在某个时刻都可能被欺骗，所以’在某个时刻，每个人都不可能被欺骗‘和’任何人在某个时刻都可能被欺骗‘之间是矛盾的。因此D是错的。",
        'ans': 'D'},
    {
        'context': '甲,乙,丙三人去餐厅吃饭,服务员想知道他们三人分别是干什么的,但三人只提供了以下信息：三人中一位是工程师,一位是教授,一位是医生;丙比医生年龄大,甲和教授不同岁,教授比乙年龄小.',
        'question': '据此可以推出：',
        'options': 'A.甲是工程师,乙是教授,丙是医生。B.甲是教授,乙是医生,丙是工程师。C.甲是医生,乙是工程师,丙是教授。D.甲是医生,乙是教授,丙是工程师 ',
        "reasoning": "根据题意，让我们一步一步的分析回答这个问题：1. 丙比医生年龄大，因此丙不可能是医生；2. 甲和教授不同岁，因此甲和教授中必有一人比另一人年龄大；3. 教授比乙年龄小，因此教授不可能是乙。4.甲和教授中必有一人是医生，另一人是工程师；又因为丙不可能是医生，因此丙是教授，5.则甲是医生，故乙是工程师。因此最终答案是C。",
        'ans': 'C'},
]
# Define the guidance program
# standard prompt
structure_program_direct = guidance(
    '''
    {{#system}}假设你是最伟大的人工智能科学家、逻辑学家和数学家之一。 让我们一步步思考。
    先阅读并分析“段落”，然后用段落中提供的信息来推理给出的四个选项哪一个是问题的答案。
    给出的四个选项，如果你认为第一个是答案，则回答A；如果你认为第二个是答案，则回答B；如果你认为第三个是答案，则回答C；如果你认为第四个是答案，则回答D。
    ----{{/system}}
    
    {{~#each examples}}
    {{#user}}
    ---
    "段落": "{{this.context}}"
    "问题": "{{this.question}}"
    "选项": "{{this.options}}"
    {{/user}}
    {{#assistant}}现在，我们知道答案应该是：{{/assistant}}
    {{#assistant}}{{this.ans}}{{/assistant}}
    {{~/each}}
    
    {{#user}}
    ---
    "段落": "{{context}}"
    "问题": "{{question}}"
    "选项": "{{options}}"
    {{/user}}
    {{#assistant}}现在，我们知道答案应该是：{{/assistant}}
    {{#assistant}}{{select "judgement" options=choose}}{{/assistant}}
    ''')

structure_program_direct_1 = guidance(
    '''
    {{#system}}假设你是最伟大的人工智能科学家、逻辑学家和数学家之一。 让我们一步步思考。
    先阅读并分析“段落”，然后用段落中提供的信息来推理给出的四个选项哪一个是问题的答案。
    给出的四个选项，如果你认为第一个是答案，则回答A；如果你认为第二个是答案，则回答B；如果你认为第三个是答案，则回答C；如果你认为第四个是答案，则回答D。
    ----{{/system}}

    {{#user}}
    ---
    "段落": "{{context}}"
    "问题": "{{question}}"
    "选项": "{{options}}"
    {{/user}}
    {{#assistant}}现在，我们知道答案应该是：{{/assistant}}
    {{#assistant}}{{select "judgement" options=choose}}{{/assistant}}
    ''')
examples = [
    {
        'premises': 'Miroslav Venhoda was a Czech choral conductor who specialized in the performance of Renaissance and Baroque music. Any choral conductor is a musician. Some musicians love music. Miroslav Venhoda published a book in 1946 called Method of Studying Gregorian Chant.',
        'propositions': 'Miroslav Venhoda, who published a book in 1946 called Method of Studying Gregorian Chant, is a musician as he is a choral conductor.',
        'conclusion': 'A Czech person wrote a book in 1946.',
        "reasoning": "Miroslav Venhoda, who is specified as a Czech choral conductor, published a book in 1946. Thus, it is true that a Czech person wrote a book in 1946.",
        'judgement': 'True'},
    {
        'premises': 'All eels are fish. No fish are plants. A thing is either a plant or animal. Nothing that breathes is paper. All animals breathe. If a sea eel is either an eel or a plant, then a sea eel is an eel or an animal.',
        'propositions': 'No eels are plants. All eels are animals.',
        'conclusion': 'Sea eel is an eel.',
        "reasoning": "all eels are fish and a sea eel is either an eel or a plant. It's also stated that no fish are plants. Therefore, a sea eel can't be a plant and must be an eel. However, there's no direct information about a sea eel being an eel.",
        'judgement': 'Unknown'},
    {
        'premises': 'Miroslav Venhoda was a Czech choral conductor who specialized in the performance of Renaissance and Baroque music. Any choral conductor is a musician. Some musicians love music. Miroslav Venhoda published a book in 1946 called Method of Studying Gregorian Chant.',
        'propositions': 'Miroslav Venhoda specialized in the performance of Renaissance and Baroque music.',
        'conclusion': 'No choral conductor specialized in the performance of Renaissance.',
        "reasoning": "Miroslav Venhoda, a choral conductor, specialized in the performance of Renaissance and Baroque music. Thus, it is false to conclude that no choral conductor specialized in the performance of Renaissance.",
        'judgement': 'False'},
]

# we can pre-define valid option sets
valid_judgement = ["True", "False", "Unknown"]
choose = ["A", "B", "C", "D"]
# Define the guidance program
# chain of thought
structure_program = guidance(
    '''
    {{#system}}假设你是最伟大的人工智能科学家、逻辑学家和数学家之一。 让我们一步步思考。
    先阅读并分析“段落”，然后用段落中提供的信息来推理给出的四个选项哪一个是问题的答案。
    给出的四个选项，如果你认为第一个是答案，则回答A；如果你认为第二个是答案，则回答B；如果你认为第三个是答案，则回答C；如果你认为第四个是答案，则回答D。
    ----{{/system}}
    
    {{~#each examples}}
    {{#user}}
    ---
    "段落": "{{this.context}}"
    "问题": "{{this.question}}"
    "选项": "{{this.options}}"
    {{/user}}
    {{#assistant}}"推理": "让我们一步步思考。{{this.reasoning}}"{{/assistant}}
    {{#assistant}}现在，我们知道答案应该是：{{/assistant}}
    {{#assistant}}{{this.ans}}{{/assistant}}
    {{~/each}}
    
    {{#user}}
    ---
    "段落": "{{context}}"
    "问题": "{{question}}"
    "选项": "{{options}}"
    {{/user}}
    {{#assistant}}"推理": "让我们一步步思考。{{/assistant}}
    {{#assistant}}{{gen "thoughts" temperature=temperature max_tokens=500 stop=['\\n\"']}}{{/assistant}}
    {{#assistant}}现在，我们知道答案应该是：{{/assistant}}
    {{#assistant}}{{select "judgement" options=choose}}{{/assistant}}
    ''')


def main():
    # Load the data from the JSON file
    with open(args.dataset, 'r', encoding='utf-8') as file:
        data = json.load(file)
    for item in data:
        # add . in the end of each sentence
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
    logfilename = 'results/logiqa/results-LOGICQA-cot-openai--' + model_name + '--' + dataset_name + '--k_' + str(
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

        print("-------------------------\n### Example ID: ", example["example_id"], "\t ( ", cnt, "/", total_cnt, " )")
        context = example['text']
        question = example['question']
        options = ' '.join(example['options'])

        # Majority vote for out['judgement']
        # count the number of A, B, C, D
        judgement_cnt = {"A": 0, "B": 0, "C": 0, "D": 0}
        thoughts_list = []

        for i in range(0, args.majoritycnt):
            try_cnt = 0
            while try_cnt < TRY_CNT:
                try:
                    out = structure_program(
                        examples=direct_examples,
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
        if majority_judgement == example["label"]:
            correct_predictions += 1

        print("[Prediction]: ", majority_judgement)
        print("[Actual]: ", example["label"])

        # Calculate and print the running accuracy
        accuracy = correct_predictions / cnt

        print("[Running Average Accuracy]: ", accuracy)

        result = {
            "example_id": example["example_id"],
            "prediction": majority_judgement,
            "actual": example["label"],
            "accuracy": accuracy,
            "judgement_cnt": judgement_cnt,
            "thoughts_list": thoughts_list,
        }

        # Write the result to a JSON file, note that we open the file in append mode ('a')
        with open(logfilename, 'a') as f:
            f.write(json.dumps(result) + '\n')  # write each result as a new line


if __name__ == "__main__":
    main()
