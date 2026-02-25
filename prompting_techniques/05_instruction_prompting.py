"""
=============================================================
Prompting Technique 5: Instruction Prompting
=============================================================

WHAT IS IT?
-----------
Instruction prompting involves writing clear, explicit instructions
to guide the model's behavior, format, tone, and constraints.
It is the foundation of all good prompting — being specific and
unambiguous about exactly what you want.

KEY COMPONENTS OF A GOOD INSTRUCTION PROMPT:
---------------------------------------------
1. Task       - What should the model do?
2. Context    - What background information is relevant?
3. Format     - How should the output be structured?
4. Tone       - What style or voice should be used?
5. Constraints - What are the limits (length, language, etc.)?

WHEN TO USE IT?
---------------
- Formatting outputs (JSON, lists, tables, markdown)
- Controlling response style
- Setting output length
- Specifying what to include or exclude

=============================================================
"""

# ------------------------------------------------------------------
# Example 1: Structured Output (JSON)
# ------------------------------------------------------------------
instruction_json = """
Extract the following information from the text below and return it
as a valid JSON object with keys: "name", "age", "city", "occupation".
Do not include any explanation, only the JSON.

Text: "Hi, I'm Sarah. I'm 28 years old, work as a software engineer,
and I live in San Francisco."
"""

# Expected output:
# {
#   "name": "Sarah",
#   "age": 28,
#   "city": "San Francisco",
#   "occupation": "software engineer"
# }

# ------------------------------------------------------------------
# Example 2: Bullet Point Summary with Constraints
# ------------------------------------------------------------------
instruction_bullets = """
Summarize the following article in exactly 5 bullet points.
Each bullet point should be one sentence long.
Do not use any introductory text; start directly with the bullet points.

Article:
"Deep learning is a subset of machine learning that uses neural networks
with many layers to learn representations of data. It has achieved
state-of-the-art results in image recognition, speech recognition,
and natural language processing. Training deep learning models requires
large amounts of labeled data and significant computational power.
Transfer learning allows models trained on one task to be applied to
related tasks, reducing data and compute requirements. Popular deep
learning frameworks include TensorFlow, PyTorch, and Keras."
"""

# ------------------------------------------------------------------
# Example 3: Rewrite with Tone Control
# ------------------------------------------------------------------
instruction_tone = """
Rewrite the following email in a professional, polite, and concise tone.
Keep it under 60 words. Do not change the core message.

Original email:
"Hey!! so I wanted to let you know that I can't come to the meeting
tomorrow because something came up. Sorry about that. Can we do it
some other time?? Thanks"
"""

# ------------------------------------------------------------------
# Example 4: Constrained Generation
# ------------------------------------------------------------------
instruction_constrained = """
Generate a motivational quote about learning.
Requirements:
- Maximum 20 words
- Must include the word "curiosity"
- Do not use clichés like "reach for the stars" or "follow your dreams"
- Output only the quote, no attribution or explanation
"""

# ------------------------------------------------------------------
# Example 5: Step-by-Step Instructions (How-To)
# ------------------------------------------------------------------
instruction_howto = """
Write step-by-step instructions for how to create a virtual environment
in Python and install a package using pip.

Format:
- Numbered steps
- Include the exact commands in code blocks (use backticks)
- Target audience: beginners with no prior experience
- Maximum 10 steps
"""

# ------------------------------------------------------------------
# Example 6: Comparative Table
# ------------------------------------------------------------------
instruction_table = """
Create a comparison table of Python, JavaScript, and Java.
Compare them on the following criteria:
- Typing system (static/dynamic)
- Primary use case
- Performance (high/medium/low)
- Learning curve (easy/moderate/hard)

Format the output as a markdown table.
"""

# ------------------------------------------------------------------
# HOW TO USE WITH AN LLM API (OpenAI example)
# ------------------------------------------------------------------
# Uncomment and install: pip install openai
#
# import openai
# openai.api_key = "YOUR_API_KEY"
#
# def instruction_prompt(prompt: str) -> str:
#     response = openai.chat.completions.create(
#         model="gpt-4o-mini",
#         messages=[{"role": "user", "content": prompt}]
#     )
#     return response.choices[0].message.content
#
# print(instruction_prompt(instruction_json))
# print(instruction_prompt(instruction_bullets))
# print(instruction_prompt(instruction_table))

# ------------------------------------------------------------------
# STUDENT EXERCISE
# ------------------------------------------------------------------
# Write an instruction prompt that asks the model to generate a
# weekly study schedule for a student. Include constraints such as:
# - 5 subjects
# - Monday to Friday only
# - 2 hours of study per day
# - Output as a markdown table

my_instruction_prompt = """
<Write clear instructions here>

Constraints:
- <constraint 1>
- <constraint 2>
- <constraint 3>

Format: <specify the output format>
"""

print("=== Instruction Prompting Examples ===\n")
print("1. Structured JSON Output:")
print(instruction_json)
print("2. Bullet Point Summary:")
print(instruction_bullets)
print("3. Tone Rewriting:")
print(instruction_tone)
print("4. Constrained Generation:")
print(instruction_constrained)
print("5. How-To Instructions:")
print(instruction_howto)
print("6. Comparison Table:")
print(instruction_table)
