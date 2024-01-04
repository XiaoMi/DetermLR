import guidance

validate_deduction_examples = [
    {'premises': '甲要么是外星人，要么是地球人。甲不是外星人。',
     'proposition': '甲可以是地球人。',
     'validation': 'False'},
    {'premises': '如果熊是红色的，那么熊很粗糙。熊是红色的。',
     'proposition': '熊是粗糙的。',
     'validation': 'True'},
    {'premises': '不会呼吸的东西都不是纸。 所有动物都呼吸。',
     'proposition': '所有的动物都是纸。',
     'validation': 'False'},
    {'premises': '一个事物要么是植物，要么是动物。所有动物都呼吸。',
     'proposition': '一切会呼吸的生物都是动物。',
     'validation': 'True'},
    {'premises': '米罗斯拉夫·文霍达（Miroslav Venhoda）是一位捷克合唱指挥，专门演奏文艺复兴和巴洛克音乐。 任何合唱指挥都是音乐家。',
     'proposition': '米罗斯拉夫·文霍达（Miroslav Venhoda）是一位专注于文艺复兴和巴洛克音乐的捷克合唱指挥，同时也是一位音乐家。',
     'validation': 'True'},
    {'premises': '任何合唱指挥都是音乐家。 有些音乐家热爱音乐。',
     'proposition': '所有合唱指挥都热爱音乐。',
     'validation': 'False'},
    {'premises': '所有银行家都是运动员。',
     'proposition': '所有运动员都是银行家。',
     'validation': 'False'},
    {'premises': '没有一个律师是银行家',
     'proposition': '所有的银行家都不是律师，所有的律师都不是银行家。',
     'validation': 'True'}
]
# Determine whether the proposition follows from the premises.
sourced_deduction_examples = [
    {'premises': '所有鳗鱼都是鱼。 没有鱼是植物。',
     'proposition': '鳗鱼不是植物。',
     'sourced': 'True'},
     {
      'premises': '不会呼吸的东西都不是纸。 所有动物都呼吸。',
      'proposition': '所有动物都需要食物。',
      'sourced': 'False'}
]

# we can pre-define valid option sets
valid_judgement = ["True", "False", "Unknown"]

# we can pre-define valid option sets
valid_validation = ["True", "False"]

# we can pre-define valid option sets
valid_usefulness = ["True", "False"]

# we can pre-define valid option sets
valid_something = ["True", "False"]

# we can pre-define valid option sets
valid_duplicated = ["True", "False"]

# we can pre-define valid option sets
valid_sourced = ["True", "False"]

# we can divide the premises and propositions into determinate_premise and rules
divide_judgement = ["True", "False"]

choose = ["A", "B", "C", "D", "K"]
# Premise exploration
gen_proposition_examples = [
    {'premises': '甲和乙中只能有一个人参加比赛。丙和丁中只能有一个人参加比赛。',
     'boundary_condition': '甲、乙、丙、丁、戊五个人中要选择三个人参加比赛。',
     'proposition': '戊必须参加比赛。',
     'topic': '甲、乙、丙、丁、戊五个人参加比赛的具体情况。',
     'question': '以下哪个人一定要去参赛？A.甲 B.乙 C.丙 D.戊',
     'explanation': '从问题可知要找到一个一定参赛的，我们可以试着确定是否有人一定参赛，或者一定不参赛。甲和乙中只能有一个人参加比赛。也就是一个名额在甲和乙之间产生，丙和丁中只能有一个人参加比赛。另外一个名额在丙丁中产生，但需要选出三人参加比赛，所以戊必须参加比赛。'},
    {'premises': '4位男士中，有3个高个子，2名博士，1人长相英俊。刘大伟和李强身高相同。',
     'boundary_condition': ' 无。',
     'proposition': '刘大伟和李强都是高个子',
     'topic': '李娜心中的白马王子在王威、吴刚、李强、刘大伟4位男士中的哪一位。',
     'question': '请问谁符合李娜要求的全部条件？A. 刘大伟,B. 李强 C. 吴刚, D. 王威',
     'explanation': '刘大伟和李强身高相同，一共有四位男士，三个高个子，也就是说只能有一个矮个子，因此，刘大伟和李强只能是高个子。'},
    {'premises': '至少要有一种人参或党参。如果有党参，必有白术。有人参，必有白术。',
     'boundary_condition': ' 无。',
     'proposition': '必有白术',
     'topic': '中药制剂中有哪些药材。',
     'question': '根据上述说法，中药制剂可推断出以下哪项？A无党参。B无何首乌。C有白术。D没有白术',
     'explanation': '如果有党参，必有白术。有人参，必有白术。可以知道，无论是有党参还是人参，都会有白术，根据条件：至少要有一种人参或党参，所以白术是必须有的。'},
    {'premises': '甲和教授不同岁。教授比乙年龄小。',
     'boundary_condition': '甲,乙,丙三人中一位是工程师,一位是教授,一位是医生',
     'proposition': '丙是教授。',
     'topic': '甲,乙,丙三人去餐厅吃饭,服务员想知道他们三人分别是干什么的。',
     'question': '据此可以推出哪一项？ A.甲是工程师,乙是教授,丙是医生 B.甲是教授,乙是医生,丙是工程师 C.甲是医生,乙是工程师,丙是教授 D.甲是医生,乙是教授,丙是工程师',
     'explanation': '从选项可知主要是需要确定这三个人的身份，甲和教授不同岁，因此甲肯定不是教授，教授比乙年龄小，因此乙肯定不是教授。但是三人中必定有一位教授，因此丙一定是教授。'},
    {'premises': '如果甲不参赛，则乙必须参赛。如果甲参加，则丁不在学校。如果丁不在学校，则乙必须参赛。',
     'boundary_condition': '甲,乙,丙，丁四人至少有一个人参加比赛。',
     'proposition': '乙肯定参赛。',
     'topic': '甲,乙,丙，丁四人是否参赛。',
     'question': '据此可以推出哪一项？ A.甲一定参赛 B.乙一定参赛 C.丙一定参赛 D.丁一定参赛',
     'explanation': '从’如果甲参加，则丁不在学校。如果丁不在学校，则乙必须参赛。‘可知如果甲参加比赛，则乙必须参赛。又因为如果甲不参赛，则乙必须参赛。可知无论甲是否参加，乙都会参加比赛。'},

    {
     'premises': '女性 3 人。戊、己、庚的性别相同。甲、丁的性别不同。',
     'boundary_condition': '7人中最高学历分别是本科和博士。',
     'proposition': '戊、己、庚的性别是男性。',
     'topic': '在某科室公开选拔副科长的招录考试中，甲、乙、丙、丁、戊、己、庚7人报名的学历和性别。',
     'question': '根据以上陈述，可以得出以下哪项？A.甲是男博士；B.己是女博士 C: 庚不是男博士；D: 丁是女博士。',
     'explanation': '由选项可以知道，我们需要确定的是甲、乙、丙、丁、戊、己、庚7人的年龄和学历。现在指导戊、己、庚的性别相同，甲、丁的性别不同，可以统计一下人数，甲和丁中至少有一个人和戊己庚性别相同，所以这四个人不可能是女性，因为女性只有三个人，因此戊、己、庚的性别是男性。'},
]

# Define the guidance program
gen_proposition = guidance(
'''
{{#system}}假设你是最伟大的人工智能科学家、逻辑学家和数学家之一。让我们一步步思考。
请使用逻辑推理规则（LRR）从至少两个给定的“前提”推导出一个“命题”，并且该命题不包含“如果”。
逻辑推理规则（LRR）：
1.“两个前提”：“如果A，则B。A为真。” 那么“命题”：“B为真。”
2.“两个前提”：“如果A，则B。B不成立。” 那么“命题”：“A不成立”
3.“两个前提”：“A是C或D。A不是C。” 那么“命题”：“A是D。”
4.“两个前提”：“如果A，则B。如果B，则C。” 那么“命题”：“如果A则C。”
5.“两个前提”：“如果A，则B。C为真。” 假设A是真的，则B也为真，若B为真与C有矛盾，则假设不成立，A一定为假。”
如果前提中包含假设，你可以假定假设为真看是否可以推出矛盾，但请保证“命题”逻辑正确。
请确保“命题”不是“前提”的重复或者仅仅更换表达方式。
请确保你的推理是直接从“前提”和“命题”推导出来的，而不是通过常识推理引入无源常识和无源信息。
请记住，您的推导出的“命题”应该是有助于解决提供的“问题”。
----{{/system}}

{{~#each examples}}
{{#user}}
---
"前提": "{{this.premises}}"
"边界条件": "{{this.boundary_condition}}"
我们想要推导出更多的命题用来解决下面的问题：
"问题": "{{this.question}}"
结合边界条件，你能从至少两个给定的“前提”推导出一个新的“命题”吗？
{{/user}}

{{#assistant}}"命题": "{{this.proposition}}"{{/assistant}}
{{~/each}}

{{#user}}
---
"前提": "{{premises}}"
"边界条件": "{{boundary_condition}}"
我们想要推导出更多的命题用来解决下面的问题：
"问题": "{{question}}"  ·
结合边界条件，你能从至少两个给定的“前提”推导出一个新的“命题”吗？
{{/user}}

{{#assistant}}"命题": "{{/assistant}}
{{#assistant}}{{gen "proposition" temperature=temperature max_tokens=100 stop='\n'}}{{/assistant}}
''')
# extract premises
condition_extra_examples = [
    {
        'context': '经过多轮淘汰赛后，甲、乙、丙、丁四名选手争夺最后的排名，排名不设并列名次，分析家预测：I、第一名或者是甲，或者是乙；II、如果丙不是第一名，丁也不是第一名；III、甲不是第一名。如果甲确定是第一名，以下哪个选项是对的？',
        'topic': '甲、乙、丙、丁四名选手在淘汰赛中的排名。',
        'premise': '第一名或者是甲，或者是乙。如果丙不是第一名，丁也不是第一名。甲不是第一名。甲确定是第一名。',
        'boundary_condition': '选手和名次是一对一的关系。'
    },
    {
        'context': '有6件清花瓷器：S、Y、M、Q、K、X。每件的制作年代各不相同，从左至右，按年代最早至年代最晚依次排序展览，已知的排序条件信息如下：（1）M的年代早于X。（2）如果Y的年代早于M，则Q的年代早于K和X。（3）如果M的年代早于Y，则K的年代早于Q和X。（4）S的年代要么早于Y，要么早于M，二者不兼得。以下哪个选项是对的？',
        'topic': '6件清花瓷器：S、Y、M、Q、K、X从左至右，按年代最早至年代最晚的排列顺序。',
        'premise': 'M的年代早于X。如果Y的年代早于M，则Q的年代早于K和X。如果M的年代早于Y，则K的年代早于Q和X。S的年代要么早于Y，要么早于M，二者不兼得。',
        'boundary_condition': '6件清花瓷器：S、Y、M、Q、K、X按照制作年代从左至右一次排列，对应一、二、三、四、五、六个位置。'
    },
    {
        'context': '某省围棋队教练从E、F、G、H、J、K和M这7名队员中挑选4名参加职业联赛，挑选必须符合下列条件：E或F有一人参加，但二人不能都参加。J或K有一人参加，但二人不能都参加。如果J参加，则G参加。除非F参加，否则M不参加。',
        'topic': 'E、F、G、H、J、K和M这7名队员中哪4名参加职业联赛',
        'premise': 'E或F有一人参加，但二人不能都参加。J或K有一人参加，但二人不能都参加。如果J参加，则G参加。除非F参加，否则M不参加。',
        'boundary_condition': '某省围棋队教练从E、F、G、H、J、K和M这7名队员中挑选4名参加职业联赛。'
    },
    {
        'context': '有7名被海尔公司录用的应聘者：F、G、H、I、W、X和Y，其中有一人需要分配到公关部，有三人需要分配到生产部，另外三人需要分配到销售部。这7名员工的人事分配必须满足以下条件：（1）H和Y必须分配在同一部门。（2）F和G不能分配在同一部门（3）如果X分配在销售部，则W分配在生产部。（4）F必须分配在生产部。如果G分配在销售部，那么以下说法正确的是？',
        'topic': 'F、G、H、I、W、X和Y7名员工的人事分配情况。',
        'premise': 'H和Y必须分配在同一部门。F和G不能分配在同一部门。如果X分配在销售部，则W分配在生产部。F必须分配在生产部。G分配在销售部。',
        'boundary_condition': 'F、G、H、I、W、X和Y七人中有一人需要分配到公关部，有三人需要分配到生产部，另外三人需要分配到销售部。'
    },
]
condition_transformation_examples = [
    {
        'premise': '艾托既不去加拿大，也不去英国。',
        'premises': '菲比不打算去荷兰,丹佛不打算去英国,艾托既不去加拿大,也不去英国.',
        'boundary_condition': '三位旅客分别去荷兰、加拿大和英国，且每个国家只有一个旅客。',
        'topic': '三位旅客菲比、艾托和丹佛分别去荷兰、加拿大和英国的分配情况。',
        'question': '所以: A.艾托去荷兰,丹佛去英国,菲比去加拿大 B.艾托去荷兰,丹佛加拿大,菲比去去英国 C.艾托去英国,丹佛去荷兰,菲比去加拿大 D.艾托去加拿大,丹佛去英国,菲比去荷兰',
        'judgement': 'True',
        'new_premise': '艾托去荷兰。丹佛和菲比都不去荷兰。'
    },
    {
        'premise': '艾托去荷兰。',
        'premises': '菲比不打算去荷兰,丹佛不打算去英国,艾托既不去加拿大,也不去英国.',
        'boundary_condition': '三位旅客分别去荷兰、加拿大和英国，且每个国家只有一个旅客。',
        'topic': '三位旅客菲比、艾托和丹佛分别去荷兰、加拿大和英国的分配情况。',
        'question': '所以: A.艾托去荷兰,丹佛去英国,菲比去加拿大 B.艾托去荷兰,丹佛加拿大,菲比去去英国 C.艾托去英国,丹佛去荷兰,菲比去加拿大 D.艾托去加拿大,丹佛去英国,菲比去荷兰',
        'judgement': 'True',
        'new_premise': '菲比不去荷兰。丹佛不去荷兰。'
    },
    {
        'premise': '甲参加第二场比赛。',
        'premises': '丁不参加第二场比赛。如果甲参加第三场比赛，乙参加第二场比赛。',
        'boundary_condition': '每人只可以参加第一场、第二场、第三场、第四场中的任意一场比赛。',
        'topic': '甲乙丙丁四人参加四场比赛的具体情况。',
        'question': '参加第四场比赛的人是谁？A.甲 B.乙 C.丙 D.丁',
        'judgement': 'True',
        'new_premise': '甲不参加第一、三、四场比赛。乙丙不参加第二场比赛。'
    },
    {
        'premise': '甲参加第一场或者第二场比赛。',
        'premises': '丁不参加第二场比赛。如果甲参加第三场比赛，乙参加第二场比赛。',
        'boundary_condition': '每人只可以参加第一场、第二场、第三场、第四场中的任意一场比赛。',
        'topic': '甲乙丙丁四人参加四场比赛的具体情况。',
        'question': '参加第四场比赛的人是谁？A.甲 B.乙 C.丙 D.丁',
        'judgement': 'True',
        'new_premise': '甲不参加第三场比赛，也不参加第四场比赛。'
    },
    {
        'premise': '如果甲参加第一场比赛，那么乙参加第二场比赛。',
        'premises': '丁不参加第二场比赛。如果甲参加第三场比赛，乙参加第二场比赛。',
        'boundary_condition': '每人只可以参加第一场、第二场、第三场、第四场中的任意一场比赛。',
        'topic': '甲乙丙丁四人参加四场比赛的具体情况。',
        'question': '参加第四场比赛的人是谁？A.甲 B.乙 C.丙 D.丁',
        'judgement': 'False',
        'new_premise': '无。'
    },
    {
        'premise': '老王在老李的左边。',
        'premises': '老徐在最右边。老李的右边还有其他人。',
        'boundary_condition': '老王、老李、老徐、老江四个人在领奖台上从左到右的站位。',
        'topic': '老王、老李、老徐、老江四个人在领奖台上从左到右的站位。',
        'question': '坐在最左边的人是谁？A.老王 B.老李 C.老徐 D.老江',
        'judgement': 'False',
        'new_premise': '无。'
    }
]
condition_transformation = guidance(
'''
{{#system}}假设你是最伟大的人工智能科学家、逻辑学家和数学家之一。 让我们一步步思考。
首先，请阅读和分析“现有前提”，阅读对转化的定义；
转化：在一对一的关系下，当前变量取值确定时意味着他不能取其他值，其他变量也不能取当前值，这个推理过程就是转化。
检查仅依靠“单个前提”和“边界条件”是否可以转化产生其他新的前提？新前提不要和现有前提重复。
如果可以，请给出新的前提，不可以则回答“无。“
请注意，请确保转化得到的新前提是对解决所提问题有帮助的。
----{{/system}}
{{~#each examples}}
{{#user}}
---
"现有前提": "{{this.premises}}"
"问题": "{{this.question}}"
"单个前提": "{{this.premise}}"
"边界条件": "{{this.boundary_condition}}"
{{/user}}
{{#assistant}}你可以根据单个前提和边界条件推出一个有助于解决问题的新前提吗？{{/assistant}}
{{#assistant}}"新前提": "{{this.new_premise}}"{{/assistant}}
{{~/each}}

{{#user}}
---
"现有前提": "{{premises}}"
"问题": "{{question}}"
"单个前提": "{{premise}}"
"边界条件": "{{boundary_condition}}"
{{/user}}
{{#assistant}}你可以根据单个前提和边界条件推出一个有助于解决问题的新前提吗？{{/assistant}}
{{#assistant}}"新前提": "{{/assistant}}
{{#assistant}}{{gen "premise" temperature=temperature max_tokens=50 stop=['\\n\"']}}{{/assistant}}
'''
)
condition_extra = guidance(
'''
{{#system}}假设你是最伟大的人工智能科学家、逻辑学家和数学家之一。 让我们一步步思考。
首先请阅读和分析下面定义的两组规则；
具体条件抽取规则：
前提：对具体变量之间的具体约束或是对具体变量对应具体取值的具体约束。
一、若一个句子中包含具体变量之间的关系，那么它是一个前提。
二、如果提问部分包含假设前提，这个假设可以转化为一个前提。
三、每个前提都请使用‘。’作为结尾。
边界条件抽取规则：
边界条件：整体变量和取值之间对应个数的整体约束，不涉及数字的一定不是边界条件。
根据上面的定义,总结出下面段落讨论的核心话题，抽取段落中的前提和边界条件，如果没有则写无。
----{{/system}}

{{~#each examples}}
{{#user}}
---
"段落": "{{this.context}}"
{{/user}}
{{#assistant}}你可以从上面段落中总结出讨论的核心话题？{{/assistant}}
{{#assistant}}"核心话题": "{{this.topic}}"{{/assistant}}
{{#assistant}}你可以从上面段落中抽取前提吗？{{/assistant}}
{{#assistant}}"前提": "{{this.premise}}"{{/assistant}}
{{#assistant}}你可以从上面段落中抽取边界条件吗？{{/assistant}}
{{#assistant}}"边界条件": "{{this.boundary_condition}}"{{/assistant}}
{{~/each}}

{{#user}}
---
"段落": "{{context}}"
{{/user}}

{{#assistant}}你可以从上面段落中总结出讨论的核心话题？{{/assistant}}
{{#assistant}}"核心话题": "{{/assistant}}
{{#assistant}}{{gen "topic" temperature=temperature max_tokens=50 stop='\n'}}{{/assistant}}
{{#assistant}}你可以从上面段落中抽取前提吗？{{/assistant}}
{{#assistant}}"前提": "{{/assistant}}
{{#assistant}}{{gen "premise" temperature=temperature max_tokens=300 stop=['\\n\"']}}{{/assistant}}
{{#assistant}}你可以从上面段落中抽取边界条件吗？{{/assistant}}
{{#assistant}}"边界条件": "{{/assistant}}
{{#assistant}}{{gen "boundary_condition" temperature=temperature max_tokens=300 stop=['\\n\"']}}{{/assistant}}
'''
)
# Verify whether a valid premise is generated.
is_something = guidance(
'''
{{#system}}Suppose you are one of the greatest AI scientists, logicians and mathematicians. Let us think step by step. 
Please determine whether there is a new useful "Proposition". Reply with True or False.
----{{/system}}

{{#user}}
---
"Proposition": "There is no new proposition that can be deduced from the given premises to determine the correctness of the hypothesis."
{{/user}}
{{#assistant}}False{{/assistant}}

{{#user}}
---
"Proposition": "A Czech person wrote a book in 1946."
{{/user}}
{{#assistant}}True{{/assistant}}

{{#user}}
---
"Proposition": "There is no new proposition that can be deduced from the given premises that would be useful in determining the correctness of the given hypothesis."
{{/user}}
{{#assistant}}False{{/assistant}}

{{#user}}
---
"Proposition": "None of the premises provide information to deduce a proposition related to a Czech person writing a book in 1946."
{{/user}}
{{#assistant}}False{{/assistant}}

{{#user}}
---
"Proposition": "{{proposition}}"
{{/user}}
{{#assistant}}{{select "is_something" options=valid_something}}{{/assistant}}
''')



# Logical validation
validate_deduction = guidance(
'''
{{#system}}假设你是最伟大的人工智能科学家、逻辑学家和数学家之一。 让我们一步步思考。
请使用逻辑推理规则（LRR）判断给定“前提”对“命题”的推导是否有效，回答True或False。
逻辑推理规则（LRR）：
1.“两个前提”：“如果A，则B。A为真。” 那么“命题”：“B 为真。”
2.“两个前提”：“如果A，则B。B不成立。” 那么“命题”：“A 不成立”
3.“两个前提”：“A 是 C 或 D。A 不是 C。” 那么“命题”：“A是D。”
4.“两个前提”：“如果A，则B。如果B，则C。” 那么“命题”：“如果A则C。”
5.“两个前提”：“如果A，则B。C为真。” 假设A是真的，则B也为真，若B为真与C有矛盾，则假设不成立，A一定为假。”
----{{/system}}
{{~#each examples}}
{{#user}}
---
"前提": "{{this.premises}}"
"命题": "{{this.proposition}}"
{{/user}}

{{#assistant}}"判断": "这个推导式有效的吗？ {{this.validation}}"{{/assistant}}
{{~/each}}

{{#user}}
---
"前提": "{{premises}}"
"命题": "{{proposition}}"
{{/user}}

{{#assistant}}"判断": "这个推导式有效的吗？ {{/assistant}}
{{#assistant}}{{select "validation" options=valid_validation}}{{/assistant}}
''')

# Verify the repeatability of logical reasoning.
duplicated_deduction_examples = [
    {'premises': '米罗斯拉夫·文霍达（Miroslav Venhoda）是一位捷克合唱指挥，专门演奏文艺复兴和巴洛克音乐。 任何合唱指挥都是音乐家。 有些音乐家热爱音乐。 米罗斯拉夫·文霍达 (Miroslav Venhoda) 于 1946 年出版了一本名为《格里高利圣歌研究方法》的书。',
     'proposition': '如果某人是合唱指挥，那么他就是音乐家。',
     'duplicated': 'True',
     'explanation': '“如果一个人是合唱指挥，那么他就是音乐家。” 只需要使用“任何合唱指挥都是音乐家”一个条件就可以推导出来。所以答案是肯定的。'
     },
    {'premises': '所有鳗鱼都是鱼。 没有鱼是植物。 一个事物要么是植物，要么是动物。 不会呼吸的东西都不是纸。 所有动物都呼吸。 如果海鳗是鳗鱼或植物，那么海鳗就是鳗鱼或动物。',
     'proposition': '鳗鱼不是植物。',
     'duplicated': 'False',
     'explanation': '“鳗鱼不是植物。” 需要使用“所有鳗鱼都是鱼。”和“没有鱼是植物。”合并才可以推导得到。所以答案是否定的。'
     },
    {'premises': '菲比不打算去荷兰。菲比去加拿大或英国。',
     'proposition': '菲比去英国或加拿大。',
     'duplicated': 'True',
     'explanation': '“菲比去英国或加拿大。”是”菲比去加拿大或英国。“相同内容的不同表达形式。'
     }
]
# Define the guidance program
duplicated_deduction = guidance(
'''
{{#system}}假设你是最伟大的人工智能科学家、逻辑学家和数学家之一。 让我们一步步思考。
仅用一个“前提”就可以推导出这一“命题”吗？请回答“对”或“错”。
----{{/system}}

{{~#each examples}}
{{#user}}
---
"前提": "{{this.premises}}"
"命题": "{{this.proposition}}"
仅用一个“前提”就可以推导出这一“命题”吗？
{{/user}}

{{#assistant}}"分析": "{{this.explanation}}"{{/assistant}}
{{#assistant}}"判断": "{{this.duplicated}}"{{/assistant}}
{{~/each}}

{{#user}}
---
"前提": "{{premises}}"
"命题": "{{proposition}}"
仅用一个“前提”就可以推导出这一“命题”吗？
{{/user}}

{{#assistant}}"分析": "{{/assistant}}
{{#assistant}}{{gen "reasoning" temperature=temperature max_tokens=300 stop=['\\n\"']}}{{/assistant}}
{{#assistant}}"判断": "{{/assistant}}
{{#assistant}}{{select "duplicated" options=valid_duplicated}}{{/assistant}}
''')
boundary_deduction_examples = [
    {'premises': '甲喜欢英文书。乙喜欢英文书。丙喜欢中文书。',
     'new_premise': '丁喜欢英文书。',
     'boundary_condition': '四个人中只有两个人喜欢英文书。',
     'judgement': 'False'
     },
    {
     'premises': '牡丹在一号画室展出。',
     'new_premise': '杜鹃在一号画室展出。',
     'boundary_condition': '每个画室只能展出一幅画。',
     'judgement': 'False'
     },
    {
        'premises': '甲喜欢英文书。丙喜欢中文书。',
        'new_premise': '丁喜欢英文书。',
        'boundary_condition': '四个人中只有两个人喜欢英文书。',
        'judgement': 'True'
    }
]
# boundary validation
boundary_deduction = guidance(
'''
{{#system}}假设你是最伟大的人工智能科学家、逻辑学家和数学家之一。让我们一步步思考。
请判断现有前提加上一个新前提后是否符合边界条件，请回答“True”或“False”。
----{{/system}}

{{~#each examples}}
{{#user}}
---
"现有前提": "{{this.premises}}"
"新前提": "{{this.new_premise}}"
"边界条件": "{{this.boundary_condition}}"
现有前提加上新前提之后，还符合边界条件吗？
{{/user}}

{{#assistant}}"判断": "{{this.judgement}}"{{/assistant}}
{{~/each}}

{{#user}}
---
"现有前提": "{{premises}}"
"新前提": "{{proposition}}"
"边界条件": "{{boundary_condition}}"
现有前提加上新前提之后，还符合边界条件吗？
{{/user}}

{{#assistant}}"判断": "{{/assistant}}
{{#assistant}}{{select "judgement" options=valid_duplicated}}{{/assistant}}
'''
)
# Define the guidance program
sourced_deduction = guidance(
'''
{{#system}}假设你是最伟大的人工智能科学家、逻辑学家和数学家之一。 让我们一步步思考。
请确定“命题”是否是从“前提”直接推导出来的，而不是通过常识推理引入无源信息，回答“对”或“错”。
----{{/system}}

{{~#each examples}}
{{#user}}
---
"前提": "{{this.premises}}"
"命题": "{{this.proposition}}"
{{/user}}

{{#assistant}}"判断": "这个命题是直接从前提推导出来的吗？ {{this.sourced}}"{{/assistant}}
{{~/each}}

{{#user}}
---
"前提": "{{premises}}"
"命题": "{{proposition}}"
{{/user}}

{{#assistant}}"判断": "这个命题是直接从前提推导出来的吗？{{/assistant}}
{{#assistant}}{{select "sourced" options=valid_sourced}}{{/assistant}}
''')


# Define the guidance program
structure_program = guidance(
'''
{{#system}}假设你是最伟大的人工智能科学家、逻辑学家和数学家之一。 让我们一步步思考。
先阅读并分析“段落”和“问题”，然后用“前提”、“边界条件”和“命题”推理给出的四个选项哪一个是所提”问题“的答案。
请确保你的推理是直接从“前提”和“命题”推导出来的，而不是通过常识推理引入无源常识和无源信息。
对于给出的四个选项，如果你认为第一个是答案，则回答A；如果你认为第二个是答案，则回答B；如果你认为第三个是答案，则回答C；如果你认为第四个是答案，则回答D,若认为4个选项都不正确，则选择K。
请注意，这是一个单选题，你只能选择你认为最正确的一个。
----{{/system}}

{{~#each examples}}
{{#user}}
---
"段落": "{{this.context}}"
"问题和选项": "{{this.question}}"
{{/user}}

{{#assistant}}"前提": "让我们一步一步思考，从段落中我们可以提取出这些前提: {{this.premises}}"{{/assistant}}
{{#assistant}}"边界条件": "让我们一步一步思考，从段落中我们可以提取出这些边界条件: {{this.boundary_condition}}"{{/assistant}}
{{#assistant}}"思考": "根据前提和边界条件，可以推导出以下这些命题：{{this.propositions}}"{{/assistant}}
{{#assistant}}"回顾问题和选项"："{{this.question}}"{{/assistant}}
{{#assistant}}"推理": "根据前提、边界条件和命题，{{this.reasoning}}"{{/assistant}}
{{#assistant}}"回顾问题和选项"："{{this.question}}"{{/assistant}}
{{#assistant}}"判断": "现在我们知道这个问题的答案应该是{{this.ans}}"{{/assistant}}
{{~/each}}

{{#user}}
---
"段落": "{{context}}"
"问题和选项": "{{question}}"
{{/user}}
{{#assistant}}"前提": "让我们一步一步思考，从段落中我们可以提取出这些前提: {{premises}}"{{/assistant}}
{{#assistant}}"边界条件": "让我们一步一步思考，从段落中我们可以提取出这些边界条件: {{boundary_condition}}"{{/assistant}}
{{#assistant}}"思考": "根据前提和边界条件，可以推导出以下这些命题：{{propositions}}"{{/assistant}}
{{#assistant}}"推理": "根据前提、边界条件和命题，{{/assistant}}
{{#assistant}}{{gen "reasoning" temperature=0.7 max_tokens=500 stop=['\\n\"']}}{{/assistant}}
{{#assistant}}"判断": "现在我们知道这个问题的答案应该是{{/assistant}}
{{#assistant}}{{select "judgement" options=choose}}{{/assistant}}
''')


# Define the guidance program
structure_program_wocot = guidance(
'''
{{#system}}假设你是最伟大的人工智能科学家、逻辑学家和数学家之一。 让我们一步步思考。
先阅读并分析“段落”和“问题”，然后用“前提”、“边界条件”和“命题”推理给出的四个选项哪一个是所提”问题“的答案。
请确保你的推理是直接从“前提”和“命题”推导出来的，而不是通过常识推理引入无源常识和无源信息。
请注意，这是一个单选题，对于给出的四个选项，如果你认为第一个是答案，则回答A；如果你认为第二个是答案，则回答B；如果你认为第三个是答案，则回答C；如果你认为第四个是答案，则回答D。若认为4个选项都不正确，则选择K。
如果可以直接从命题中得到答案，则你应该直接选出答案，否则请结合命题、前提和边界条件继续推理，直到得出唯一答案。
----{{/system}}

{{~#each examples}}
{{#user}}
---
"段落": "{{this.context}}"
"问题和选项": "{{this.question}}"
{{/user}}

{{#assistant}}"前提": "让我们一步一步思考，从段落中我们可以提取出这些前提: {{this.premises}}"{{/assistant}}
{{#assistant}}"边界条件": "让我们一步一步思考，从段落中我们可以提取出这些边界条件: {{this.boundary_condition}}"{{/assistant}}
{{#assistant}}"思考": "根据前提和边界条件，可以推导出以下这些命题：{{this.propositions}}"{{/assistant}}
{{#assistant}}"回顾问题和选项"："{{this.question}}"{{/assistant}}
{{#assistant}}"推理": "回顾前提、边界条件和命题，接着已经得到的命题继续推理，{{this.reasoning}}"{{/assistant}}
{{#assistant}}"回顾问题和选项"："{{this.question}}"{{/assistant}}
{{#assistant}}"判断": "现在我们知道这个问题的答案应该是{{this.ans}}"{{/assistant}}
{{~/each}}

{{#user}}
---
"段落": "{{context}}"
"问题和选项": "{{question}}"
{{/user}}
{{#assistant}}"前提": "让我们一步一步思考，从段落中我们可以提取出这些前提: {{premises}}"{{/assistant}}
{{#assistant}}"边界条件": "让我们一步一步思考，从段落中我们可以提取出这些边界条件: {{boundary_condition}}"{{/assistant}}
{{#assistant}}"思考": "根据前提和边界条件，可以推导出以下这些命题：{{propositions}}"{{/assistant}}
{{#assistant}}"回顾问题和选项"："{{question}}"{{/assistant}}
{{#assistant}}"判断": "现在我们知道这个问题的答案应该是{{/assistant}}
{{#assistant}}{{select "judgement" options=choose}}{{/assistant}}
''')
examples = [
    {
        'context': '办公室里有一个教育学硕士，一个教育学士，一个哲学硕士，一个哲学学士。四个人中，A是既不是教育学硕士也不是哲学学士；A和C学的是同一学科；B只有学士学位；D不学哲学。',
        'premises': 'A是既不是教育学硕士也不是哲学学士。A和C学的是同一学科。B只有学士学位；D不学哲学。',
        'boundary_condition': '办公室里有一个教育学硕士，一个教育学士，一个哲学硕士，一个哲学学士。',
        'question': '如果以上说法正确，下列哪项为真? A是教育学士。B是哲学学士。C是哲学学士。D是教育学士。',
        'propositions': 'A的学位可能是哲学硕士或者教育学学士。C的学位也可能是哲学学士或者教育学硕士。B的学位可能是教育学士或者哲学学士。D的学位可能是教育学硕士或者教育学学士。若D的学位是教育学硕士，C的学位是哲学学士。若D是教育学学士，A是哲学硕士，因此C的学位是哲学学士。',
        'options': 'A是教育学士。B是哲学学士。C是哲学学士。D是教育学士。',
        "reasoning": "从命题可知A的学位可能是哲学硕士或者教育学学士。又可知因为A和C学的是同一学科，A的学位可能是哲学硕士或者教育学学士，因此C的学位也可能是哲学学士或者教育学硕士。因为D不学哲学，因此D的学位可能是教育学硕士或者教育学学士。但是只有两个学士，所以若D的学位是教育学硕士，C的学位是哲学学士；若D是教育学学士，A是哲学硕士，因此C的学位是哲学学士。因此，D的学位无论是教育学硕士或者教育学学士，C的学位都是哲学学士。因此C是对的。",
        'ans': 'C'},
    {
        'context': '赵明、钱红、孙杰三人被北京大学、清华大学和北京师范大学录取。他们分别被哪个学校录取的，同学们作了如下的猜测：同学A猜：赵明被清华大学录取，孙杰被北京师范大学录取。同学B猜：赵明被北京师范大学录取，钱红被清华大学录取。同学C猜：赵明被北京大学录取，孙杰被清华大学录取。结果，同学们的猜测各对了一半。',
        'question': '据此,可以得到：A.赵明、钱红、孙杰分别被北京大学、清华大学和北京师范大学录取。 B.赵明、钱红、孙杰分别被清华大学、北京师范大学和北京大学录取。 C.赵明、钱红、孙杰分别被北京师范大学、清华大学和北京大学录取。 D.赵明、钱红、孙杰分别被北京大学、北京师范大学和清华大学录取。',
        'premises': '同学A猜：赵明被清华大学录取，孙杰被北京师范大学录取。同学B猜：赵明被北京师范大学录取，钱红被清华大学录取。同学C猜：赵明被北京大学录取，孙杰被清华大学录取。',
        'boundary_condition': '结果，同学们的猜测各对了一半。',
        'propositions': '赵明被北京师范大学录取，钱红被清华大学录取，孙杰被北京大学录取。',
        'options': 'A.赵明、钱红、孙杰分别被北京大学、清华大学和北京师范大学录取。 B.赵明、钱红、孙杰分别被清华大学、北京师范大学和北京大学录取。 C.赵明、钱红、孙杰分别被北京师范大学、清华大学和北京大学录取。 D.赵明、钱红、孙杰分别被北京大学、北京师范大学和清华大学录取。',
        "reasoning": "从命题中可以知道，赵明被北京师范大学录取，钱红被清华大学录取，孙杰被北京大学录取，据此我们可以直接得到答案，因此不用结合前提再做推理，最终答案是C。",
        'ans': 'C'},
    {
        'context': '最聪明的骗子可能在某一时刻欺骗所有人，也可能在任何时候都欺骗一部分人，但绝对不可能在任何时刻欺骗所有人 .',
        'question': '根据上述说法，以下哪项是不正确的？ A.不可能在任何时刻欺骗所有人。B.一个人可能在任何时候都被欺骗。C.一个人可能在任何时候都不会被欺骗。D.在某个时刻，每个人都不可能被欺骗。',
        'premises': '最聪明的骗子可能在某一时刻欺骗所有人。可能在任何时候都欺骗一部分人。绝对不可能在任何时刻欺骗所有人。',
        'boundary_condition': '无',
        'propositions': '任何人在某个时刻都可能被欺骗。',
        'options': '不可能在任何时刻欺骗所有人。一个人可能在任何时候都被欺骗。一个人可能在任何时候都不会被欺骗。在某个时刻，每个人都不可能被欺骗。',
        "reasoning": "从命题可知，任何人在某个时刻都可能被欺骗，所以’在某个时刻，每个人都不可能被欺骗‘和’任何人在某个时刻都可能被欺骗‘之间是矛盾的。因此D是错的。",
        'ans': 'D'},
    {
        'context': '甲,乙,丙三人去餐厅吃饭,服务员想知道他们三人分别是干什么的,但三人只提供了以下信息：三人中一位是工程师,一位是教授,一位是医生;丙比医生年龄大,甲和教授不同岁,教授比乙年龄小.',
        'question': '据此可以推出：A.甲是工程师,乙是教授,丙是医生。B.甲是教授,乙是医生,丙是工程师。C.甲是医生,乙是工程师,丙是教授。D.甲是医生,乙是教授,丙是工程师',
        'premises': '丙比医生年龄大,甲和教授不同岁,教授比乙年龄小.',
        'boundary_condition': '甲,乙,丙三人中一位是工程师,一位是教授,一位是医生',
        'propositions': '丙不可能是医生。教授不可能是乙。甲和教授不同岁，教授不可能是甲。丙是教授。',
        'options': 'A.甲是工程师,乙是教授,丙是医生。B.甲是教授,乙是医生,丙是工程师。C.甲是医生,乙是工程师,丙是教授。D.甲是医生,乙是教授,丙是工程师 ',
        "reasoning": "从命题中可以知道，丙是教授。而甲和乙的职业无法确定。但是根据丙是教授，只有C满足这个要求，因此最终答案是C。",
        'ans': 'C'},
{
        'context': 'G、H、J、K、L、M和O七人结伴出游。在他们4天的露营生活中，每天要安排两个人值班为大家做饭。要求这4天的人员安排不能重复，且恰好有一人值班两天。此外，值班安排还须满足下列条件：(1)J要排在H值班的次日。(2)值班两天的那个人必须排在第四天，不能排在第三天。(3)G必须与J和O中的某一个人排在同一天。(4)第一天或第二天至少有一天安排K。(5)O必须排在第三天。',
        'question': '50.以下哪个人可以排在任意一天?A.H B.J C.K D.L',
        'premises': '(1)J要排在H值班的次日。(2)值班两天的那个人必须排在第四天，不能排在第三天。(3)G必须与J和O中的某一个人排在同一天。(4)第一天或第二天至少有一天安排K。(5)O必须排在第三天。',
        'boundary_condition': '七人结伴出游。在他们4天的露营生活中，每天要安排两个人值班为大家做饭。要求这4天的人员安排不能重复，且恰好有一人值班两天。',
        'propositions': 'O必须在第三天值班。值班两天的那个人必须排在第四天，且不是O。K不能在第四天值班。值班两天的那个人不是K。',
        'options': 'A.H B.J C.K D.L ',
        "reasoning": "从命题中可以知道，O必须在第三天值班，因此O不能排在任意一天；根据J要排在H值班的次日，所以J不能排在第一天，H不能排在第四天；值班两天的那个人必须排在第四天，且不是O，所以J也不能排在第四天；K不能在第四天值班，但可以在第一天或第二天值班。综上所述，只有L没有任何限制，可以排在任意一天，因此最终答案是D。",
        'ans': 'D'},
]

# final-question with reasoning memory
structure_program_memory = guidance(
'''
{{#system}}假设你是最伟大的人工智能科学家、逻辑学家和数学家之一。 让我们一步步思考。
先阅读并分析“段落”和“问题”，然后用“前提”、“边界条件”和“命题”推理给出的四个选项哪一个是所提”问题“的答案。
请确保你的推理是直接从“前提”和“命题”推导出来的，而不是通过常识推理引入无源常识和无源信息。
请注意，这是一个单选题,对于给出的四个选项，如果你认为第一个是答案，则回答A；如果你认为第二个是答案，则回答B；如果你认为第三个是答案，则回答C；如果你认为第四个是答案，则回答D。若认为4个选项都不正确，则选择K。
如果可以直接从命题中得到答案，则你应该直接选出答案，否则请结合命题、前提和边界条件继续推理，直到得出唯一答案。
----{{/system}}

{{~#each examples}}
{{#user}}
---
"段落": "{{this.context}}"
"问题和选项": "{{this.question}}"
{{/user}}

{{#assistant}}"前提": "让我们一步一步思考，从段落中我们可以提取出这些前提: {{this.premises}}"{{/assistant}}
{{#assistant}}"边界条件": "让我们一步一步思考，从段落中我们可以提取出这些边界条件: {{this.boundary_condition}}"{{/assistant}}
{{#assistant}}"思考": "根据前提和边界条件，可以推导出以下这些命题：{{this.propositions}}"{{/assistant}}
{{#assistant}}"回顾问题和选项"："{{this.question}}"{{/assistant}}
{{#assistant}}"推理": "利用前提、边界条件，接着已经得到的命题继续推理，{{this.reasoning}}"{{/assistant}}
{{#assistant}}"回顾问题和选项"："{{this.question}}"{{/assistant}}
{{#assistant}}"判断": "现在我们知道这个问题的答案应该是{{this.ans}}"{{/assistant}}
{{~/each}}

{{#user}}
---
"段落": "{{context}}"
"问题和选项": "{{question}}"
{{/user}}
{{#assistant}}"前提": "让我们一步一步思考，从段落中我们可以提取出这些前提: {{premises}}"{{/assistant}}
{{#assistant}}"回顾一下这些命题的推导历史": "{{infer_history}}"{{/assistant}}
{{#assistant}}"边界条件": "让我们一步一步思考，从段落中我们可以提取出这些边界条件: {{boundary_condition}}"{{/assistant}}
{{#assistant}}"思考": "根据前提和边界条件，可以推导出以下这些命题：{{propositions}}"{{/assistant}}
{{#assistant}}"回顾问题和选项"："{{question}}"{{/assistant}}
{{#assistant}}"推理": "利用前提、边界条件，接着已经得到的命题继续推理，{{/assistant}}
{{#assistant}}{{gen "reasoning" temperature=0.7 max_tokens=500 stop=['\\n\"']}}{{/assistant}}
{{#assistant}}"回顾问题和选项"："{{question}}"{{/assistant}}
{{#assistant}}"判断": "现在我们知道这个问题的答案应该是{{/assistant}}
{{#assistant}}{{select "judgement" options=choose}}{{/assistant}}
''')
# Determine premise type.
divide_judgement_examples = [
    {
        'premises': 'All animals breathe.',
        'Analysis': 'This premise doesn\'t have any keywords with assumptions, so it doesn\'t have information with assumptions.',
        'Judgement': 'True'},
    {
        'premises': 'If the eel is a plant, it can live on land.',
        'Analysis': 'The premise contains the assumption key word "if", so it have a hypothetical message.',
        'Judgement': 'False'},
    {
        'premises': 'Unless the grey rhino is an animal, it cannot run on land',
        'Analysis': 'The premise contains the assumption key word "unless", so it have a "if" message.',
        'Judgement': 'False'},
    {
        'premises': 'Miroslav Venhoda was a Czech choral conductor who specialized in the performance of Renaissance and Baroque music.',
        'Analysis': 'This premise doesn\'t have any keywords with assumptions, so it doesn\'t have information with assumptions.',
        'Judgement': 'True'}
]
# Define the guidance program
premise_judgement = guidance(
'''
{{#system}}Suppose you are one of the greatest AI scientists, logicians and mathematicians. Let us think step by step. 
Read and analyze the definition given below first, then using the definition to judge whether the premise given below is a fact or not,reply with True or False.
Facts: The content of the premise is all objective facts, without any assumptions.At least, without the following keywords: "if","Unless","As long as","or".
Please make sure your classification decisions are derived directly from definitions and examples, rather than introducing unsourced common sense and unsourced information through common-sense reasoning.
----{{/system}}

{{~#each examples}}
{{#user}}
---
"Premises": "{{this.premises}}"
{{/user}}
{{#assistant}}"Definition": "Facts: The content of the premise is all objective facts, without any assumptions.At least, without the following keywords: "if","Unless","As long as","or"."{{/assistant}}
{{#assistant}}"Explanation": "{{this.Analysis}}"{{/assistant}}
{{#assistant}}"Judgement": "Is this premise a Fact? {{this.Judgement}}"{{/assistant}}
{{~/each}}

{{#user}}
---
"Premises": "{{premises}}"
{{/user}}

{{#assistant}}"Definition": "Facts: The content of the premise is all objective facts, without any assumptions or uncertain information.At least, without the following keywords: "if","Unless","As long as","or"."{{/assistant}}
{{#assistant}}"Judgement": "Is this premise a Fact? {{/assistant}}
{{#assistant}}{{select "validation" options=valid_validation}}{{/assistant}}
''')

condition_select_history = guidance(
'''
{{#system}}Suppose you are one of the greatest AI scientists, logicians and mathematicians. Let us think step by step. 
Read and analyze the "determinate_premise" and "indeterminate_premise" first, then selecting several determinate_premise and rule from them.The purpose of selection is to prepare for the next step of reasoning.
If you are given a reasoning history, do not select a combination of "indeterminate_premise" and "determinate_premise" that has already been selected in the history.
There are two ways to choose them: you can choose the "determinate_premise" and "indeterminate_premise" that is directly related to "Hypothesis". Or you can choose "determinate_premise" and "indeterminate_premise" that have nothing to do with "Hypothesis" for the time being, but they have common information interactions.
----{{/system}}

{{~#each examples}}

{{#user}}
---
"determinate_premise": "{{this.determinate_premise}}"
"indeterminate_premise": "{{this.indeterminate_premise}}"
"Hypothesis": "{{this.Hypothesis}}"
{{/user}}

{{#assistant}}"Results": "{{this.Results}}"{{/assistant}}
{{#assistant}}"Explanation": "{{this.Explanation}}"{{/assistant}}
{{~/each}}
{{#user}}
---
"determinate_premise": "{{determinate_premise}}"
"indeterminate_premise": "{{indeterminate_premise}}"
"Hypothesis": "{{Hypothesis}}"
"Reasoning history": {{infer_history}}
{{/user}}
{{#assistant}}"Results": {{/assistant}}
{{#assistant}}{{gen "results" temperature=0.7 max_tokens=200 stop='\n'}}{{/assistant}}
'''
)
conditions_scores_examples = [
    {
        'determinate_premise': 'C need to be kept.',
        'indeterminate_premise': 'If you keep statement A, you must keep statement B and statement C. If you keep statement D, you must delete both statement E and statement C.Statement A is important information and cannot be deleted.Statement E and statement F should be saved at the same time.',
        'Hypothesis': 'D and C need to be kept',
        'last_history': 'In the last round, we use this "most relevant premise": "If you keep statement A, you must keep statement B and statement C."and got a "New Proposition": If you keep statement D, you must delete both statement E and statement C.',
        'explanation': 'From the determinate_premise, select the "Most relevant premise" which has the same subject with "Hypothesis",for this premise it is C.',
        'Most_relevant_premise': 'C need to be kept.(0.25)',
        'Other_premises_scores': 'If you keep statement A, you must keep statement B and statement C.(0.25)  If you keep statement D, you must delete both statement E and statement C.(0.25) Statement A is important information and cannot be deleted.(0.0) Statement E and statement F should be saved at the same time.(0.0)',
        'Results': 'If you keep statement D, you must delete both statement E and statement C. If you keep statement A, you must keep statement B and statement C.C need to be kept.'
    },
    {
        'determinate_premise': 'The bear is big. Bear is blue.',
        'indeterminate_premise': 'The tiger is rough. If bear is big, then bear is red. If someone is big, then they are nice.',
        'Hypothesis': 'bear is rough.',
        'last_history': 'There\'s no Last_reasoning_history yet, because this is the first derivation.',
        'Most_relevant_premise': 'The bear is big.(0.25)',
        'Other_premises_scores': 'If bear is big, then bear is red.(0.8)The tiger is rough.(0.0) If someone is big, then they are nice.(0.55)',
        'Results': 'The bear is big.If someone is big, then they are nice.If bear is big, then bear is red.',
        'explanation': 'The scores of "If bear is big, then bear is red." is 0.8, because they have the same noun and adjective +0.55, and "The bear is big." is the premise of "If bear is big, then bear is red."+0.25, so the score is 0.8.'
    }
]

conditions_scores_examples_2 = [
    {
        'determinate_premise': '牡丹不在在2号展室展出。牡丹不在4号画室展出。牡丹不在3号画室展出。',
        'indeterminate_premise': '猛虎和雄鸡不在同一展室展出。奔马和仙鹤应在同一展室展出。 仙鹤或腊梅在4号展室展出。',
        'boundary_condition': '一幅画只能在一个画室展出，一个画室可以展出多幅画。',
        'count': '牡丹（3次）仙鹤（2次）4号展室（2次）3号展室（1次）2号展室（1次）猛虎（1次）雄鸡（1次）奔马（1次）腊梅（1次）',
        'topic': '不同的画在不同的画室的展出情况。',
        'last_false_history': '上一轮中，选择次数最多的牡丹作为筛选标准，因为牡丹的画室尚未完全确定。但是没有得到有效的命题。',
        'explanation': '没有选择次数最多的牡丹作为筛选标准，在上一轮中选择了牡丹但是没有得到有效的命题，这一轮不能再选，因此应该选择被提及第二多的仙鹤作为标准。',
        'Most_relevant_premise': '仙鹤',
        'Results': '奔马和仙鹤应在同一展室展出。 仙鹤或腊梅在4号展室展出。'
    },
    {
        'determinate_premise': '牡丹在2号展室展出。牡丹不在4号画室展出。牡丹不在3号画室展出。',
        'indeterminate_premise': '猛虎和雄鸡不在同一展室展出。奔马和仙鹤应在同一展室展出。 仙鹤或腊梅在4号展室展出。',
        'boundary_condition': '一幅画只能在一个画室展出，一个画室可以展出多幅画。',
        'count': '牡丹（3次）仙鹤（2次）4号展室（2次）3号展室（1次）2号展室（1次）猛虎（1次）雄鸡（1次）奔马（1次）腊梅（1次）',
        'topic': '不同的画在不同的画室的展出情况。',
        'last_false_history': '还没有历史信息。',
        'explanation': '没有选择次数最多的牡丹作为筛选标准，因为一幅画只能在一个画室展出，从牡丹在2号展室展出可知，牡丹的取值已经确定，因此应该选择被提及第二多的仙鹤作为标准。',
        'Most_relevant_premise': '仙鹤',
        'Results': '奔马和仙鹤应在同一展室展出。 仙鹤或腊梅在4号展室展出。'
    },
    {
        'determinate_premise': '无。',
        'indeterminate_premise': '甲、乙、丙的学历层次相同，己、庚的学历层次不同；戊、己、庚的性别相同，甲、丁的性别不同。博士毕业的有 3 人；女性 3 人。最终录用的是一名女博士。',
        'boundary_condition': '7人中最高学历分别是本科和博士。',
        'count': '性别（4次）学历（4次）博士（2次）甲（2次）己（2次）庚（2次）戊（1次）',
        'topic': '在某科室公开选拔副科长的招录考试中，甲、乙、丙、丁、戊、己、庚7人报名的学历和性别。',
        'last_false_history': '上一轮中，我们选择了学历作为筛选主题。但是没有获得有效命题。',
        'explanation': '学历在上一轮中被选择了，但没有获得有效命题，因此这一轮不能选。和性别相关的话题可以作为选择，因此将其作为标准。',
        'Most_relevant_premise': '性别',
        'Results': '戊、己、庚的性别相同，甲、丁的性别不同。女性 3 人。'
    },
]
# Premise Prioritization
condition_select_score_2 = guidance(
'''
{{#system}}假设你是最伟大的人工智能科学家、逻辑学家和数学家之一。让我们一步步思考。
首先阅读并分析“确定前提”和“不确定前提”，然后从中筛选出几个前提。
当你确定主题时，请先阅读一次推理历史，不要选择之前失败过的主题作为这一轮的选择。
请按照以下步骤操作：
1.统计各个主题被前提提及的累计次数，和主题相关的都需要被计数，例如(主题：性别 那么男性和女性都需要被记录。)
2.按照被提及的次数从高到低，对主题进行判定,如果被提及个数相同，则优先选择涉及确定前提多的那个主题。
3.该主题的取值在当前话题下是否已经完全确定，如果完全确定，则寻找并判定下一个主题，如果还没有完全确定，则进入第4步。
4.将该主题作为前提筛选的标准，筛选出和该主题相关的所有前提。
----{{/system}}

{{~#each examples}}
{{#user}}
---
"确定前提": "{{this.determinate_premise}}"
"非确定前提": "{{this.indeterminate_premise}}"
"核心话题": "{{this.topic}}"
"边界条件": "{{this.boundary_condition}}"
"推理历史"： "{{this.last_false_history}}"
{{/user}}
{{#assistant}}你可以统计各个主题被前提提及的累计次数吗？{{/assistant}}
{{#assistant}}"次数统计": "{{this.count}}"{{/assistant}}
{{#assistant}}你应该选择哪个主题作为前提筛选的标准？{{/assistant}}
{{#assistant}}"分析": "{{this.explanation}}"{{/assistant}}
{{#assistant}}和这个主题相关的所有前提是？{{/assistant}}
{{#assistant}}"筛选结果": "{{this.Results}}"{{/assistant}}
{{~/each}}

{{#user}}
---
"确定前提": "{{determinate_premise}}"
"非确定前提": "{{indeterminate_premise}}"
"核心话题": "{{topic}}"
"边界条件": "{{boundary_condition}}"
"推理历史"： "{{last_false_history}}"
{{/user}}
{{#assistant}}你可以统计各个主题被前提提及的累计次数吗？{{/assistant}}
{{#assistant}}"次数统计": "{{/assistant}}
{{#assistant}}{{gen "count" temperature=temperature max_tokens=200 stop='\n'}}{{/assistant}}
{{#assistant}}你应该选择哪个主题作为前提筛选的标准？{{/assistant}}
{{#assistant}}"分析": "{{/assistant}}
{{#assistant}}{{gen "explanation" temperature=temperature max_tokens=200 stop='\n'}}{{/assistant}}
{{#assistant}}和这个主题相关的所有前提是？{{/assistant}}
{{#assistant}}"筛选结果": "{{/assistant}}
{{#assistant}}{{gen "results" temperature=temperature max_tokens=200 stop='\n'}}{{/assistant}}
'''
)
conditions_scores_examples_3 = [
    {
        'determinate_premise': '牡丹在2号展室展出。牡丹不在4号画室展出。牡丹不在3号画室展出。',
        'indeterminate_premise': '猛虎和雄鸡不在同一展室展出。奔马和仙鹤应在同一展室展出。 仙鹤或腊梅在4号展室展出。',
        'boundary_condition': '一幅画只能在一个画室展出，一个画室可以展出多幅画。',
        'count': '牡丹（3次）仙鹤（2次）4号展室（2次）3号展室（1次）2号展室（1次）猛虎（1次）雄鸡（1次）奔马（1次）腊梅（1次）',
        'topic': '不同的画在不同的画室的展出情况。',
        'explanation': '没有选择次数最多的牡丹作为筛选标准，因为一幅画只能在一个画室展出，从牡丹在2号展室展出可知，牡丹的取值已经确定，因此应该选择被提及第二多的仙鹤作为标准。',
        'Most_relevant_premise': '仙鹤',
        'Results': '奔马和仙鹤应在同一展室展出。 仙鹤或腊梅在4号展室展出。'
    },
    {
        'determinate_premise': '仙鹤不在4号展室展出。',
        'indeterminate_premise': '猛虎和雄鸡不在同一展室展出。奔马和仙鹤应在同一展室展出。 仙鹤或腊梅在4号展室展出。',
        'boundary_condition': '一幅画只能在一个画室展出，一个画室可以展出多幅画。',
        'count': '仙鹤（3次）4号展室（2次）牡丹（1次）猛虎（1次）雄鸡（1次）奔马（1次）腊梅（1次）',
        'topic': '不同的画在不同的画室的展出情况。',
        'explanation': '一幅画只在一个画室展出，考虑仙鹤是否可以作为标准：现在知道了仙鹤不在4号展室展出，但是还无法确定具体在哪个画室展出，因此可以将仙鹤作为选择标准。',
        'Most_relevant_premise': '仙鹤',
        'Results': '仙鹤不在4号展室展出。奔马和仙鹤应在同一展室展出。仙鹤或腊梅在4号展室展出。'
    },
    {
        'determinate_premise': '无。',
        'indeterminate_premise': '甲、乙、丙的学历层次相同，己、庚的学历层次不同；戊、己、庚的性别相同，甲、丁的性别不同。博士毕业的有 3 人；女性 3 人。最终录用的是一名女博士。',
        'boundary_condition': '7人中最高学历分别是本科和博士。',
        'count': '性别（4次）学历（4次）博士（2次）甲（2次）己（2次）庚（2次）戊（1次）',
        'topic': '在某科室公开选拔副科长的招录考试中，甲、乙、丙、丁、戊、己、庚7人报名的学历和性别。',
        'explanation': '和性别相关的话题确定性更大，因此将其作为标准。',
        'Most_relevant_premise': '性别',
        'Results': '戊、己、庚的性别相同，甲、丁的性别不同。女性 3 人。'
    },
    {
        'determinate_premise': '牡丹在2号展室展出。牡丹不在4号画室展出。牡丹不在3号画室展出。仙鹤在2号展室展出。',
        'indeterminate_premise': '猛虎和雄鸡不在同一展室展出。 仙鹤或腊梅在4号展室展出。',
        'boundary_condition': '一幅画只能在一个画室展出，一个画室可以展出多幅画。',
        'count': '牡丹（3次）2号展室（2次）4号展室（2次）仙鹤（2次）猛虎（1次）雄鸡（1次）奔马（1次）腊梅（1次）3号展室（1次）',
        'topic': '不同的画在不同的画室的展出情况。',
        'explanation': '没有选择次数最多的牡丹作为筛选标准，因为一幅画只能在一个画室展出，从牡丹在2号展室展出可知，牡丹的取值已经确定，但被提及第二多的仙鹤也确定在二号展出，因此需要继续选择剩下的前提，猛虎尚未确定，他也是第三多的变量，因此，可以选择猛虎作为标准。',
        'Most_relevant_premise': '仙鹤',
        'Results': '奔马和仙鹤应在同一展室展出。 仙鹤或腊梅在4号展室展出。最终录用的是一名女博士。'
    },
]
condition_select_score_3 = guidance(
'''
{{#system}}假设你是最伟大的人工智能科学家、逻辑学家和数学家之一。让我们一步步思考。
首先阅读并分析“确定前提”和“不确定前提”，然后从中筛选出几个前提。
请按照以下步骤操作：
1.统计各个主题被前提提及的累计次数，和主题相关的都需要被计数，例如（主题：性别 那么男性和女性都需要被记录。）
2.按照被提及的次数从高到低，对主题进行判定,如果被提及个数相同，则优先选择涉及确定前提多的那个主题。
3.该主题的取值在当前话题下是否已经完全确定，如果完全确定，则寻找并判定下一个主题，如果还没有完全确定，则进入第4步。
4.将该主题作为前提筛选的标准，筛选出和该主题相关的所有前提。
----{{/system}}

{{~#each examples}}
{{#user}}
---
"确定前提": "{{this.determinate_premise}}"
"非确定前提": "{{this.indeterminate_premise}}"
"核心话题": "{{this.topic}}"
"边界条件": {{this.boundary_condition}}
{{/user}}
{{#assistant}}你可以统计各个主题被前提提及的累计次数吗？{{/assistant}}
{{#assistant}}"次数统计": "{{this.count}}"{{/assistant}}
{{#assistant}}你应该选择哪个主题作为前提筛选的标准？{{/assistant}}
{{#assistant}}"分析": "{{this.explanation}}"{{/assistant}}
{{#assistant}}和这个主题相关的所有前提是？{{/assistant}}
{{#assistant}}"筛选结果": "{{this.Results}}"{{/assistant}}
{{~/each}}

{{#user}}
---
"确定前提": "{{determinate_premise}}"
"非确定前提": "{{indeterminate_premise}}"
"核心话题": "{{topic}}"
"边界条件": {{boundary_condition}}
{{/user}}
{{#assistant}}你可以统计各个主题被前提提及的累计次数吗？{{/assistant}}
{{#assistant}}"次数统计": "{{/assistant}}
{{#assistant}}{{gen "count" temperature=temperature max_tokens=200 stop='\n'}}{{/assistant}}
{{#assistant}}你应该选择哪个主题作为前提筛选的标准？{{/assistant}}
{{#assistant}}"分析": "{{/assistant}}
{{#assistant}}{{gen "explanation" temperature=temperature max_tokens=200 stop='\n'}}{{/assistant}}
{{#assistant}}和这个主题相关的所有前提是？{{/assistant}}
{{#assistant}}"筛选结果": "{{/assistant}}
{{#assistant}}{{gen "results" temperature=temperature max_tokens=200 stop='\n'}}{{/assistant}}
'''
)
condition_select_score_1 = guidance(
'''
{{#system}}Suppose you are one of the greatest AI scientists, logicians and mathematicians. Let us think step by step. 
Read and analyze the "determinate_premise" and "indeterminate_premise" first, then selecting several premises from them. 
Read the "Last_reasoning_history".If we got a "false Proposition" in history,when you select "Most_relevant_premise",do not choose the same "Most relevant premise" in history as your answer.
Please follow these steps:
1.From the determinate_premise, select the "Most relevant premise" which has the same subject with "Hypothesis", and give a score from 0 to 1.
2.You need to assess how the "Most relevant premise" relates to all the other "determinate_premise" and "indeterminate_premise",based on Relevance scoring rules.
3.The "determinate_premise" and "indeterminate_premise" with scores higher than 0.25 will be used as the final results, along with Most_relevant_premise.
Relevance scoring rules:
1. When scoring relevance, 0.25 added for each noun or 0.3 added for each adjective that is the same between two sentences.
2. Scores start to accumulate from 0 points, and the upper limit is 1 point.
3. If sentence p1 is a hypothetical premise of sentence p2,then add 0.25 to p2. for example: measure "if A then B." and "A is true." Then add 0.25 points to "if A then B".
----{{/system}}

{{~#each examples}}
{{#user}}
---
"determinate_premise": "{{this.determinate_premise}}"
"indeterminate_premise": "{{this.indeterminate_premise}}"
"Hypothesis": "{{this.Hypothesis}}"
"Last_reasoning_history": "{{this.last_history}}"
{{/user}}
{{#assistant}}Can you select the premise from the "determinate_premises" that scores the highest score for Relevance scoring rules to the "hypothesis"?{{/assistant}}
{{#assistant}}"Most_relevant_premise": "{{this.Most_relevant_premise}}"{{/assistant}}
{{#assistant}}Can you assess how the "Most relevant premise" relates to all the other "determinate_premise" and "indeterminate_premise" accoding to Relevance scoring rules?{{/assistant}}
{{#assistant}}"Other_premises_scores": "{{this.Other_premises_scores}}"{{/assistant}}
{{#assistant}}"Results": "{{this.Results}}"{{/assistant}}
{{~/each}}

{{#user}}
---
"determinate_premise": "{{determinate_premise}}"
"indeterminate_premise": "{{indeterminate_premise}}"
"Hypothesis": "{{Hypothesis}}"
"Last_reasoning_history": "{{last_history}}"
{{/user}}
{{#assistant}}Can you select the premise from the "determinate_premises" that scores the highest score for Relevance scoring rules to the "hypothesis"?{{/assistant}}
{{#assistant}}"Most_relevant_premise": "{{/assistant}}
{{#assistant}}{{gen "Most_relevant_premise" temperature=0.7 max_tokens=200 stop='\n'}}{{/assistant}}
{{#assistant}}Can you assess how the "Most relevant premise" relates to all the other "determinate_premise" and "indeterminate_premise" accoding to Relevance scoring rules?{{/assistant}}
{{#assistant}}"Other_premises_scores": "{{/assistant}}
{{#assistant}}{{gen "Other_premises_scores" temperature=0.7 max_tokens=200 stop='\n'}}{{/assistant}}
{{#assistant}}"Results": "{{/assistant}}
{{#assistant}}{{gen "results" temperature=0.7 max_tokens=200 stop='\n'}}{{/assistant}}
'''
)
# Verify whether the premise is directly helpful to the hypothesis.
useful_deduction_examples = [
    {'Premise': '张三会说四川方言。',
     'Explanation': '这句话肯定了张三对“四川方言”这门语言的取值，并且没有假设、联言、选言的成分。所以他是一个肯定前提，也是一个确定前提。',
     'topic': '张三、李四、王五三个人对方言的掌握情况。',
     'usefulness': 'True'},
    {'Premise': '灰色兔子不可爱。',
     'Explanation': '这句话否定了兔子对“可爱”这个属性的取值，并且没有假设、联言、选言的成分。所以他是一个否定前提，也是一个确定前提。',
     'topic': '不同种类的兔子是否可爱。',
     'usefulness': 'True'},
    {'Premise': '丙比甲年龄大。',
     'topic': '甲乙丙丁戊五个人的年龄排序。',
    'Explanation': '这句话比较了甲乙之间的年龄大小关系，但不能以此判断丙在五个人中具体的年龄位次，所以他是一个非确定前提。',
     'usefulness': 'False'},
    {'Premise': '如果王伟是高个子，那么李达是矮个子',
     'Explanation': '这个前提是“如果……那么……”的结构，我们无法具体确定王伟和李达的身高情况。所以他是一个充分条件假言前提，也是一个非确定前提。',
     'topic': '四个男人的身体状态。',
     'usefulness': 'False'},
    {'Premise': '只有乔治参赛，比利才参加比赛。',
     'topic': '乔治、比利、亨德拉、阿山是否参加羽毛球比赛。',
     'Explanation': '这个前提是“只有……才……”的结构。我们无法具体确定乔治和比利是否参赛。所以他是一个必要条件假言前提，也是一个非确定前提。',
     'usefulness': 'False'},
    {'Premise': '甲和乙二人中有一个人去南京，但是他们不可以同时去。',
     'topic': '甲乙丙丁戊五个人的出差情况。',
     'Explanation': '这句话的含义是要么甲去南京，要么乙去南京。表达甲乙二人二选一，因此他是一个选言前提，也是一个非确定前提。',
     'usefulness': 'False'},
    {'Premise': '甲和乙都喜欢绿茶。',
     'topic': '甲乙丙丁戊五个人分别喜欢的饮品。',
     'Explanation': '这个前提是“……和……”的结构。以他是一个联言前提，也是一个非确定前提。',
     'usefulness': 'False'}
]
premise_divide_judgement = ["True", "False"]
# Define the guidance program
useful_deduction = guidance(
'''
{{#system}}假设你是最伟大的人工智能科学家、逻辑学家和数学家之一。 让我们一步步思考。
首先,阅读并分析以下的定义：
1.确定前提有以下两种：
（1）肯定前提：肯定核心话题中某个具体变量和取值之间的关系。（例：A是B）
（2）否定前提：否定核心话题中某个具体变量和取值之间的关系。（例：A不是B）
2.非确定前提可以为以下五类：
（1）充分条件假言前提
充分条件假言前提是陈述某一事物是另一事物充分条件的假言前提。(例：若A则B,A->B)
（2）必要条件假言前提
必要条件假言前提是陈述某一事物是另一事物必要条件的假言前提。(例：只有A才B，B->A)
（3）联言前提：是陈述事物同时存在的前提，（例：p并且q）
（4）相容性选言前提：是指子简单前提至少有一个是真并且可以不止一个为真的前提。（例：p或者q）
（5）不相容性选言前提：是指子前提中有且仅有一个为真。(例：要么p，要么q。)
其次，阅读并分析“前提“和”核心话题“，你首先需要判定这个“前提”属于上面哪一个具体类别，并以此判定判断该“前提”是否为“确定前提”。
第三，请确保您的分类决策直接来自定义，而不是无源常识。
----{{/system}}

{{~#each examples}}
{{#user}}
---
"前提": "{{this.Premise}}"
"核心话题": "{{this.topic}}"
{{/user}}
{{#assistant}}这个前提是否是确定前提？{{/assistant}}
{{#assistant}}"分析": "{{this.Explanation}}"{{/assistant}}
{{#assistant}}"判断": "{{this.usefulness}}" {{/assistant}}
{{~/each}}

{{#user}}
---
"前提": "{{Premise}}"
"核心话题": "{{topic}}"
{{/user}}
{{#assistant}}这个前提是否是确定前提？{{/assistant}}
{{#assistant}}"分析": "{{/assistant}}
{{#assistant}}{{gen "Explanation" temperature=temperature max_tokens=200 stop='\n'}}{{/assistant}}
{{#assistant}}"判断": "{{/assistant}}
{{#assistant}}{{select "usefulness" options=valid_validation}}{{/assistant}}
''')
