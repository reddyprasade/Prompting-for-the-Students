"""
=============================================================
Prompting Technique 7: Prompt Chaining
=============================================================

WHAT IS IT?
-----------
Prompt Chaining breaks a complex task into a sequence of smaller,
dependent sub-tasks. The output of one prompt becomes the input
(context) for the next prompt in the chain.

Think of it like an assembly line: each step processes and enriches
the result before passing it forward.

WHEN TO USE IT?
---------------
- Long, multi-step workflows (research → outline → draft → edit)
- When a single prompt would be too long or complex
- When intermediate results need to be verified or transformed
- Building AI pipelines and agents

STRUCTURE:
----------
Prompt 1 → Output 1
Output 1 → Prompt 2 → Output 2
Output 2 → Prompt 3 → Output 3
...

=============================================================
"""

# ------------------------------------------------------------------
# Example: Blog Post Writing Pipeline (3-Step Chain)
# ------------------------------------------------------------------

# STEP 1: Generate an outline
step1_prompt_template = """
You are a content strategist. Create a structured outline for a
blog post about the following topic.

Topic: "{topic}"

Output format:
- Title
- Introduction (one sentence summary)
- 3-5 main section headings
- Conclusion heading
"""

# STEP 2: Write the introduction (using output from Step 1)
step2_prompt_template = """
You are a professional blog writer. Using the outline below,
write a compelling introduction paragraph (3-5 sentences) for the blog post.

Outline:
{outline}

Write only the introduction. Do not write the full article.
"""

# STEP 3: Generate a catchy title and meta description
step3_prompt_template = """
You are an SEO copywriter. Based on the blog post introduction below,
create:
1. A catchy, SEO-friendly title (max 60 characters)
2. A meta description (max 155 characters)

Introduction:
{introduction}

Output format:
Title: <title here>
Meta Description: <meta description here>
"""

# ------------------------------------------------------------------
# Simulated Chain Execution (without API)
# ------------------------------------------------------------------
topic = "The impact of artificial intelligence on modern education"

# Simulate Step 1 output
outline = """
Title: How AI is Transforming Modern Education
Introduction: Artificial intelligence is reshaping classrooms and learning experiences worldwide.
Sections:
  1. Personalized Learning with AI
  2. AI-Powered Tutoring Systems
  3. Automating Administrative Tasks
  4. Challenges and Ethical Concerns
  5. The Future of AI in Education
Conclusion: Preparing Students for an AI-Driven World
"""

# Simulate Step 2 output (using outline from Step 1)
introduction = """
Artificial intelligence is no longer a futuristic concept — it is actively
reshaping how students learn and teachers teach. From personalized learning
platforms that adapt to individual student needs to AI tutors available 24/7,
the impact of AI on modern education is profound. However, with great
opportunity comes great responsibility, as educators and policymakers must
navigate the ethical challenges that AI introduces.
"""

# Demonstrate what each prompt looks like at runtime
print("=== Prompt Chaining: Blog Post Pipeline ===\n")

print("--- STEP 1: Generate Outline ---")
print(step1_prompt_template.format(topic=topic))

print("--- STEP 2: Write Introduction (uses Step 1 output) ---")
print(step2_prompt_template.format(outline=outline))

print("--- STEP 3: Generate Title & Meta Description (uses Step 2 output) ---")
print(step3_prompt_template.format(introduction=introduction))

# ------------------------------------------------------------------
# HOW TO USE WITH AN LLM API (OpenAI example)
# ------------------------------------------------------------------
# Uncomment and install: pip install openai
#
# import openai
# openai.api_key = "YOUR_API_KEY"
#
# def call_llm(prompt: str) -> str:
#     response = openai.chat.completions.create(
#         model="gpt-4o-mini",
#         messages=[{"role": "user", "content": prompt}]
#     )
#     return response.choices[0].message.content
#
# def run_blog_chain(topic: str) -> dict:
#     # Step 1
#     prompt1 = step1_prompt_template.format(topic=topic)
#     outline = call_llm(prompt1)
#     print("=== OUTLINE ===\n", outline)
#
#     # Step 2
#     prompt2 = step2_prompt_template.format(outline=outline)
#     introduction = call_llm(prompt2)
#     print("=== INTRODUCTION ===\n", introduction)
#
#     # Step 3
#     prompt3 = step3_prompt_template.format(introduction=introduction)
#     seo_output = call_llm(prompt3)
#     print("=== SEO OUTPUT ===\n", seo_output)
#
#     return {"outline": outline, "introduction": introduction, "seo": seo_output}
#
# result = run_blog_chain("The impact of artificial intelligence on modern education")

# ------------------------------------------------------------------
# Another Chain Example: Code Review Pipeline
# ------------------------------------------------------------------
code_review_chain = {
    "step1": """
Review the following Python function for bugs only.
List each bug on a separate line prefixed with "BUG:".

```python
{code}
```
""",
    "step2": """
Given the following list of bugs found in a Python function:
{bugs}

Rewrite the corrected version of the function. Include only the
fixed code, no explanation.
""",
    "step3": """
Write a docstring for the following Python function.
Include: description, parameters (Args), and return value (Returns).

```python
{fixed_code}
```
"""
}

print("\n--- Code Review Chain Prompts (templates) ---")
for step, template in code_review_chain.items():
    print(f"\n{step.upper()}:\n{template}")

# ------------------------------------------------------------------
# STUDENT EXERCISE
# ------------------------------------------------------------------
# Design a 3-step prompt chain for summarizing a research paper.
# Step 1: Extract key findings
# Step 2: Summarize the findings in plain language
# Step 3: Generate 3 questions a student could explore further

my_chain = {
    "step1_extract": """
    <Write prompt to extract key findings from a paper>
    Paper: {paper_text}
    """,
    "step2_summarize": """
    <Write prompt to summarize findings in plain language>
    Findings: {findings}
    """,
    "step3_questions": """
    <Write prompt to generate follow-up study questions>
    Summary: {summary}
    """
}
