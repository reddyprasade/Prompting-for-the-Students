"""
=============================================================
Prompting Technique 3: Chain-of-Thought (CoT) Prompting
=============================================================

WHAT IS IT?
-----------
Chain-of-Thought (CoT) prompting encourages the LLM to reason
step-by-step before giving a final answer. Instead of jumping
to a conclusion, the model "thinks out loud" through intermediate
reasoning steps.

VARIANTS:
---------
1. Zero-Shot CoT: Add "Let's think step by step." to the prompt.
2. Few-Shot CoT:  Provide examples that include reasoning steps.

WHEN TO USE IT?
---------------
- Multi-step math problems
- Logical reasoning tasks
- Commonsense reasoning
- Any problem where intermediate steps matter

STRUCTURE (Zero-Shot CoT):
--------------------------
[Question / Problem]

Let's think step by step.

STRUCTURE (Few-Shot CoT):
--------------------------
Question: <example question>
Reasoning: <step-by-step reasoning>
Answer: <final answer>

Question: <actual question>
Reasoning:

=============================================================
"""

# ------------------------------------------------------------------
# Example 1: Zero-Shot CoT — Math Problem
# ------------------------------------------------------------------
zero_shot_cot_math = """
A bakery makes 120 cookies in the morning and 80 in the afternoon.
They sell 75 cookies during the day. How many cookies are left?

Let's think step by step.
"""

# ------------------------------------------------------------------
# Example 2: Zero-Shot CoT — Logic Puzzle
# ------------------------------------------------------------------
zero_shot_cot_logic = """
There are 5 houses in a row. Each house is painted a different color.
The green house is immediately to the left of the white house.
The red house is in the middle. Which position is the green house?

Let's think step by step.
"""

# ------------------------------------------------------------------
# Example 3: Few-Shot CoT — Arithmetic
# ------------------------------------------------------------------
few_shot_cot_arithmetic = """
Question: Roger has 5 tennis balls. He buys 2 more cans of tennis balls.
Each can has 3 balls. How many tennis balls does he have now?
Reasoning:
  - Roger starts with 5 tennis balls.
  - He buys 2 cans, each with 3 balls: 2 × 3 = 6 new balls.
  - Total = 5 + 6 = 11 tennis balls.
Answer: 11

Question: The cafeteria had 23 apples. If they used 20 to make lunch and
bought 6 more, how many apples do they have?
Reasoning:
  - Start with 23 apples.
  - Used 20: 23 - 20 = 3 apples remaining.
  - Bought 6 more: 3 + 6 = 9 apples.
Answer: 9

Question: A library has 400 books. They receive a donation of 150 books
and then lend out 80 books. How many books are in the library now?
Reasoning:
"""

# ------------------------------------------------------------------
# Example 4: Few-Shot CoT — Commonsense Reasoning
# ------------------------------------------------------------------
few_shot_cot_commonsense = """
Question: Would a vegetarian eat a chicken sandwich?
Reasoning:
  - A vegetarian avoids eating meat.
  - Chicken is a type of meat.
  - A chicken sandwich contains chicken.
  - Therefore, a vegetarian would NOT eat a chicken sandwich.
Answer: No

Question: Can you use a metal spoon in a microwave?
Reasoning:
"""

# ------------------------------------------------------------------
# HOW TO USE WITH AN LLM API (OpenAI example)
# ------------------------------------------------------------------
# Uncomment and install: pip install openai
#
# import openai
# openai.api_key = "YOUR_API_KEY"
#
# def chain_of_thought(prompt: str) -> str:
#     response = openai.chat.completions.create(
#         model="gpt-4o-mini",
#         messages=[{"role": "user", "content": prompt}]
#     )
#     return response.choices[0].message.content
#
# print(chain_of_thought(zero_shot_cot_math))
# print(chain_of_thought(few_shot_cot_arithmetic))

# ------------------------------------------------------------------
# STUDENT EXERCISE
# ------------------------------------------------------------------
# Create a Zero-Shot CoT prompt for the following problem:
# "A car travels at 60 km/h. It needs to cover 210 km.
#  The driver stops for 30 minutes for lunch. How long is the trip total?"
#
# Hint: End your prompt with "Let's think step by step."

my_cot_prompt = """
<Write your problem here>

Let's think step by step.
"""

print("=== Chain-of-Thought Prompting Examples ===\n")
print("1. Zero-Shot CoT — Math:")
print(zero_shot_cot_math)
print("2. Zero-Shot CoT — Logic:")
print(zero_shot_cot_logic)
print("3. Few-Shot CoT — Arithmetic:")
print(few_shot_cot_arithmetic)
print("4. Few-Shot CoT — Commonsense:")
print(few_shot_cot_commonsense)
