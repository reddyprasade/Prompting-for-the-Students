"""
=============================================================
Prompting Technique 1: Zero-Shot Prompting
=============================================================

WHAT IS IT?
-----------
Zero-shot prompting means giving the LLM a task with NO examples.
You simply describe the task and let the model use its pre-trained
knowledge to answer.

WHEN TO USE IT?
---------------
- Quick, straightforward tasks
- When the model already understands the domain well
- Summarization, translation, classification, Q&A

STRUCTURE:
----------
[Task Instruction] + [Input Text]

=============================================================
"""

# ------------------------------------------------------------------
# Example 1: Sentiment Classification
# ------------------------------------------------------------------
zero_shot_sentiment = """
Classify the sentiment of the following review as Positive, Negative, or Neutral.

Review: "The battery life is amazing but the camera quality is disappointing."

Sentiment:
"""

# ------------------------------------------------------------------
# Example 2: Language Translation
# ------------------------------------------------------------------
zero_shot_translation = """
Translate the following English sentence into French.

Sentence: "Machine learning is transforming the world."

Translation:
"""

# ------------------------------------------------------------------
# Example 3: Text Summarization
# ------------------------------------------------------------------
zero_shot_summarization = """
Summarize the following paragraph in one sentence.

Paragraph: "Artificial intelligence (AI) refers to the simulation of
human intelligence processes by machines, especially computer systems.
These processes include learning, reasoning, and self-correction. AI is
being applied in a variety of domains including healthcare, finance,
education, and transportation."

Summary:
"""

# ------------------------------------------------------------------
# Example 4: Simple Q&A
# ------------------------------------------------------------------
zero_shot_qa = """
Answer the following question.

Question: What is the capital of Japan?

Answer:
"""

# ------------------------------------------------------------------
# HOW TO USE WITH AN LLM API (OpenAI example)
# ------------------------------------------------------------------
# Uncomment and install: pip install openai
#
# import openai
# openai.api_key = "YOUR_API_KEY"
#
# def zero_shot(prompt: str) -> str:
#     response = openai.chat.completions.create(
#         model="gpt-4o-mini",
#         messages=[{"role": "user", "content": prompt}]
#     )
#     return response.choices[0].message.content
#
# print(zero_shot(zero_shot_sentiment))
# print(zero_shot(zero_shot_translation))
# print(zero_shot(zero_shot_summarization))
# print(zero_shot(zero_shot_qa))

# ------------------------------------------------------------------
# STUDENT EXERCISE
# ------------------------------------------------------------------
# Write your own zero-shot prompt below for any task you choose.
# Ideas: grammar correction, keyword extraction, topic classification.

my_zero_shot_prompt = """
<Write your task instruction here>

Input: <Provide your input text>

Output:
"""

print("=== Zero-Shot Prompting Examples ===\n")
print("1. Sentiment Classification Prompt:")
print(zero_shot_sentiment)
print("2. Translation Prompt:")
print(zero_shot_translation)
print("3. Summarization Prompt:")
print(zero_shot_summarization)
print("4. Q&A Prompt:")
print(zero_shot_qa)
