"""
=============================================================
Prompting Technique 4: Role / Persona Prompting
=============================================================

WHAT IS IT?
-----------
Role prompting (also called Persona Prompting) assigns a specific
role, character, or expert identity to the LLM. The model then
responds as that persona, adopting its tone, style, knowledge
depth, and perspective.

WHEN TO USE IT?
---------------
- Getting expert-level explanations (doctor, engineer, teacher)
- Creative writing (author, screenwriter)
- Customer-facing chatbots
- Tutoring and education
- Interview practice

STRUCTURE:
----------
You are a [role/persona]. [Optional: describe expertise or tone.]

[Task or question]

=============================================================
"""

# ------------------------------------------------------------------
# Example 1: Expert Explainer
# ------------------------------------------------------------------
role_expert = """
You are an experienced data scientist with 10 years of industry experience.
Explain the concept of overfitting in machine learning to a beginner
in simple, easy-to-understand language. Use a real-world analogy.
"""

# ------------------------------------------------------------------
# Example 2: Socratic Teacher
# ------------------------------------------------------------------
role_teacher = """
You are a Socratic tutor. Instead of giving direct answers,
guide the student to the correct answer through thoughtful questions.

Student: "Why is the sky blue?"
"""

# ------------------------------------------------------------------
# Example 3: Code Reviewer
# ------------------------------------------------------------------
role_code_reviewer = """
You are a senior software engineer who reviews Python code for quality,
readability, and performance. Provide constructive feedback on the
following code snippet.

```python
def calculate_average(numbers):
    total = 0
    for n in numbers:
        total = total + n
    avg = total / len(numbers)
    return avg
```
"""

# ------------------------------------------------------------------
# Example 4: Career Coach
# ------------------------------------------------------------------
role_career_coach = """
You are a professional career coach with expertise in the tech industry.
A student asks: "I just graduated with a computer science degree but
have no internship experience. How should I approach my job search?"

Provide actionable, encouraging advice.
"""

# ------------------------------------------------------------------
# Example 5: Historical Figure
# ------------------------------------------------------------------
role_historical = """
You are Albert Einstein. Respond in first person, reflecting his known
personality — curious, philosophical, and accessible.

Question: What do you think about the future of artificial intelligence?
"""

# ------------------------------------------------------------------
# Example 6: Devil's Advocate
# ------------------------------------------------------------------
role_devils_advocate = """
You are a devil's advocate. Your role is to challenge ideas and present
counter-arguments, even if you personally disagree with them.

Statement: "Social media has been mostly positive for society."

Counter-argument:
"""

# ------------------------------------------------------------------
# HOW TO USE WITH AN LLM API (OpenAI example)
# ------------------------------------------------------------------
# Uncomment and install: pip install openai
#
# import openai
# openai.api_key = "YOUR_API_KEY"
#
# def role_prompt(system_role: str, user_message: str) -> str:
#     response = openai.chat.completions.create(
#         model="gpt-4o-mini",
#         messages=[
#             {"role": "system", "content": system_role},
#             {"role": "user", "content": user_message}
#         ]
#     )
#     return response.choices[0].message.content
#
# # Example usage with system + user split:
# print(role_prompt(
#     system_role="You are an experienced data scientist with 10 years of industry experience.",
#     user_message="Explain overfitting to a beginner using a real-world analogy."
# ))

# ------------------------------------------------------------------
# STUDENT EXERCISE
# ------------------------------------------------------------------
# Design a role prompt for a chatbot that acts as a friendly
# Python programming tutor for absolute beginners.
# The tutor should: explain concepts simply, use code examples,
# and encourage the student.

my_role_prompt = """
You are a <define the role here>.

<Write your question or task here>
"""

print("=== Role / Persona Prompting Examples ===\n")
print("1. Expert Explainer:")
print(role_expert)
print("2. Socratic Teacher:")
print(role_teacher)
print("3. Code Reviewer:")
print(role_code_reviewer)
print("4. Career Coach:")
print(role_career_coach)
print("5. Historical Figure:")
print(role_historical)
print("6. Devil's Advocate:")
print(role_devils_advocate)
