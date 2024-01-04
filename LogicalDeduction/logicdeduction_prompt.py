import guidance

validate_deduction_examples = [
    {'premises': 'The truck is older than the bus. The bus is older than the sedan.',
     'boundary_condition': 'In an antique car show, there are three vehicles: a minivan, a bus, and a sedan.',
     'proposition': 'The truck is older than the sedan.',
     'validation': 'True'},
    {'premises': 'The truck is older than the bus. The bus is older than the sedan.',
     'boundary_condition': 'In an antique car show, there are three vehicles: a minivan, a bus, and a sedan.',
     'proposition': 'The bus is the second oldest',
     'validation': 'True'},
    {'premises': 'The truck is older than the bus. The bus is older than the sedan.',
     'boundary_condition': 'In an antique car show, there are three vehicles: a minivan, a bus, and a sedan.',
     'proposition': 'The truck is younger than the sedan.',
     'validation': 'False'},
    {'premises': 'The raven is to the right of the blue jay.The cardinal is the leftmost.The robin is to the right of the raven.',
     'boundary_condition': 'On a branch, there are five birds: a cardinal, a robin, a blue jay, a quail, and a raven.',
     'proposition': 'The blue jay is the second from the left.',
     'validation': 'False'},
    {'premises': 'If A is the second from the left. B is on the left of A.',
     'boundary_condition': 'On a branch, there are three people: A,B and C.',
     'proposition': 'B is the first from the right.',
     'validation': 'False'},
    {'premises': 'The minivan is newer than the hatchback.The truck is newer than the limousine.The bus is newer than the hatchback.The bus is newer than the minivan.The motorcyle is newer than the truck.',
     'boundary_condition': 'In an antique car show, there are seven vehicles: a bus, a motorcyle, a hatchback, a station wagon, a minivan, a truck, and a limousine. ',
     'proposition': 'The minivan is newer than the hatchback and the bus.',
     'validation': 'False'},
    {'premises': 'Joe finished below Dan.Dan finished below Rob.',
     'boundary_condition': 'In a golf tournament, there were five golfers: Ada, Eli, Amy, Joe, and Mel. ',
     'proposition': 'Rob finished below Joe.',
     'validation': 'False'}
]
# reasoning source validation: whether comes from the set of premises.
sourced_deduction_examples = [
    {'premises': 'B is the third from the left, and C is to the left of B.',
     'boundary_condition': 'On a branch, there are three people: A,B and C.',
     'proposition': 'C is rounder than B',
     'sourced': 'False'},
     {
      'premises': 'B is the second from the right, and C is to the right of B.',
      'boundary_condition': 'On a branch, there are three people: A,B and C. ',
      'proposition': 'B is the first from the right.',
      'sourced': 'True'},
     {
      'premises': 'The falcon is to the right of the owl. The hummingbird is to the left of the owl.',
      'boundary_condition': 'On a branch, there are three birds: a hummingbird, an owl, and a falcon. ',
      'proposition': 'The owl is the second from the left.',
      'sourced': 'True'},
    {
      'premises': 'The falcon is to the right of the owl. The hummingbird is to the left of the owl.',
      'boundary_condition': 'On a branch, there are three birds: a hummingbird, an owl, and a falcon. ',
      'proposition': 'Billy is the second from the left.',
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

# ans corresponding to the dataset of three objects
choose_3 = ["A", "B", "C"]
# ans corresponding to the dataset of five objects
choose_5 = ["A", "B", "C", "D", "E"]
# ans corresponding to the dataset of seven objects
choose_7 = ["A", "B", "C", "D", "E", "F", "G"]

# examples uesd for final-question
examples = [
    {
        'context': 'The following paragraphs each describe a set of seven objects arranged in a fixed order. The statements are logically consistent within each paragraph.\n\nOn a branch, there are seven birds: a falcon, a crow, a hawk, a hummingbird, a blue jay, a robin, and a raven. The blue jay is to the right of the robin. The hawk is to the left of the hummingbird. The robin is the second from the right. The falcon is the third from the left. The crow is to the right of the hummingbird. The raven is the second from the left.',
        'premises': 'The blue jay is to the right of the robin. The hawk is to the left of the hummingbird. The robin is the second from the right. The falcon is the third from the left. The crow is to the right of the hummingbird. The raven is the second from the left.',
        'boundary_condition': 'On a branch, there are seven birds: a falcon, a crow, a hawk, a hummingbird, a blue jay, a robin, and a raven.',
        'question': 'Which of the following is true? A) The falcon is the third from the right.B) The crow is the third from the right.C) The hawk is the third from the right.D) The hummingbird is the third from the right.E) The blue jay is the third from the right.F) The robin is the third from the right.G) The raven is the third from the right.',
        'propositions': 'Hummingbird is the forth from the left. The blue jay is the first from the right. The hawk is the first from the left.',
        'options': 'A) The falcon is the third from the right.B) The crow is the third from the right.C) The hawk is the third from the right.D) The hummingbird is the third from the right.E) The blue jay is the third from the right.F) The robin is the third from the right.G) The raven is the third from the right.',
        "reasoning": "From the propositions, we know that Hummingbird is the forth from the left.However, there are seven objects, which means there are seven positions, which is the fourth from the left and the third from the right. So we know that Hummingbird is the third from the right.So we know the answer is D.",
        'ans': 'D',
    },
    {
        'context': 'The following paragraphs each describe a set of five objects arranged in a fixed order. The statements are logically consistent within each paragraph.\n\nIn a golf tournament, there were five golfers: Dan, Amy, Eve, Ana, and Mya. Dan finished above Eve. Dan finished below Mya. Amy finished third. Ana finished second-to-last.',
        'question': 'Which of the following is true? A) Dan finished last.B) Amy finished last.C) Eve finished last.D) Ana finished last.E) Mya finished last.',
        'premises': 'Dan finished above Eve. Dan finished below Mya. Amy finished third. Ana finished second-to-last.',
        'boundary_condition': 'In a golf tournament, there were five golfers: Dan, Amy, Eve, Ana, and Mya.',
        'propositions': 'Ana does not finish first. Amy does not finish first. Eve does not finish first. Dan does not finish first. Mya finish first.',
        'options': 'A) Dan finished last.B) Amy finished last.C) Eve finished last.D) Ana finished last.E) Mya finished last.',
        "reasoning": "From the propositions, we know that Amy finished third.Mya finished first.So there are three positions remained.And we know from premises that Dan finished above Eve and Dan finished below Mya. So we know that Dan is located in the mid of these three positions,he finished forth.Additionally, Dan finished above Eve, so Eve finished last. The anwser is C.",
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

gen_proposition_examples = [
    {'premises': 'The truck is older than the bus. The bus is older than the sedan.',
     'boundary_condition': 'In an antique car show, there are three vehicles: a bus, a sedan, and a truck.',
     'proposition': 'The truck is older than the sedan.',
     'topic': 'A set of three objects arranged in a fixed order.',
     'question': 'Which of the following is true? A) The bus is the newest.B) The sedan is the newest.C) The truck is the newest.',
     'explanation': 'According to "trucks are older than buses" and buses are older than cars, we know that buses rank second in the order of new to old.'},
    {'premises': 'If A is the second from the left. B is on the left of A.',
     'boundary_condition': 'In an AI show, there are three robots: A,B,C.',
     'proposition': 'B is the first from the left.',
     'topic': 'A set of three objects arranged in a fixed order.',
     'question': 'Which of the following is true? A) A is the first from the left.B) B is the first from the left.C)C is the first from the left.',
     'explanation': 'From left to right, we can count the position:first,second,third. A is in the second position.B is on the left of A.So B is in the first position.'},
    {'premises': 'Joe finished below Dan.Dan finished below Rob.',
     'boundary_condition': 'In a golf tournament, there were five golfers: Joe, Eve, Mya, Rob, and Dan.',
     'proposition': 'Joe finished below Rob.',
     'topic': 'A set of five objects arranged in a fixed order.',
     'question': 'Which of the following is true?A) Joe finished last.B) Eve finished last.C) Mya finished last.D) Rob finished last.E) Dan finished last.',
     'explanation': 'Joe finished below Dan.Dan finished below Rob.'},
    {'premises': 'Joe finished below Rob.Dan finished below Rob. Eve finished above Rob.Mya finished first.',
     'boundary_condition': 'In a golf tournament, there were five golfers: Joe, Eve, Mya, Rob, and Dan.',
     'proposition': 'Rob finished third.Eve finished second.',
     'topic': 'A set of five objects arranged in a fixed order.',
     'question': 'Which of the following is true?A) Joe finished last.B) Eve finished last.C) Mya finished last.D) Rob finished last.E) Dan finished last.',
     'explanation': 'There were two people who finished after Rob and one who finished before Rob, Mya finished first. So there are four positions left, so Rob is the third to finish.'},
    {
     'premises': 'The falcon is the third from the left. The crow is to the right of the hummingbird. The raven is the second from the left. The hawk is to the left of the hummingbird.The robin is the second from the right. The blue jay is to the first from the right.',
     'boundary_condition': 'On a branch, there are seven birds: a falcon, a crow, a hawk, a hummingbird, a blue jay, a robin, and a raven.',
     'proposition': 'Hummingbird is the forth from the left.',
     'topic': 'A set of seven objects arranged in a fixed order.',
     'question': 'Which of the following is true?A) The falcon is the third from the right.B) The crow is the third from the right.C) The hawk is the third from the right.D) The hummingbird is the third from the right.The blue jay is the third from the right.The robin is the third from the right.The raven is the third from the right',
     'explanation': 'From the following four premises:The falcon is the third from the left.The raven is the second from the left.The robin is the second from the right. The blue jay is to the first from the right.'},
]

# Premise Exploration 
gen_proposition = guidance(
'''
{{#system}}
Suppose you are one of the greatest AI scientists, logicians and mathematicians. Let us think step by step. 
Please use the "One-to-One Rules between Location and Object" to determine whether a given set of "premises" is a valid deduction of the "proposition," reply with True or False.
One-to-One Rules between Location and Object:
1. "Two premises": "If A is the second from the left. B is on the left of A." then "Proposition": "B is the first from the left."
2. "One premise": "B is the first from the left." then "Proposition": "No object is on the left of B."
3. "Two premises": "The loquats are more expensive than the kiwis. The kiwis are the second expensive." then "Proposition": "The loquats are the most expensive."
4. "Two premises": "If A is the second from the left. B is on the right of A." then "Proposition": "B is the third from the left."
4. "Three premises": "A is not the second from left. B is not the second from left. There are three people in total." then "Proposition": "C is the second from left."
Use One-to-One Rules between Location and Object to derive a "proposition" from at least two given "premises" that either directly gives a definite position for an object or gives a relative position between it and other objects.
Make sure that the "proposition" is not a repetition of the "premise" or merely a change of expression.
Make sure that your reasoning is derived directly from "premises" and "propositions" rather than introducing passive common sense and passive information through common sense reasoning.
Keep in mind that your derived "propositions" should be helpful in solving the "question" provided.
----{{/system}}

{{~#each examples}}
{{#user}}
---
"premises": "{{this.premises}}"
"boundary_condition": "{{this.boundary_condition}}"
We want to derive more propositions to solve the following question:
"question": "{{this.question}}"
Combined with boundary conditions, can you derive a new "proposition" from at least two given "premises"?
{{/user}}

{{#assistant}}"proposition": "{{this.proposition}}"{{/assistant}}
{{~/each}}

{{#user}}
---
"premises": "{{premises}}"
"boundary_condition": "{{boundary_condition}}"
We want to derive more propositions to solve the following question:
"question": "{{question}}"
Combined with boundary conditions, can you derive a new "proposition" from at least two given "premises"?
{{/user}}

{{#assistant}}"proposition": "{{/assistant}}
{{#assistant}}{{gen "proposition" temperature=temperature max_tokens=100 stop='\n'}}{{/assistant}}
''')

# Premise extraction
condition_extra_examples = [
    {
        'context': 'The following paragraphs each describe a set of seven objects arranged in a fixed order. The statements are logically consistent within each paragraph.\n\nOn a shelf, there are seven books: a green book, a brown book, a white book, a black book, an orange book, a purple book, and a yellow book. The purple book is to the left of the yellow book. The green book is to the left of the white book. The brown book is to the right of the yellow book. The white book is the fourth from the left. The green book is to the right of the orange book. The black book is the second from the left.',
        'topic': 'A set of 7 objects arranged in a fixed order.',
        'premise': 'The purple book is to the left of the yellow book. The green book is to the left of the white book. The brown book is to the right of the yellow book. The white book is the fourth from the left. The green book is to the right of the orange book. The black book is the second from the left.',
        'boundary_condition': 'The statements are logically consistent within each paragraph.\n\nOn a shelf, there are seven books: a green book, a brown book, a white book, a black book, an orange book, a purple book, and a yellow book.'
    },
    {
        'context': 'The following paragraphs each describe a set of five objects arranged in a fixed order. The statements are logically consistent within each paragraph.\n\nA fruit stand sells five fruits: watermelons, oranges, loquats, plums, and kiwis. The plums are less expensive than the kiwis. The plums are more expensive than the watermelons. The loquats are more expensive than the kiwis. The oranges are the most expensive.',
        'topic': 'A set of 5 objects arranged in a fixed order.',
        'premise': 'The plums are less expensive than the kiwis. The plums are more expensive than the watermelons. The loquats are more expensive than the kiwis. The oranges are the most expensive.',
        'boundary_condition': 'The statements are logically consistent within each paragraph.\n\nA fruit stand sells five fruits: watermelons, oranges, loquats, plums, and kiwis.'
    },
    {
        'context': 'The following paragraphs each describe a set of three objects arranged in a fixed order. The statements are logically consistent within each paragraph.\n\nOn a shelf, there are three books: a red book, a gray book, and a white book. The white book is to the left of the gray book. The red book is the second from the left.',
        'topic': 'A set of 3 objects arranged in a fixed order.',
        'premise': 'The white book is to the left of the gray book. The red book is the second from the left.',
        'boundary_condition': 'On a shelf, there are three books: a red book, a gray book, and a white book.'
    }
]
condition_transformation_examples = [
    {
        'premise': 'Ada finished third-to-last.',
        'premises': 'Amy finished third. Joe finished last. Mya finished above Dan. Eve finished fourth. Amy finished above Rob. Ada finished third-to-last.',
        'boundary_condition': 'In a golf tournament, there were seven golfers: Dan, Eve, Mya, Amy, Rob, Ada, and Joe.',
        'topic': 'A set of seven objects arranged in a fixed order.',
        'question': 'Which of the following is true?A) Dan finished second-to-last.B) Eve finished second-to-last.C) Mya finished second-to-last.D) Amy finished second-to-last.E) Rob finished second-to-last.F) Ada finished second-to-last.G) Joe finished second-to-last.',
        'judgement': 'True',
        'new_premise': 'Ada did not finish first. Ada did not finish second.'
    },
    {
        'premise': 'Eve finished fourth.',
        'premises': 'Amy finished third. Joe finished last. Mya finished above Dan. Eve finished fourth. Amy finished above Rob. Ada finished third-to-last.',
        'boundary_condition': 'In a golf tournament, there were seven golfers: Dan, Eve, Mya, Amy, Rob, Ada, and Joe.',
        'topic': 'A set of seven objects arranged in a fixed order.',
        'question': 'Which of the following is true?A) Dan finished second-to-last.B) Eve finished second-to-last.C) Mya finished second-to-last.D) Amy finished second-to-last.E) Rob finished second-to-last.F) Ada finished second-to-last.G) Joe finished second-to-last.',
        'judgement': 'True',
        'new_premise': 'Dan, Mya, Amy, Rob, Ada, and Joe did not finish fourth. Eve did not finish first,second,third,fifth,sixth or seventh.'
    },
    {
        'premise': 'Eve did not finish fourth.',
        'premises': 'Amy finished third. Joe finished last. Mya finished above Dan. Eve did not finish fourth. Amy finished above Rob. Ada finished third-to-last.',
        'boundary_condition': 'In a golf tournament, there were seven golfers: Dan, Eve, Mya, Amy, Rob, Ada, and Joe.',
        'topic': 'A set of seven objects arranged in a fixed order.',
        'question': 'Which of the following is true?A) Dan finished second-to-last.B) Eve finished second-to-last.C) Mya finished second-to-last.D) Amy finished second-to-last.E) Rob finished second-to-last.F) Ada finished second-to-last.G) Joe finished second-to-last.',
        'judgement': 'False',
        'new_premise': 'None.'
    },
    {
        'premise': 'Amy finished above Rob.',
        'premises': 'Amy finished third. Joe finished last. Mya finished above Dan. Eve did not finish fourth. Amy finished above Rob. Ada finished third-to-last.',
        'boundary_condition': 'In a golf tournament, there were seven golfers: Dan, Eve, Mya, Amy, Rob, Ada, and Joe.',
        'topic': 'A set of seven objects arranged in a fixed order.',
        'question': 'Which of the following is true?A) Dan finished second-to-last.B) Eve finished second-to-last.C) Mya finished second-to-last.D) Amy finished second-to-last.E) Rob finished second-to-last.F) Ada finished second-to-last.G) Joe finished second-to-last.',
        'judgement': 'True',
        'new_premise': 'Rob did not finish first.'
    },
{
        'premise': 'Amy is older than Rob.',
        'premises': 'Dan is newer than Eve.',
        'boundary_condition': 'In a golf tournament, there were seven golfers: Dan, Eve, Mya, Amy, Rob, Ada, and Joe.',
        'topic': 'A set of seven objects arranged in a fixed order.',
        'question': 'Which of the following is true?A) Dan finished second-to-last.B) Eve finished second-to-last.C) Mya finished second-to-last.D) Amy finished second-to-last.E) Rob finished second-to-last.F) Ada finished second-to-last.G) Joe finished second-to-last.',
        'judgement': 'True',
        'new_premise': 'Rob is not the oldest.'
    }
]
condition_transformation = guidance(
'''
{{#system}}
Suppose you are one of the greatest AI scientists, logicians, and mathematicians. Let's think about it step by step.
First, please read and analyze the "existing premises", read the definition of transformation;
Transformation: In the one-to-one relationship, when the value of the current variable is determined, it means that this variable can not take other values, and other variables can not take the current value, this reasoning process is transformation.
Check whether relying on a single "premise" and "boundary condition" can translate into other new premises? The new premises should not duplicate any of the existing premises.
If it can be transformed, give the new premises you have deduced; if it can't, answer "None."
Make sure that the new premises you get are helpful in solving the problem.
----{{/system}}
{{~#each examples}}
{{#user}}
---
"existing premises": "{{this.premises}}"
"question": "{{this.question}}"
"premise": "{{this.premise}}"
"boundary condition": "{{this.boundary_condition}}"
{{/user}}
{{#assistant}}Can you derive a new premise based on the premises and boundary condition that help solve the problem?{{/assistant}}
{{#assistant}}"new premise": "{{this.new_premise}}"{{/assistant}}
{{~/each}}

{{#user}}
---
"existing premises": "{{premises}}"
"question": "{{question}}"
"premise": "{{premise}}"
"boundary condition": "{{boundary_condition}}"
{{/user}}
{{#assistant}}Can you derive a new premise based on the premises and boundary condition that help solve the problem?{{/assistant}}
{{#assistant}}"new premise": "{{/assistant}}
{{#assistant}}{{gen "premise" temperature=temperature max_tokens=50 stop=['\\n\"']}}{{/assistant}}
'''
)
condition_extra = guidance(
'''
{{#system}}
Suppose you are one of the greatest AI scientists, logicians, and mathematicians. Let's think about it step by step.
First read and analyze the two sets of definitions defined below;
Premise: A constraint on the absolute position of an object or on the relative relationship between two objects.
Boundary condition: A description of the number of objects and the name of the object.
According to the above definition, summarize the core topics discussed in the following paragraphs and extract the premise and boundary conditions in the context.
----{{/system}}

{{~#each examples}}
{{#user}}
---
"context": "{{this.context}}"
{{/user}}
{{#assistant}}Can you summarize the core topics of the discussion from the context above?{{/assistant}}
{{#assistant}}"topic": "{{this.topic}}"{{/assistant}}
{{#assistant}}Can you extract the premise from the context above?{{/assistant}}
{{#assistant}}"premise": "{{this.premise}}"{{/assistant}}
{{#assistant}}Can you extract the boundary conditions from the context above?{{/assistant}}
{{#assistant}}"boundary condition": "{{this.boundary_condition}}"{{/assistant}}
{{~/each}}

{{#user}}
---
"context": "{{context}}"
{{/user}}

{{#assistant}}Can you summarize the core topics of the discussion from the context above?{{/assistant}}
{{#assistant}}"topic": "{{/assistant}}
{{#assistant}}{{gen "topic" temperature=temperature max_tokens=50 stop='\n'}}{{/assistant}}
{{#assistant}}Can you extract the premise from the context above?{{/assistant}}
{{#assistant}}"premise": "{{/assistant}}
{{#assistant}}{{gen "premise" temperature=temperature max_tokens=300 stop=['\\n\"']}}{{/assistant}}
{{#assistant}}Can you extract the boundary conditions from the context above?{{/assistant}}
{{#assistant}}"boundary condition": "{{/assistant}}
{{#assistant}}{{gen "boundary_condition" temperature=temperature max_tokens=300 stop=['\\n\"']}}{{/assistant}}
'''
)
# Verify whether a premise with right format is generated.
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



# Logical Validation 
validate_deduction = guidance(
'''
{{#system}}Suppose you are one of the greatest AI scientists, logicians and mathematicians. Let us think step by step. 
Please use basic orientation knowledge to determine whether a given set of "premises" and "boundary condition" to "propositions" is a correct deduction, reply with True or False.
Focus on checking whether the logic of the reasoning is correct and whether the proposition conflicts with the existing premise.
----{{/system}}
{{~#each examples}}
{{#user}}
---
"Premises": "{{this.premises}}"
"Boundary condition": "{{this.boundary_condition}}"
"Proposition": "{{this.proposition}}"
{{/user}}

{{#assistant}}"Judgement": "Is this deduction valid? {{this.validation}}"{{/assistant}}
{{~/each}}

{{#user}}
---
"Premises": "{{premises}}"
"Boundary condition": "{{boundary_condition}}"
"Proposition": "{{proposition}}"
{{/user}}

{{#assistant}}"Judgement": "Is this deduction valid? {{/assistant}}
{{#assistant}}{{select "validation" options=valid_validation}}{{/assistant}}
''')
# boundary validation 
boundary_deduction_examples = [
    {
        'premises': 'The peaches are the second-most expensive. The plums are the cheapest. The pears are more expensive than the kiwis.',
        'new_premise': 'The Kiwis are the most expensive.',
        'boundary_condition': 'A fruit stand sells seven fruits: kiwis, loquats, pears, peaches, mangoes, plums, and apples.',
        'judgement': 'True'
    },
    {
        'premises': 'The peaches are the second-most expensive. The plums are the cheapest. The pears are more expensive than the kiwis.',
        'new_premise': 'The Kiwis are the cheapest.',
        'boundary_condition': 'A fruit stand sells seven fruits: kiwis, loquats, pears, peaches, mangoes, plums, and apples.',
        'judgement': 'False'
    },
    {
        'premises': 'The peaches are the second-most expensive. The plums are the cheapest. The pears are more expensive than the kiwis.',
        'new_premise': 'The peaches, plums, or pears are the most expensive.',
        'boundary_condition': 'A fruit stand sells seven fruits: kiwis, loquats, pears, peaches, mangoes, plums, and apples.',
        'judgement': 'False'
    }

]
boundary_deduction = guidance(
'''
{{#system}}Suppose you are one of the greatest AI scientists, logicians, and mathematicians. Let's think about it step by step.
Answer "True" or "False" to determine whether the existing premises plus a new premise satisfies the boundary condition.
----{{/system}}

{{~#each examples}}
{{#user}}
---
"existing premises": "{{this.premises}}"
"new premise": "{{this.new_premise}}"
"boundary condition": "{{this.boundary_condition}}"
After adding the new premise to the existing premise, does it still meet the boundary conditions?
{{/user}}

{{#assistant}}"Judgement": "{{this.judgement}}"{{/assistant}}
{{~/each}}

{{#user}}
---
"existing premises": "{{premises}}"
"new premise": "{{proposition}}"
"boundary condition": "{{boundary_condition}}"
After adding the new premise to the existing premise, does it still meet the boundary conditions?
{{/user}}

{{#assistant}}"Judgement": "{{/assistant}}
{{#assistant}}{{select "judgement" options=valid_duplicated}}{{/assistant}}
'''
)
# Define the guidance program
sourced_deduction = guidance(
'''
{{#system}}Suppose you are one of the greatest AI scientists, logicians and mathematicians. Let us think step by step. 
Please determine whether the "Proposition" is directly deduced from the "Premises" and "Boundary condition" with certainty other than introducing unsourced information by common sense reasoning, reply with True or False.
----{{/system}}

{{~#each examples}}
{{#user}}
---
"Premises": "{{this.premises}}"
"Boundary condition": "{{this.boundary_condition}}"
"Proposition": "{{this.proposition}}"
{{/user}}

{{#assistant}}"Judgement": "Is this proposition directly deduced from the premises? {{this.sourced}}"{{/assistant}}
{{~/each}}

{{#user}}
---
"Premises": "{{premises}}"
"Boundary condition": "{{boundary_condition}}"
"Proposition": "{{proposition}}"
{{/user}}

{{#assistant}}"Judgement": "Is this proposition directly deduced from the premises? {{/assistant}}
{{#assistant}}{{select "sourced" options=valid_sourced}}{{/assistant}}
''')


# Define the guidance program
structure_program = guidance(
'''
{{#system}}Suppose you are one of the greatest AI scientists, logicians, and mathematicians. Let's think about it step by step.
First read and analyze the "paragraphs" and "questions", then use the "premises", "boundary conditions" and "propositions" to reason which of the options given is the answer to the "question".
Make sure that your reasoning is derived directly from "premises" and "propositions" rather than introducing passive common sense and passive information through common sense reasoning.
Please note that this is a single choice question.
If you can get the answer directly from the proposition, then you should choose the answer directly, otherwise keep reasoning with the proposition, premises, and boundary conditions until you arrive at a single answer.
----{{/system}}

{{~#each examples}}
{{#user}}
---
"context": "{{this.context}}"
"question and options": "{{this.question}}"
{{/user}}

{{#assistant}}"Premises": "Let's think step by step, and from the context we can extract these premises: {{this.premises}}"{{/assistant}}
{{#assistant}}"Boundary_condition": "Let's think step by step, and from the context we can extract these boundary conditions: {{this.boundary_condition}}"{{/assistant}}
{{#assistant}}"Thoughts": "Let us think step by step. From the premises, we can deduce propositions:{{this.propositions}}"{{/assistant}}
{{#assistant}}"Recall the questions and options":"{{this.question}}"{{/assistant}}
{{#assistant}}"Reasoning": "Let us think step by step, from the premises, boundary conditions and propositions,{{this.reasoning}}"{{/assistant}}
{{#assistant}}"Recall the questions and options":"{{this.question}}"{{/assistant}}
{{#assistant}}"Judgement": "Now we know that the answer to this question should be{{this.ans}}"{{/assistant}}
{{~/each}}

{{#user}}
---
"context": "{{context}}"
"question and options": "{{question}}"
{{/user}}
{{#assistant}}"Premises": "Let's think step by step, and from the context we can extract these premises: {{premises}}"{{/assistant}}
{{#assistant}}"Boundary_condition": "Let's think step by step, and from the context we can extract these boundary conditions: {{boundary_condition}}"{{/assistant}}
{{#assistant}}"Thoughts": "Let us think step by step. From the premises, we can deduce propositions:{{propositions}}"{{/assistant}}
{{#assistant}}"Recall the questions and options":"{{question}}"{{/assistant}}
{{#assistant}}"Reasoning": "Let us think step by step, from the premises, boundary conditions and propositions,{{/assistant}}
{{#assistant}}{{gen "reasoning" temperature=0.7 max_tokens=500 stop=['\\n\"']}}{{/assistant}}
{{#assistant}}"Recall the questions and options":"{{question}}"{{/assistant}}
{{#assistant}}"Judgement": "Now we know that the answer to this question should be{{/assistant}}
{{#assistant}}{{select "judgement" options=choose}}{{/assistant}}
''')


# Define the guidance program
structure_program_wocot = guidance(
'''
{{#system}}Suppose you are one of the greatest AI scientists, logicians, and mathematicians. Let's think about it step by step.
First read and analyze the "paragraphs" and "questions", then use the "premises", "boundary conditions" and "propositions" to reason which of the options given is the answer to the "question".
Make sure that your reasoning is derived directly from "premises" and "propositions" rather than introducing passive common sense and passive information through common sense reasoning.
Please note that this is a single choice question.
If you can get the answer directly from the proposition, then you should choose the answer directly, otherwise keep reasoning with the proposition, premises, and boundary conditions until you arrive at a single answer.
----{{/system}}

{{{~#each examples}}
{{#user}}
---
"context": "{{this.context}}"
"question and options": "{{this.question}}"
{{/user}}

{{#assistant}}"Premises": "Let's think step by step, and from the context we can extract these premises: {{this.premises}}"{{/assistant}}
{{#assistant}}"Boundary_condition": "Let's think step by step, and from the context we can extract these boundary conditions: {{this.boundary_condition}}"{{/assistant}}
{{#assistant}}"Thoughts": "Let us think step by step. From the premises, we can deduce propositions:{{this.propositions}}"{{/assistant}}
{{#assistant}}"Recall the questions and options":"{{this.question}}"{{/assistant}}
{{#assistant}}"Reasoning": "Let us think step by step, from the premises, boundary conditions and propositions,{{this.reasoning}}"{{/assistant}}
{{#assistant}}"Recall the questions and options":"{{this.question}}"{{/assistant}}
{{#assistant}}"Judgement": "Now we know that the answer to this question should be{{this.ans}}"{{/assistant}}
{{~/each}}

{{#user}}
---
"context": "{{context}}"
"questions and options": "{{question}}"
{{/user}}
{{#assistant}}"Premises": "Let's think step by step, and from the context we can extract these premises: {{premises}}"{{/assistant}}
{{#assistant}}"Boundary_condition": "Let's think step by step, and from the context we can extract these boundary conditions: {{boundary_condition}}"{{/assistant}}
{{#assistant}}"Thoughts": "Let us think step by step. From the premises, we can deduce propositions:{{propositions}}"{{/assistant}}
{{#assistant}}"Recall the questions and options":"{{question}}"{{/assistant}}
{{#assistant}}"Judgement": "Now we know that the answer to this question should be{{/assistant}}
{{#assistant}}{{select "judgement" options=choose}}{{/assistant}}
''')


# final-question with memory
structure_program_memory = guidance(
'''
{{#system}}Suppose you are one of the greatest AI scientists, logicians, and mathematicians. Let's think about it step by step.
First read and analyze the "paragraphs" and "questions", then use the "premises", "boundary conditions" and "propositions" to reason which of the options given is the answer to the "question".
Make sure that your reasoning is derived directly from "premises" and "propositions" rather than introducing passive common sense and passive information through common sense reasoning.
Please note that this is a single choice question.
If you can get the answer directly from the proposition, then you should choose the answer directly, otherwise keep reasoning with the proposition, premises, and boundary conditions until you arrive at a single answer.
----{{/system}}

{{~#each examples}}
{{#user}}
---
"context": "{{this.context}}"
"question and options": "{{this.question}}"
{{/user}}

{{#assistant}}"Premises": "Let's think step by step, and from the context we can extract these premises: {{this.premises}}"{{/assistant}}
{{#assistant}}"Boundary_condition": "Let's think step by step, and from the context we can extract these boundary conditions: {{this.boundary_condition}}"{{/assistant}}
{{#assistant}}"Thoughts": "Let us think step by step. From the premises, we can deduce propositions:{{this.propositions}}"{{/assistant}}
{{#assistant}}"Recall the questions and options":"{{this.question}}"{{/assistant}}
{{#assistant}}"Reasoning": "Using premises, boundary conditions, and continuing to reason according to the propositions already obtained,{{this.reasoning}}"{{/assistant}}
{{#assistant}}"Recall the questions and options":"{{this.question}}"{{/assistant}}
{{#assistant}}"Judgement": "Now we know that the answer to this question should be{{this.ans}}"{{/assistant}}
{{~/each}}

{{#user}}
---
"context": "{{context}}"
"question and options": "{{question}}"
{{/user}}
{{#assistant}}"Premises": "Let's think step by step, and from the context we can extract these premises: {{premises}}"{{/assistant}}
{{#assistant}}"Boundary_condition": "Let's think step by step, and from the context we can extract these boundary conditions: {{boundary_condition}}"{{/assistant}}
{{#assistant}}"Thoughts": "Let us think step by step. From the premises, we can deduce propositions:{{propositions}}"{{/assistant}}
{{#assistant}}"Recall the reasoning history":"{{infer_history}}"{{/assistant}}
{{#assistant}}"Recall the questions and options":"{{question}}"{{/assistant}}
{{#assistant}}"Reasoning": "Using premises, boundary conditions, and continuing to reason according to the propositions already obtained,{{/assistant}}
{{#assistant}}{{gen "reasoning" temperature=0.7 max_tokens=500 stop=['\\n\"']}}{{/assistant}}
{{#assistant}}"Recall the questions and options":"{{question}}"{{/assistant}}
{{#assistant}}"Judgement": "Now we know that the answer to this question should be{{/assistant}}
{{#assistant}}{{select "judgement" options=choose}}{{/assistant}}
''')
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
        'determinate_premise': 'The loquats are the fourth-most expensive.The apples are the second-cheapest.Peaches are not the cheapest. ',
        'indeterminate_premise': 'The loquats are less expensive than the kiwis.The peaches are more expensive than the kiwis.The peaches are less expensive than the oranges. The oranges are more expensive than the kiwis.',
        'boundary_condition': 'A fruit stand sells seven fruits: oranges, plums, loquats, apples, kiwis, cantaloupes, and peaches.',
        'count': 'loquats(2 times) apples(1 times) kiwis(3 times) peaches(3 times) oranges(2 times)',
        'topic': 'A set of 7 objects arranged in a fixed order.',
        'last_false_history': 'In the last round, we selected loquats as the standard. But we did not get a correct proposition.',
        'explanation': 'In the previous round, loquat was selected as the standard, but the correct proposition was not obtained, so loquat cannot be selected in this round. kiwis(3 times) peaches(3 times) are both 3 times, but peaches involves a certain premise, so Peaches should be selected as the standard.',
        'Most_relevant_premise': 'peaches',
        'Results': 'Peaches are not the cheapest. The peaches are more expensive than the kiwis. The peaches are less expensive than the oranges.'
    },
    {
        'determinate_premise': 'The crow is the rightmost. The crow is not the leftmost.',
        'indeterminate_premise': 'The raven is the first from the left.The blue jay is to the right of the owl.The hummingbird is to the right of the blue jay.The hawk is to the right of the hummingbird.',
        'boundary_condition': 'On a branch, there are seven birds: a blue jay, an owl, a falcon, a hawk, a raven, a crow, and a hummingbird.',
        'count': 'hummingbird(2 times) crow(2 times) raven(1 time) blue jay(2 times) owl(1 time) hawk(1 time)',
        'topic': 'A set of 7 objects arranged in a fixed order.',
        'last_false_history': 'In the last round, we select blue jay as the standard. But we did not get a correct proposition.',
        'explanation': 'The Crow has been mentioned the most, but his position has been determined, and we selected blue jay in the last round but got a wrong proposition.So we need to choose another variable that is mentioned the most. hummingbird\' position is not determined, So we can choose it as standard.',
        'Most_relevant_premise': 'hummingbird',
        'Results': 'The hummingbird is to the right of the blue jay.The hawk is to the right of the hummingbird.'
    },
]
condition_select_score_2 = guidance(
'''
{{#system}}Suppose you are one of the greatest artificial intelligence scientists, logicians, and mathematicians. Let's think about it step by step.
First read and analyze the "determinate premises" and "indeterminate premises", and then filter out several premises.
When you decide on a variable, read through the inference history first and don't choose a variable that has failed before as your choice for this round.
Please follow these steps:
1. Count the cumulative number of times each variable is mentioned by "determinate premises" and "indeterminate premises".
2. Determine the variable according to the number of mentions from high to low. If the number of mentions is the same, the variable with more prerequisites will be given priority.
3. Determine whether the value of the variable has been determined under the current variable. If it is determined, search and determine the next variable in order from most to least. If it has not been completely determined, go to step 4.
4. Use this variable as a criterion for screening "premises" and filter out all premises related to this variable.
----{{/system}}

{{~#each examples}}
{{#user}}
---
"determinate_premise": "{{this.determinate_premise}}"
"indeterminate_premise": "{{this.indeterminate_premise}}"
"topic": "{{this.topic}}"
"boundary_condition": {{this.boundary_condition}}
"Inference history": "{{this.last_false_history}}"
{{/user}}
{{#assistant}}Can you count the cumulative number of times each variable is mentioned by the premises?{{/assistant}}
{{#assistant}}"Count": "{{this.count}}"{{/assistant}}
{{#assistant}}Which variable should you choose as the criterion for premises screening?{{/assistant}}
{{#assistant}}"Explanation": "{{this.explanation}}"{{/assistant}}
{{#assistant}}What are all the premises related to this variable?{{/assistant}}
{{#assistant}}"Results": "{{this.Results}}"{{/assistant}}
{{~/each}}

{{#user}}
---
"determinate_premise": "{{determinate_premise}}"
"indeterminate_premise": "{{indeterminate_premise}}"
"topic": "{{topic}}"
"boundary_condition": "{{boundary_condition}}"
"Inference history": "{{last_false_history}}"
{{/user}}
{{#assistant}}Can you count the cumulative number of times each variable is mentioned by the premises?{{/assistant}}
{{#assistant}}"Count": "{{/assistant}}
{{#assistant}}{{gen "count" temperature=temperature max_tokens=200 stop='\n'}}{{/assistant}}
{{#assistant}}Which variable should you choose as the criterion for premises screening?{{/assistant}}
{{#assistant}}"Explanation": "{{/assistant}}
{{#assistant}}{{gen "explanation" temperature=temperature max_tokens=200 stop='\n'}}{{/assistant}}
{{#assistant}}What are all the premises related to this variable?{{/assistant}}
{{#assistant}}"Results": "{{/assistant}}
{{#assistant}}{{gen "results" temperature=temperature max_tokens=200 stop='\n'}}{{/assistant}}
'''
)
conditions_scores_examples_3 = [
    {
         'determinate_premise': 'Peony is on display in exhibition room 2. Peonies are not on display in Studio 4. Peonies are not on display in Studio 3. ',
         'indeterminate_premise': 'Tiger and rooster are not exhibited in the same exhibition room. Galloping horses and cranes should be displayed in the same exhibition room. Cranes or wintersweets are on display in Room 4. ',
         'boundary_condition': 'A painting can only be exhibited in one studio, and multiple paintings can be exhibited in one studio. ',
         'count': 'Peony (3 times) Crane (2 times) Exhibition Room 4 (2 times) Exhibition Room 3 (1 time) Exhibition Room 2 (1 time) Tiger (1 time) Rooster (1 time) Galloping horse (1 time) Wintersweet (1 time)',
         'topic': 'The exhibition of different paintings in different studios. ',
         'explanation': 'The most frequent peony is not selected as a screening criterion because a painting can only be exhibited in one studio. From the fact that the peony is displayed in the No. 2 exhibition room, it can be seen that the value of the peony has been determined,.So the second most relevant "crane" should be selected as standard. ',
         'Most_relevant_premise': 'Crane',
         'Results': 'The galloping horse and the crane should be displayed in the same exhibition room. Cranes or wintersweets are on display in Room 4. '
    },
    {
        'determinate_premise': 'The loquats are the fourth-most expensive.The apples are the second-cheapest.Peaches are not the cheapest. ',
        'indeterminate_premise': 'The loquats are less expensive than the kiwis.The peaches are more expensive than the kiwis.The peaches are less expensive than the oranges. The oranges are more expensive than the kiwis.',
        'boundary_condition': 'A fruit stand sells seven fruits: oranges, plums, loquats, apples, kiwis, cantaloupes, and peaches.',
        'count': 'loquats(2 times) apples(1 times) kiwis(3 times) peaches(3 times) oranges(2 times)',
        'topic': 'A set of 7 objects arranged in a fixed order.',
        'explanation': 'Kiwis(3 times) peaches(3 times) are both 3 times, but peaches involves a certain premise, so Peaches should be selected as the standard.',
        'Most_relevant_premise': 'peaches',
        'Results': 'Peaches are not the cheapest. The peaches are more expensive than the kiwis. The peaches are less expensive than the oranges.'
    },
    {
        'determinate_premise': 'The white book is the fourth from the left.The black book is the second from the left.',
        'indeterminate_premise': 'The green book is to the left of the white book. The brown book is to the right of the yellow book.The purple book is to the left of the yellow book.',
        'boundary_condition': 'On a shelf, there are seven books: a green book, a brown book, a white book, a black book, an orange book, a purple book, and a yellow book.',
        'count': 'white book(2 times) black book(1 time) green book(1 time) brown book(1 time) yellow book (2 times) purple book(1 time) ',
        'topic': 'A set of 7 objects arranged in a fixed order.',
        'explanation': 'The white book has been mentioned for 2 times, but it\' position is determined. So we have to choose yellow book as the standard.',
        'Most_relevant_premise': 'yellow book',
        'Results': 'The brown book is to the right of the yellow book.The purple book is to the left of the yellow book.'
    },
    {
        'determinate_premise': 'The crow is the rightmost. The crow is not the leftmost.',
        'indeterminate_premise': 'The raven is the first from the left.The blue jay is to the right of the owl.The hummingbird is to the right of the blue jay.The hawk is to the right of the hummingbird.',
        'boundary_condition': 'On a branch, there are seven birds: a blue jay, an owl, a falcon, a hawk, a raven, a crow, and a hummingbird.',
        'count': 'hummingbird(2 times) crow(2 time) raven(1 time) blue jay(2 time) owl(1 time) hawk(1 time)',
        'topic': 'A set of 7 objects arranged in a fixed order.',
        'explanation': 'The Crow has been mentioned the most, but his position has been determined, so we need to choose another variable that is mentioned the most. hummingbird\' position is not determined, So we can choose it as standard.',
        'Most_relevant_premise': 'hummingbird',
        'Results': 'The hummingbird is to the right of the blue jay.The hawk is to the right of the hummingbird.'
    },
]
# premise prioritization
condition_select_score_3 = guidance(
'''
{{#system}}Suppose you are one of the greatest artificial intelligence scientists, logicians, and mathematicians. Let's think about it step by step.
First read and analyze the "determinate premises" and "indeterminate premises", and then filter out several premises.
Please follow these steps:
1. Count the cumulative number of times each variable is mentioned by "determinate premises" and "indeterminate premises".
2. Determine the variable according to the number of mentions from high to low. If the number of mentions is the same, the variable with more prerequisites will be given priority.
3. Determine whether the value of the variable has been determined under the current variable. If it is determined, search and determine the next variable in order from most to least. If it has not been completely determined, go to step 4.
4. Use this variable as a criterion for screening "premises" and filter out all premises related to this variable.
----{{/system}}

{{~#each examples}}
{{#user}}
---
"determinate_premise": "{{this.determinate_premise}}"
"indeterminate_premise": "{{this.indeterminate_premise}}"
"topic": "{{this.topic}}"
"boundary_condition": "{{this.boundary_condition}}"
{{/user}}
{{#assistant}}Can you count the cumulative number of times each variable is mentioned by the premises?{{/assistant}}
{{#assistant}}"Count": "{{this.count}}"{{/assistant}}
{{#assistant}}Which variable should you choose as the criterion for premises screening?{{/assistant}}
{{#assistant}}"Explanation": "{{this.explanation}}"{{/assistant}}
{{#assistant}}What are all the premises related to this variable?{{/assistant}}
{{#assistant}}"Results": "{{this.Results}}"{{/assistant}}
{{~/each}}

{{#user}}
---
"determinate_premise": "{{determinate_premise}}"
"indeterminate_premise": "{{indeterminate_premise}}"
"topic": "{{topic}}"
"boundary_condition": "{{boundary_condition}}"
{{/user}}
{{#assistant}}Can you count the cumulative number of times each variable is mentioned by the premises?{{/assistant}}
{{#assistant}}"Count": "{{/assistant}}
{{#assistant}}{{gen "count" temperature=temperature max_tokens=200 stop='\n'}}{{/assistant}}
{{#assistant}}Which variable should you choose as the criterion for premises screening?{{/assistant}}
{{#assistant}}"Explanation": "{{/assistant}}
{{#assistant}}{{gen "explanation" temperature=temperature max_tokens=200 stop='\n'}}{{/assistant}}
{{#assistant}}What are all the premises related to this variable?{{/assistant}}
{{#assistant}}"Results": "{{/assistant}}
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
# Verify whether it is useful for the hypothesis.
useful_deduction_examples = [
    {'Premise': 'The red book is the second from the left.',
     'Explanation': 'This premise directly establishes the red book in the second position from left to right.',
     'usefulness': 'True'},
    {'Premise': 'The tractor is the second-newest.',
     'Explanation': 'This premise explains that tractors rank second in the new to old ranking.',
     'usefulness': 'True'},
    {'Premise': 'The tractor is the newer than car.',
    'Explanation': 'This premise provides the relative old and new relation between the two objects',
     'usefulness': 'False'},
    {'Premise': 'The red book is to the left of the purple book.',
     'Explanation': 'This premise provides the relative position relationship between the two books.',
     'usefulness': 'False'},
    {'Premise': ' Ana finished second-to-last.',
     'Explanation': 'Through this premise, we can only confirm the relative position range of Ana.',
     'usefulness': 'False'}
]
premise_divide_judgement = ["True", "False"]
# Define the guidance program
useful_deduction = guidance(
'''
{{#system}}Suppose you are one of the greatest AI scientists, logicians, and mathematicians. Let's think about it step by step.
First, read and analyze the following definition:
Determinate_premise: It directly describes an object's specific location or ranking, not its relative position to other objects.
Second, read and analyze the "Premise". Judge "Premise" is "determinate_premise" or not.
Third,please make sure your classification decisions are derived directly from definitions, rather than unsourced common sense.
----{{/system}}

{{~#each examples}}
{{#user}}
---
"Premise": "{{this.Premise}}"
{{/user}}
{{#assistant}}Is this "Premise" a "determinate_premise" or not?{{/assistant}}
{{#assistant}}"Explanation": "{{this.Explanation}}"{{/assistant}}
{{#assistant}}"Judgement": "{{this.usefulness}}" {{/assistant}}
{{~/each}}

{{#user}}
---
"Premise": "{{Premise}}"
{{/user}}
{{#assistant}}Is this "Premise" a "determinate_premise" or not?{{/assistant}}
{{#assistant}}"Explanation": "{{/assistant}}
{{#assistant}}{{gen "Explanation" temperature=temperature max_tokens=200 stop='\n'}}{{/assistant}}
{{#assistant}}"usefulness": "{{/assistant}}
{{#assistant}}{{select "usefulness" options=valid_validation}}{{/assistant}}
''')
