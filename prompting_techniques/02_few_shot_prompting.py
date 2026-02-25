"""
=============================================================
Prompting Technique 2: Few-Shot Prompting
=============================================================

WHAT IS IT?
-----------
Few-shot prompting provides a small number of input-output
EXAMPLES (shots) before the actual task. The model learns
the pattern from the examples and applies it to new input.

WHEN TO USE IT?
---------------
- When zero-shot gives inconsistent or incorrect outputs
- Custom classification categories
- Enforcing a specific output format
- Domain-specific tasks the model may not handle well by default

STRUCTURE:
----------
[Task Description (optional)]

Example 1:
  Input: <example input>
  Output: <example output>

Example 2:
  Input: <example input>
  Output: <example output>

Now:
  Input: <actual input>
  Output:

NUMBER OF SHOTS:
----------------
- 1-shot : one example
- few-shot : 2–5 examples (most common)
- many-shot: 6+ examples (use when task is complex)

=============================================================
"""

# ------------------------------------------------------------------
# Example 1: Custom Sentiment Labels
# ------------------------------------------------------------------
few_shot_sentiment = """
Classify each review into one of these categories: LOVE, HATE, MEH.

Review: "This laptop is absolutely fantastic, best purchase ever!"
Category: LOVE

Review: "Completely useless, broke after one day."
Category: HATE

Review: "It's okay, nothing special about it."
Category: MEH

Review: "Decent product but not worth the price."
Category:
"""

# ------------------------------------------------------------------
# Example 2: Entity Extraction
# ------------------------------------------------------------------
few_shot_entity = """
Extract the person name and city from each sentence.

Sentence: "Alice moved to Berlin last year."
Person: Alice | City: Berlin

Sentence: "Bob is visiting Tokyo for a conference."
Person: Bob | City: Tokyo

Sentence: "Maria has been living in Mumbai since 2020."
Person: | City:
"""

# ------------------------------------------------------------------
# Example 3: Math Word Problem Formatting
# ------------------------------------------------------------------
few_shot_math = """
Solve the math word problem. Show only the final numeric answer.

Problem: "If a train travels 60 miles per hour for 2 hours, how far does it go?"
Answer: 120 miles

Problem: "A store has 45 apples. They sell 18. How many are left?"
Answer: 27 apples

Problem: "Sarah has $150. She spends $37 on books and $25 on lunch. How much money does she have left?"
Answer:
"""

# ------------------------------------------------------------------
# Example 4: Text-to-Emoji
# ------------------------------------------------------------------
few_shot_emoji = """
Convert the given emotion or activity into a fitting emoji.

Emotion/Activity: happy
Emoji: 😊

Emotion/Activity: running
Emoji: 🏃

Emotion/Activity: eating pizza
Emoji: 🍕

Emotion/Activity: studying
Emoji:
"""

# ------------------------------------------------------------------
# HOW TO USE WITH AN LLM API (OpenAI example)
# ------------------------------------------------------------------
# Uncomment and install: pip install openai
#
# import openai
# openai.api_key = "YOUR_API_KEY"
#
# def few_shot(prompt: str) -> str:
#     response = openai.chat.completions.create(
#         model="gpt-4o-mini",
#         messages=[{"role": "user", "content": prompt}]
#     )
#     return response.choices[0].message.content
#
# print(few_shot(few_shot_sentiment))
# print(few_shot(few_shot_entity))
# print(few_shot(few_shot_math))
# print(few_shot(few_shot_emoji))

# ------------------------------------------------------------------
# STUDENT EXERCISE
# ------------------------------------------------------------------
# Task: Write a few-shot prompt that classifies movie genres.
# Provide 2-3 examples with movie descriptions and their genres,
# then add a new movie description for the model to classify.

my_few_shot_prompt = """
<Task description (optional)>

Description: <example description 1>
Genre: <example genre 1>

Description: <example description 2>
Genre: <example genre 2>

Description: <new movie description>
Genre:
"""

print("=== Few-Shot Prompting Examples ===\n")
print("1. Custom Sentiment Classification:")
print(few_shot_sentiment)
print("2. Entity Extraction:")
print(few_shot_entity)
print("3. Math Problem:")
print(few_shot_math)
print("4. Text to Emoji:")
print(few_shot_emoji)
