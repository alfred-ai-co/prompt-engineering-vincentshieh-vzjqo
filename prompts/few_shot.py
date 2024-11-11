FEW_SHOT_PROMPT = """
Given the following topic {input}, generate a quiz with a random number of questions between 1 to 5.

The output should be a JSON object with a list of questions under the "questions" key.
Each question object in the list should include the "question" key, the "choices" key, and the "answer" key.
The "question" should be a string.
The "choices" should be a list of objects with "key" and "value" fields, with each "key" being a letter of the alphabet in alphabetical order and each "value" being a string.
The "answer" should be the letter of the alphabet corresponding to the correct choice.

Here is an example of a quiz:
1.
Question: What is the square root of 16?
Answer: 4

2.
Question: What is the sum of the angles in a triangle?
Answer: 180 degrees

Here is another example of a quiz:
1.
Question: What is the sum of 10 and 5?
Answer: 15

2.
Question: What is the product of 7 and 4?
Answer: 28
"""
