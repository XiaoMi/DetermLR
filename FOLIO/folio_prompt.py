import guidance
examples = [
    {'premises': 'Miroslav Venhoda was a Czech choral conductor who specialized in the performance of Renaissance and Baroque music. Any choral conductor is a musician. Some musicians love music. Miroslav Venhoda published a book in 1946 called Method of Studying Gregorian Chant.',
     'propositions': 'Miroslav Venhoda, who published a book in 1946 called Method of Studying Gregorian Chant, is a musician as he is a choral conductor.',
     'conclusion': 'A Czech person wrote a book in 1946.',
     'determine': 'Miroslav Venhoda was a Czech choral conductor who specialized in the performance of Renaissance and Baroque music. Miroslav Venhoda published a book in 1946 called Method of Studying Gregorian Chant. Miroslav Venhoda, who published a book in 1946 called Method of Studying Gregorian Chant, is a musician as he is a choral conductor.',
     'memory': 'In the NO:1 round,we use these "premises":"Miroslav Venhoda was a Czech choral conductor who specialized in the performance of Renaissance and Baroque music.  Miroslav Venhoda published a book in 1946 called Method of Studying Gregorian Chant." and got a "New Proposition": "Miroslav Venhoda, who published a book in 1946 called Method of Studying Gregorian Chant, is a musician as he is a choral conductor.',
     "reasoning": "Miroslav Venhoda, who is specified as a Czech choral conductor, published a book in 1946. Thus, it is true that a Czech person wrote a book in 1946.",
     'judgement': 'True'},
    {'premises': 'All eels are fish. No fish are plants. A thing is either a plant or animal. Nothing that breathes is paper. All animals breathe. If a sea eel is either an eel or a plant, then a sea eel is an eel or an animal.',
     'propositions': 'No eels are plants. All eels are animals.',
     'conclusion': 'Sea eel is an eel.',
     'determine': 'No eels are plants. All eels are animals.No eels are plants. All eels are animals.If a sea eel is either an eel or a plant, then a sea eel is an eel or an animal.',
     'memory': 'In the NO:1 round,we use these "premises":"All eels are fish. No fish are plants." and got a "New Proposition": "No eels are plants."\n In the NO:2 round,we use these "premises":"No eels are plants. A thing is either a plant or animal."and got a "New Proposition": "All eels are animals."',
     "reasoning": "all eels are fish and a sea eel is either an eel or a plant. It's also stated that no fish are plants. Therefore, a sea eel can't be a plant and must be an eel. However, there's no direct information about a sea eel being an eel.",
     'judgement': 'Unknown'},
    {'premises': 'Miroslav Venhoda was a Czech choral conductor who specialized in the performance of Renaissance and Baroque music. Any choral conductor is a musician. Some musicians love music. Miroslav Venhoda published a book in 1946 called Method of Studying Gregorian Chant.',
     'propositions': 'Miroslav Venhoda specialized in the performance of Renaissance and Baroque music,is a musician.',
     'conclusion': 'No choral conductor specialized in the performance of Renaissance.',
     'determine': 'Miroslav Venhoda specialized in the performance of Renaissance and Baroque music,is a musician.Any choral conductor is a musician.Miroslav Venhoda published a book in 1946 called Method of Studying Gregorian Chant.',
     'memory': 'In the NO:1 round,we use these "premises":"Miroslav Venhoda was a Czech choral conductor who specialized in the performance of Renaissance and Baroque music. Any choral conductor is a musician."and got a "New Proposition": "Miroslav Venhoda specialized in the performance of Renaissance and Baroque music."',
     "reasoning": "Miroslav Venhoda, a choral conductor, specialized in the performance of Renaissance and Baroque music. Thus, it is false to conclude that no choral conductor specialized in the performance of Renaissance.",
     'judgement': 'False'},
    {'premises': 'Anne is not furry. Anne is white. Bob is blue. Bob is cold. Bob is young. Erin is blue. Harry is not young. If someone is rough then they are cold. If someone is rough then they are white.If Harry is red, then Harry is cold. All white people are red. Red, rough people are young. If someone is blue then they are rough. If Anne is not red then Anne is young. Cold, young people are not furry.',
     'propositions': 'If Erin is young, then she is not furry.If Erin is cold and young, then she is not furry. If Erin is rough, then she is not furry.Erin is rough.If Erin is red and rough, then she is not furry.Erin is cold.',
     'conclusion': 'Erin is not furry.',
     'determine': 'Erin is cold.Erin is blue.Erin is rough.',
     'memory': '',
     "reasoning": "We know from the propositions that If Erin is rough, then she is not furry. And Erin is rough. So we know that Erin is not furry. So the Hypothesis is true.",
     'judgement': 'True'},
]

validate_deduction_examples = [
    {'premises': 'All eels are fish. No fish are plants.',
     'proposition': 'No eels are plants.',
     'validation': 'True'},
    {'premises': 'If bear is red,then the bear is rough. The bear is red.',
     'proposition': 'The bear is rough.',
     'validation': 'True'},
    {'premises': 'Nothing that breathes is paper. All animals breathe.',
     'proposition': 'All animals are paper.',
     'validation': 'False'},
    {'premises': 'A thing is either a plant or animal. All animals breathe.',
     'proposition': 'All things that breathe are animals.',
     'validation': 'True'},
    {'premises': 'Miroslav Venhoda was a Czech choral conductor who specialized in the performance of Renaissance and Baroque music. Any choral conductor is a musician.',
     'proposition': 'Miroslav Venhoda, being a Czech choral conductor specializing in Renaissance and Baroque music, is also a musician.',
     'validation': 'True'},
    {'premises': 'Any choral conductor is a musician. Some musicians love music.',
     'proposition': 'All choral conductor love music.',
     'validation': 'False'},
    {'premises': 'Any choral conductor is a musician. Miroslav Venhoda published a book in 1946 called Method of Studying Gregorian Chant.',
     'proposition': 'Miroslav Venhoda, who published a book in 1946 called Method of Studying Gregorian Chant, is a musician as he is a choral conductor.',
     'validation': 'True'}
]
# Verify whether the proposition comes from premises and not from other unknown sources of knowledge
sourced_deduction_examples = [
    {'premises': 'All eels are fish. No fish are plants.',
     'proposition': 'No eels are plants.',
     'sourced': 'True'},
     {
      'premises': 'Nothing that breathes is paper. All animals breathe.',
      'proposition': 'All animals need food.',
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

# Premise exploration
gen_proposition_examples = [
    {'premises': 'All eels are fish. No fish are plants. All animals breathe.',
     'proposition': 'No eels are plants.',
     'conclusion': 'Sea eel is an eel.',
     'explanation': 'This expression is deduced from the two premises as follows: if x is an eel, then it is a fish (from Premise 1), and if it is a fish, then it is not a plant (from Premise 2). Thus, if x is an eel, then it is not a plant.'},
    {'premises': 'All eels are fish. A thing is either a plant or animal. No fish are plants.',
     'proposition': 'All eels are animals.',
     'conclusion': 'Sea eel is an eel.',
     'explanation': 'This statement follows from the premises as follows: If x is an eel, then it is a fish (from Premise 1). If x is a thing (which includes being a fish, hence an eel), then it is either a plant or an animal (from Premise 2). Since it cannot be a plant (because it is a fish and no fish is a plant), it must be an animal. Thus, if x is an eel, it is an animal.'},
    {'premises': 'A thing is either a plant or animal. All animals breathe.',
     'proposition': 'All things that breathe are animals.',
     'conclusion': 'Sea eel is an eel.',
     'explanation': 'This statement is deduced from the premises as follows: If x is a thing, then it is either a plant or an animal (from Premise 1), and if x is an animal, then it breathes (from Premise 2). Therefore, if a thing breathes, it must be an animal, because it can not be a plant that breathes based on these premises.'},
    {
     'premises': 'If you keep statement A, you must keep statement B and statement C. If you keep statement D, you must delete both statement E and statement C.Statement A is important information and cannot be deleted.Statement E and statement F should be saved at the same time.',
     'proposition': 'You must keep statement B and statement C',
     'conclusion': 'D need to be kept',
     'explanation': 'This statement is deduced from the premises as follows:If you keep statement A, you must keep statement B and statement C. Statement A is important information and cannot be deleted.Therefore, if A is saved, then B and C are saved.'
    }
]
# Define the guidance program
gen_proposition = guidance(
'''
{{#system}}Suppose you are one of the greatest AI scientists, logicians and mathematicians. Let us think step by step. 
Please use Logical Reasoning Rules(LRR) to deduce a "Proposition" from two given "Premises" and the proposition does not include "if".
Logical Reasoning Rules(LRR):
1. "Two premises": "If A,then B. A is true." then "Proposition": "B is true."
2. "Two premises": "If A,then B. B is not true." then "Proposition": "A is not true"
3. "Two premises": "A is either C or D. A is not C." then "Proposition": "A is D."
Please make sure that the "Proposition" is logically correct.
Please make sure that the "Proposition" is not a duplicate of the "Premises".
Please make sure your reasoning is directly deduced from the "Premises" and "Propositions" other than introducing unsourced common knowledge and unsourced information by common sense reasoning.
Please remember that your "Proposition" should be useful to determine whether the "Hypothesis" is True, False or Unknown.
----{{/system}}

{{~#each examples}}
{{#user}}
---
"Premises": "{{this.premises}}"
We want to deduce more propositions to determine the correctness of the following "Hypothesis":
"Hypothesis": "{{this.conclusion}}"
Can you deduce a new "Proposition" from at least two given "Premises"?
{{/user}}

{{#assistant}}"Proposition": "{{this.proposition}}"{{/assistant}}
{{~/each}}

{{#user}}
---
"Premises": "{{premises}}"
We want to deduce more propositions to determine the correctness of the following "Hypothesis":
"Hypothesis": "{{conclusion}}"
Can you deduce a new "Proposition" from at least two given "Premises"?
{{/user}}

{{#assistant}}"Proposition": "{{/assistant}}
{{#assistant}}{{gen "proposition" temperature=temperature max_tokens=50 stop='\n'}}{{/assistant}}
''')


# Determining whether generates a new proposition with right format.
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
{{#system}}Suppose you are one of the greatest AI scientists, logicians and mathematicians. Let us think step by step. 
Please use the Logical Reasoning Rules(LRR) to determine whether the deduction of the given "Premises" to a "Proposition" is valid or not, reply with True or False.
Logical Reasoning Rules(LRR):
1. "Two premises": "If A,then B. A is true." then "Proposition": "B is true."
2. "Two premises": "If A,then B. If B,then C." then "Proposition": "If A, then C."
3. "Two premises": "If A,then B. B is not true." then "Proposition": "A is not true"
4. "Two premises": "A is either C or D. A is not C." then "Proposition": "A is D."
----{{/system}}
{{~#each examples}}
{{#user}}
---
"Premises": "{{this.premises}}"
"Proposition": "{{this.proposition}}"
{{/user}}

{{#assistant}}"Judgement": "Is this deduction valid? {{this.validation}}"{{/assistant}}
{{~/each}}

{{#user}}
---
"Premises": "{{premises}}"
"Proposition": "{{proposition}}"
{{/user}}

{{#assistant}}"Judgement": "Is this deduction valid? {{/assistant}}
{{#assistant}}{{select "validation" options=valid_validation}}{{/assistant}}
''')

# Verify the repeatability of logical reasoning result.
duplicated_deduction_examples = [
    {'premises': 'Miroslav Venhoda was a Czech choral conductor who specialized in the performance of Renaissance and Baroque music. Any choral conductor is a musician. Some musicians love music. Miroslav Venhoda published a book in 1946 called Method of Studying Gregorian Chant.',
     'proposition': 'If someone is a choral conductor, then he is a musician.',
     'duplicated': 'True',
     'explanation': '"If someone is a choral conductor, then he is a musician." can be derived only using "Any choral conductor is a musician". So the answer is true.'
     },
    {'premises': 'All eels are fish. No fish are plants. A thing is either a plant or animal. Nothing that breathes is paper. All animals breathe. If a sea eel is either an eel or a plant, then a sea eel is an eel or an animal.',
     'proposition': 'No eels are plants.',
     'duplicated': 'False',
     'explanation': '"No eels are plants." can be derived using "All eels are fish." and "No fish are plants." So the answer is false.'
     }
]
# Define the guidance program
duplicated_deduction = guidance(
'''
{{#system}}Suppose you are one of the greatest AI scientists, logicians and mathematicians. Let us think step by step. 
Can this "proposition" can be derived using only one "premise"?Please reply with True or False.
----{{/system}}

{{~#each examples}}
{{#user}}
---
"Premises": "{{this.premises}}"
"Proposition": "{{this.proposition}}"
Can this "proposition" can be derived using only one "premise"?
{{/user}}

{{#assistant}}"Judgement": "{{this.duplicated}}"{{/assistant}}
{{#assistant}}"explanation": "this.explanation"{{/assistant}}
{{~/each}}

{{#user}}
---
"Premises": "{{premises}}"
"Proposition": "{{proposition}}"
Can this "proposition" can be derived using only one "premise"?
{{/user}}

{{#assistant}}"Judgement": " {{/assistant}}
{{#assistant}}{{select "duplicated" options=valid_duplicated}}{{/assistant}}
''')


# Define the guidance program
sourced_deduction = guidance(
'''
{{#system}}Suppose you are one of the greatest AI scientists, logicians and mathematicians. Let us think step by step. 
Please determine whether the "Proposition" is directly deduced from the "Premises" with certainty other than introducing unsourced information by common sense reasoning, reply with True or False.
----{{/system}}

{{~#each examples}}
{{#user}}
---
"Premises": "{{this.premises}}"
"Proposition": "{{this.proposition}}"
{{/user}}

{{#assistant}}"Judgement": "Is this proposition directly deduced from the premises? {{this.sourced}}"{{/assistant}}
{{~/each}}

{{#user}}
---
"Premises": "{{premises}}"
"Proposition": "{{proposition}}"
{{/user}}

{{#assistant}}"Judgement": "Is this proposition directly deduced from the premises? {{/assistant}}
{{#assistant}}{{select "sourced" options=valid_sourced}}{{/assistant}}
''')


# Define the guidance program
structure_program = guidance(
'''
{{#system}}Suppose you are one of the greatest AI scientists, logicians and mathematicians. Let us think step by step. 
Read and analyze the "Premises" first, then judge whether the "Hypothesis" is True, False or Unknown.
Please make sure your reasoning is directly deduced from the "Premises" and "Propositions" other than introducing unsourced common knowledge and unsourced information by common sense reasoning.
----{{/system}}

{{~#each examples}}
{{#user}}
---
"Premises": "{{this.premises}}"
"Hypothesis": "{{this.conclusion}}"
{{/user}}

{{#assistant}}"Thoughts": "Let us think step by step. From the premises, we can deduce propositions: {{this.propositions}}"{{/assistant}}
{{#assistant}}"Reasoning": "Let us think step by step, {{this.reasoning}}"{{/assistant}}
{{#assistant}}"Recall the Hypothesis": "{{this.conclusion}}"{{/assistant}}
{{#assistant}}"Judgement": "Now we know that the Hypothesis is {{this.judgement}}{{/assistant}}
{{~/each}}

{{#user}}
---
"Premises": "{{premises}}"
"Hypothesis": "{{conclusion}}"
{{/user}}

{{#assistant}}"Thoughts": "Let us think step by step. From the premises, we can deduce propositions: {{propositions}}"{{/assistant}}
{{#assistant}}"Recall the Hypothesis": "{{conclusion}}"{{/assistant}}
{{#assistant}}"Reasoning": "Let us think step by step,{{/assistant}}
{{#assistant}}{{gen "reasoning" temperature=0.7 max_tokens=300 stop=['\\n\"']}}{{/assistant}}
{{#assistant}}"Recall the Hypothesis": "{{conclusion}}"{{/assistant}}
{{#assistant}}"Judgement": "Now we know that the Hypothesis is {{/assistant}}
{{#assistant}}{{select "judgement" options=valid_judgement}}{{/assistant}}
''')


# Define the guidance program
structure_program_wocot = guidance(
'''
{{#system}}Suppose you are one of the greatest AI scientists, logicians and mathematicians. Let us think step by step. 
Read and analyze the "Premises" first, then judge whether the "Hypothesis" is True, False or Unknown.
Please make sure your reasoning is directly deduced from the "Premises" and "Propositions" other than introducing unsourced common knowledge and unsourced information by common sense reasoning.
----{{/system}}

{{~#each examples}}
{{#user}}
---
"Premises": "{{this.premises}}"
"Hypothesis": "{{this.conclusion}}"
{{/user}}

{{#assistant}}"Thoughts": "Let us think step by step. From the premises, we can deduce propositions: {{this.propositions}}"{{/assistant}}
{{#assistant}}If there are propositions that directly determine whether the hypothesis is true or false, you do not need to analyze the premises again; otherwise, you should reason with both propositions and premises.{{/assistant}}
{{#assistant}}"Reasoning": "Let us think step by step, {{this.reasoning}}"{{/assistant}}
{{#assistant}}"Recall the Hypothesis": "{{this.conclusion}}"{{/assistant}}
{{#assistant}}"Judgement": "Now we know that the Hypothesis is {{this.judgement}}{{/assistant}}
{{~/each}}

{{#user}}
---
"Premises": "{{premises}}"
"Hypothesis": "{{conclusion}}"
{{/user}}

{{#assistant}}"Thoughts": "Let us think step by step. From the premises, we can deduce propositions: {{propositions}}"{{/assistant}}
{{#assistant}}If there are propositions that directly determine whether the hypothesis is true or false, you do not need to analyze the premises again; otherwise, you should reason with both propositions and premises.{{/assistant}}
{{#assistant}}"Recall the Hypothesis": "{{conclusion}}"{{/assistant}}
{{#assistant}}"Judgement": "Now we know that the Hypothesis is {{/assistant}}
{{#assistant}}{{select "judgement" options=valid_judgement}}{{/assistant}}
''')
# Define the guidance program
structure_program_memory = guidance(
'''
{{#system}}Suppose you are one of the greatest AI scientists, logicians and mathematicians. Let us think step by step. 
Read and analyze the "Premises" first, then use "Propositions" to reasoning whether the "Hypothesis" is True, False or Unknown.
Please make sure your reasoning is directly deduced from the "Premises" and "Propositions" other than introducing unsourced common knowledge and unsourced information by common sense reasoning.
If there are propositions that directly determine whether the hypothesis is true or false, you do not need to analyze the premises; otherwise, you should reason with both propositions and premises.
----{{/system}}

{{~#each examples}}
{{#user}}
---
"Premises": "{{this.premises}}"
"Hypothesis": "{{this.conclusion}}"
{{/user}}

{{#assistant}}"Thoughts": "Let us think step by step. From the premises, we can deduce propositions: {{this.propositions}}"{{/assistant}}
{{#assistant}}If there are propositions that directly determine whether the hypothesis is true or false, you do not need to analyze the premises again; otherwise, you should reason with both propositions and premises.{{/assistant}}
{{#assistant}}"Reasoning": "Let us think step by step, from the premises and propositions,{{this.reasoning}}"{{/assistant}}
{{#assistant}}"Recall the Hypothesis": "{{this.conclusion}}"{{/assistant}}
{{#assistant}}"Judgement": "Now we know that the Hypothesis is {{this.judgement}}{{/assistant}}
{{~/each}}

{{#user}}
---
"Premises": "{{premises}}"
"Hypothesis": "{{conclusion}}"
{{/user}}

{{#assistant}}"Thoughts": "Let us think step by step. From the premises, we can deduce propositions: {{propositions}}"{{/assistant}}
{{#assistant}}"Recall the Propositions Deduction history": "{{infer_history}}"{{/assistant}}
{{#assistant}}If there are propositions that directly determine whether the hypothesis is true or false, you do not need to analyze the premises again; otherwise, you should reason with both propositions and premises.{{/assistant}}
{{#assistant}}"Recall the Hypothesis": "{{conclusion}}"{{/assistant}}
{{#assistant}}"Reasoning": "Let us think step by step, from the premises and propositions,{{/assistant}}
{{#assistant}}{{gen "reasoning" temperature=0.7 max_tokens=300 stop=['\\n\"']}}{{/assistant}}
{{#assistant}}"Recall the Hypothesis": "{{conclusion}}"{{/assistant}}
{{#assistant}}"Judgement": "Now we know that the Hypothesis is {{/assistant}}
{{#assistant}}{{select "judgement" options=valid_judgement}}{{/assistant}}
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
conditions_scores_examples_3 = [
    {
        'determinate_premise': 'C need to be kept.',
        'indeterminate_premise': 'If C need to be kept,then E need to be delete. If you keep statement A, you must keep statement B and statement C. If you keep statement D, you must delete both statement E and statement C.Statement A is important information and cannot be deleted.Statement E and statement F should be saved at the same time.',
        'Hypothesis': 'D and C need to be kept',
        'New_proposition': 'C need to be kept.',
        'last_history': 'In the last round, we use this "most relevant premise": "If you keep statement A, you must keep statement B and statement C."and got a "New Proposition": If you keep statement D, you must delete both statement E and statement C.',
        'explanation': 'We choose the "New_proposition" as the answer of "Most_relevant_premise" which is "C need to be kept."',
        'Most_relevant_premise': 'C need to be kept.(1)',
        'Other_premises_scores': 'If C need to be kept,then E need to be delete.(0.5) If you keep statement A, you must keep statement B and statement C.(0.25)  If you keep statement D, you must delete both statement E and statement C.(0.25) Statement A is important information and cannot be deleted.(0.0) Statement E and statement F should be saved at the same time.(0.0)',
        'Results': 'If C need to be kept,then E need to be delete.C need to be kept.'
    },
    {
        'determinate_premise': 'The bear is big. Billy is big.',
        'indeterminate_premise': 'The tiger is rough. If bear is big, then bear is red. If someone is big, then they are nice.',
        'New_proposition': 'The bear is big.',
        'Hypothesis': 'bear is rough.',
        'Most_relevant_premise': 'The bear is big.(1)',
        'Other_premises_scores': 'If bear is big, then bear is red.(0.8)The tiger is rough.(0.0) If someone is big, then they are nice.(0.55)',
        'Results': 'The bear is big.If someone is big, then they are nice.If bear is big, then bear is red.',
        'explanation': 'The scores of "If bear is big, then bear is red." is 0.8, because they have the same noun and adjective(0.55), and "The bear is big." is the premise of "If bear is big, then bear is red."(0.25) so the score is 0.8.'
    }
]
conditions_scores_examples_2 =[
    {
        'determinate_premise': 'The bear is big. Billy is rough.The tiger is rough.',
        'indeterminate_premise': ' If bear is big, then bear is red. If someone is big, then they are nice.',
        'New_proposition': 'The bear is big.',
        'Hypothesis': 'bear is rough.',
        'Last_Most_relevant_premise': 'Billy is rough.',
        'Most_relevant_premise': 'The bear is big.(0.25)',
        'Other_premises_scores': 'If bear is big, then bear is red.(0.8)The tiger is rough.(0.0) If someone is big, then they are nice.(0.55)Billy is rough.(0.25)',
        'Results': 'The bear is big.If someone is big, then they are nice.If bear is big, then bear is red.',
        'explanation': 'The scores of "If bear is big, then bear is red." is 0.8, because they have the same noun and adjective(0.55), and "The bear is big." is the premise of "If bear is big, then bear is red."(0.25) so the score is 0.8.'
    },
]
# Premise Prioritization
condition_select_score_2 = guidance(
'''
{{#system}}Suppose you are one of the greatest AI scientists, logicians and mathematicians. Let us think step by step.
Read and analyze the "determinate_premise" and "indeterminate_premise" first, then selecting several premises from them. 
Read the "Last_Most_relevant_premise", when you select "Most_relevant_premise",do not choose "Last_Most_relevant_premise" as your answer.
Please follow these steps:
1.From the determinate_premise, select the "Most relevant premise" with the highest correlation with the "Hypothesis", you need to follow this premise with a score from 0 to 1.Unless determinate_premise is empty then you can select from indeterminate_premise.
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
"Last_Most_relevant_premise": "{{this.Last_Most_relevant_premise}}"
{{/user}}
{{#assistant}}Can you select the premise from the "determinate_premises" that scores the highest score for Relevance scoring rules to the "hypothesis"?{{/assistant}}
{{#assistant}}"Most_relevant_premise": "{{this.Most_relevant_premise}}"{{/assistant}}
{{#assistant}}Can you assess how the "Most relevant premise" relates to all the other "determinate_premise" and "indeterminate_premise" accoding to Relevance scoring rules?{{/assistant}}
{{#assistant}}"Other_premises_scores": "{{this.Other_premises_scores}}"{{/assistant}}
{{#assistant}}"Results": "{{this.Results}}"{{/assistant}}
{{#assistant}}"explanation": "{{this.explanation}}"{{/assistant}}
{{~/each}}

{{#user}}
---
"determinate_premise": "{{determinate_premise}}"
"indeterminate_premise": "{{indeterminate_premise}}"
"Hypothesis": "{{Hypothesis}}"
"Last_Most_relevant_premise": "{{Last_Most_relevant_premise}}"
{{/user}}
{{#assistant}}Can you select the premise from the "determinate_premises" that scores the highest score for Relevance scoring rules to the "hypothesis"?{{/assistant}}
{{#assistant}}"Most_relevant_premise": "{{/assistant}}
{{#assistant}}{{gen "Most_relevant_premise" temperature=temperature max_tokens=200 stop='\n'}}{{/assistant}}
{{#assistant}}Can you assess how the "Most relevant premise" relates to all the other "determinate_premise" and "indeterminate_premise" accoding to Relevance scoring rules?{{/assistant}}
{{#assistant}}"Other_premises_scores": "{{/assistant}}
{{#assistant}}{{gen "Other_premises_scores" temperature=temperature max_tokens=200 stop='\n'}}{{/assistant}}
{{#assistant}}"Results": "{{/assistant}}
{{#assistant}}{{gen "results" temperature=temperature max_tokens=200 stop='\n'}}{{/assistant}}
'''
)
# Premise Prioritization
condition_select_score_3 = guidance(
'''
{{#system}}Suppose you are one of the greatest AI scientists, logicians and mathematicians. Let us think step by step. 
Read and analyze the "determinate_premise" and "indeterminate_premise" first, then selecting several premises from them. 
When you select "Most_relevant_premise", please choose the "New_proposition" as the answer.
Please follow these steps:
1.Please choose the "New_proposition" as the answer of "Most_relevant_premise" and with score 1.
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
"New_proposition": {{this.New_proposition}}
{{/user}}
{{#assistant}}When you select "Most_relevant_premise", please choose the "New_proposition" as your answer with a score 1.{{/assistant}}
{{#assistant}}"Most_relevant_premise": "{{this.Most_relevant_premise}}"{{/assistant}}
{{#assistant}}Can you assess how the "Most relevant premise" relates to all the other "determinate_premise" and "indeterminate_premise" accoding to Relevance scoring rules?{{/assistant}}
{{#assistant}}"Other_premises_scores": "{{this.Other_premises_scores}}"{{/assistant}}
{{#assistant}}"Results": "{{this.Results}}"{{/assistant}}
{{#assistant}}"explanation": "{{this.explanation}}"{{/assistant}}
{{~/each}}

{{#user}}
---
"determinate_premise": "{{determinate_premise}}"
"indeterminate_premise": "{{indeterminate_premise}}"
"Hypothesis": "{{Hypothesis}}"
"New_proposition": {{New_proposition}}
{{/user}}
{{#assistant}}When you select "Most_relevant_premise", please choose the "New_proposition" as your answer with a score 1.{{/assistant}}
{{#assistant}}"Most_relevant_premise": "{{New_proposition}}"{{/assistant}}
{{#assistant}}Can you assess how the "Most relevant premise" relates to all the other "determinate_premise" and "indeterminate_premise" accoding to Relevance scoring rules?{{/assistant}}
{{#assistant}}"Other_premises_scores": "{{/assistant}}
{{#assistant}}{{gen "Other_premises_scores" temperature=temperature max_tokens=200 stop='\n'}}{{/assistant}}
{{#assistant}}"Results": "{{/assistant}}
{{#assistant}}{{gen "results" temperature=temperature max_tokens=200 stop='\n'}}{{/assistant}}
'''
)
# Premise Prioritization
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
{{#assistant}}{{gen "Other_premises_scores" temperature=temperature max_tokens=200 stop='\n'}}{{/assistant}}
{{#assistant}}"Results": "{{/assistant}}
{{#assistant}}{{gen "results" temperature=temperature max_tokens=200 stop='\n'}}{{/assistant}}
'''
)
# Check whether it is helpful for hypothesis.
useful_deduction_examples = [
    {'Premise': 'Miroslav Venhoda, who published a book in 1946 called Method of Studying Gregorian Chant, is a musician as he is a choral conductor.',
     'Hypothesis': 'A Czech person wrote a book in 1946.',
    'Explanation': 'This premise and Hypothesis contain the same noun(book and 1946), and it is not in the structure of "if..." or "if...then...".',
     'usefulness': 'True'},
    {'Premise': 'All rabbits are cute.',
     'Hypothesis': 'Rock is a turtle or cute.',
    'Explanation': 'This premise and Hypothesis contain the same adjective(cute), and it is not in the structure of "if..." or "if...then...".',
     'usefulness': 'True'},
    {'Premise': 'No animals are paper.',
     'Hypothesis': 'Sea eel is an eel.',
    'Explanation': 'This premise is not in the structure of "if..." or "if...then...",but it has no same noun or adjective with Hypothesis.',
     'usefulness': 'False'},
    {'Premise': 'If no animals are paper, then there is no paper.',
     'Hypothesis': 'Sea eel is an eel.',
    'Explanation': 'This premise has no same noun or adjective with Hypothesis, and it is in the structure of "if...then...".',
     'usefulness': 'False'},
    {'Premise': 'If sea eel is an animal,it is an eel.',
     'Hypothesis': 'Sea eel is an eel.',
    'Explanation': 'This premise has the same noun(sea eel) with Hypothesis, but it is in the structure of "if...".',
     'usefulness': 'False'}
]
premise_divide_judgement = ["True", "False"]
useful_deduction = guidance(
'''
{{#system}}Suppose you are one of the greatest AI scientists, logicians and mathematicians. Let us think step by step. 
First, read and analyze the following definition:
Determinate_premise: The premise contains the same noun or adjective as the Hypothesis,and the premise is not in the structure of "if..." or "if...then...".
Second, read and analyze the "Premise" and "Hypothesis" .Judge "Premise" is "determinate_premise" or not.
Third,please make sure your classification decisions are derived directly from definitions, rather than unsourced common sense.
----{{/system}}

{{~#each examples}}
{{#user}}
---
"Premise": "{{this.Premise}}"
"Hypothesis": "{{this.Hypothesis}}"
{{/user}}
{{#assistant}}"Explanation": "{{this.Explanation}}"{{/assistant}}
{{#assistant}}"Judgement": "Is this "Premise" a "determinate_premise" or not?{{this.usefulness}}" {{/assistant}}
{{~/each}}

{{#user}}
---
"Premise": "{{Premise}}"
"Hypothesis": "{{conclusion}}"
{{/user}}
{{#assistant}}"Explanation": "{{/assistant}}
{{#assistant}}{{gen "Explanation" temperature=temperature max_tokens=200 stop='\n'}}{{/assistant}}
{{#assistant}}"Judgement": "Is this "Premise" a "determinate_premise" or not?{{/assistant}}
{{#assistant}}{{select "usefulness" options=valid_validation}}{{/assistant}}
''')
# Premise Identification
premise_classification_examples = [
    {'Premises': 'If people perform in school talent shows often, then they attend and are very engaged with school events. All people who are inactive and disinterested members of their community chaperone high school dances.  Bonnie either both attends and is very engaged with school events and is a student who attends the school, or she neither attends and is very engaged with school events nor is a student who attends the school.',
     'Hypothesis': 'Bonnie performs in school talent shows often.',
    'determinate_premise': 'If people perform in school talent shows often, then they attend and are very engaged with school events. Bonnie either both attends and is very engaged with school events and is a student who attends the school, or she neither attends and is very engaged with school events nor is a student who attends the school.',
    'indeterminate_premise': 'All people who are inactive and disinterested members of their community chaperone high school dances.',
    'Explanation': 'If people perform in school talent shows often, then they attend and are very engaged with school events.(intersection:school talent shows) Bonnie either both attends and is very engaged with school events and is a student who attends the school, or she neither attends and is very engaged with school events nor is a student who attends the school.(intersection:Bonnie)All people who are inactive and disinterested members of their community chaperone high school dances.(No intersection)'},
    {'Premises': 'No animals are paper. Sea eel is an animal.Paper is not an animal.',
     'Hypothesis': 'Sea eel is an eel.',
    'determinate_premise': 'Sea eel is an animal.',
    'indeterminate_premise': 'No animals are paper. Paper is not an animal.',
    'Explanation': 'Sea eel is an animal.(intersection:Sea eel) No animals are paper.(No intersection) Paper is not an animal.(No intersection)'}
]
premise_classification = guidance(
'''
{{#system}}Suppose you are one of the greatest AI scientists, logicians and mathematicians. Let us think step by step. 
Read and analyze the "Premises" and "Hypothesis" first.Please divide "Premises" into "determinate_premise" and "indeterminate_premise".
If the object discussed by "Premises" and "Hypothesis "has an intersection, then the Premise should be considered as "determinate_premise", otherwise it is "indeterminate_premise".
Please divide "Premises" into "determinate_premise" and "indeterminate_premise" according to "Hypothesis".
----{{/system}}

{{~#each examples}}
{{#user}}
---
"Premises": "{{this.Premises}}"
"Hypothesis": "{{this.Hypothesis}}"
{{/user}}
{{#assistant}}Can you divide "Premises" into "determinate_premise" and "indeterminate_premise" according to "Hypothesis"?{{/assistant}}
{{#assistant}}"determinate_premise": "{{this.determinate_premise}}"{{/assistant}}
{{#assistant}}"indeterminate_premise": "{{this.indeterminate_premise}}"{{/assistant}}
{{~/each}}

{{#user}}
---
"Premises": "{{Premises}}"
"Hypothesis": "{{Hypothesis}}"
{{/user}}

{{#assistant}}Can you divide "Premises" into "determinate_premise" and "indeterminate_premise" according to "Hypothesis"?{{/assistant}}
{{#assistant}}"determinate_premise": "{{/assistant}}
{{#assistant}}{{gen "determinate_premise" temperature=0.7 max_tokens=200 stop='\n'}}{{/assistant}}
{{#assistant}}"indeterminate_premise": "{{/assistant}}
{{#assistant}}{{gen "indeterminate_premise" temperature=0.7 max_tokens=200 stop='\n'}}{{/assistant}}
''')
