"""
=============================================================
Prompting Technique 9: Generated Knowledge Prompting
=============================================================

WHAT IS IT?
-----------
Generated Knowledge Prompting is a two-step technique:

  Step 1 — GENERATE: Ask the LLM to generate relevant background
           knowledge or facts about the topic.
  Step 2 — INTEGRATE: Use that generated knowledge as context in
           a second prompt to answer the actual question or complete
           the actual task.

This improves accuracy because the model first "activates" and
makes explicit relevant knowledge, then uses it to reason.

WHEN TO USE IT?
---------------
- Commonsense reasoning tasks
- Questions that benefit from background knowledge
- Reducing hallucinations by grounding answers in stated facts
- Science, history, and fact-based Q&A

STRUCTURE:
----------
STEP 1 Prompt:
  "Generate [N] relevant facts about [topic]."

STEP 2 Prompt:
  "Using the following facts:
   [facts from Step 1]

   Answer: [original question]"

=============================================================
"""

# ------------------------------------------------------------------
# Example 1: Science Question
# ------------------------------------------------------------------

# STEP 1: Generate knowledge about the topic
gen_knowledge_step1_science = """
Generate 5 relevant scientific facts about photosynthesis.
Be concise — one sentence per fact.
"""

# Simulated output from Step 1:
generated_facts_science = """
1. Photosynthesis occurs primarily in the chloroplasts of plant cells.
2. It requires sunlight, carbon dioxide (CO2), and water (H2O) as inputs.
3. The process produces glucose (C6H12O6) and releases oxygen (O2) as a byproduct.
4. Chlorophyll is the green pigment that absorbs light energy for photosynthesis.
5. There are two main stages: the light-dependent reactions and the Calvin cycle.
"""

# STEP 2: Use the knowledge to answer a question
gen_knowledge_step2_science = f"""
Using the following facts about photosynthesis:
{generated_facts_science}

Answer the question below clearly and accurately.

Question: Why are plants green, and what role does their color play in making food?
"""

# ------------------------------------------------------------------
# Example 2: History Question
# ------------------------------------------------------------------
gen_knowledge_step1_history = """
Generate 4 key facts about the causes of World War I.
One sentence per fact.
"""

generated_facts_history = """
1. The assassination of Archduke Franz Ferdinand of Austria in 1914 was the immediate trigger.
2. A complex system of military alliances meant that war between two nations quickly involved many others.
3. Extreme nationalism in Europe led to intense competition between major powers.
4. Militarism — the buildup of military forces — had created an arms race between European nations.
"""

gen_knowledge_step2_history = f"""
Using the following historical facts:
{generated_facts_history}

Explain in 3-4 sentences why World War I spread so quickly across Europe.
"""

# ------------------------------------------------------------------
# Example 3: Commonsense Reasoning
# ------------------------------------------------------------------
gen_knowledge_step1_commonsense = """
Generate 3 relevant facts about how exercise affects the human brain.
One sentence per fact.
"""

generated_facts_commonsense = """
1. Exercise increases the production of BDNF (Brain-Derived Neurotrophic Factor), which supports neuron growth.
2. Physical activity improves blood flow to the brain, enhancing cognitive performance.
3. Regular exercise is associated with reduced symptoms of depression and anxiety.
"""

gen_knowledge_step2_commonsense = f"""
Using these facts about exercise and the brain:
{generated_facts_commonsense}

Answer: Should students exercise before studying? Why or why not? (2-3 sentences)
"""

# ------------------------------------------------------------------
# Print Examples
# ------------------------------------------------------------------
print("=== Generated Knowledge Prompting Examples ===\n")

print("--- Example 1: Science ---")
print("STEP 1 — Generate Knowledge:")
print(gen_knowledge_step1_science)
print("(Simulated knowledge output):", generated_facts_science)
print("STEP 2 — Use Knowledge to Answer:")
print(gen_knowledge_step2_science)

print("--- Example 2: History ---")
print("STEP 1 — Generate Knowledge:")
print(gen_knowledge_step1_history)
print("(Simulated knowledge output):", generated_facts_history)
print("STEP 2 — Use Knowledge to Answer:")
print(gen_knowledge_step2_history)

print("--- Example 3: Commonsense Reasoning ---")
print("STEP 1 — Generate Knowledge:")
print(gen_knowledge_step1_commonsense)
print("(Simulated knowledge output):", generated_facts_commonsense)
print("STEP 2 — Use Knowledge to Answer:")
print(gen_knowledge_step2_commonsense)

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
# def generated_knowledge(knowledge_prompt: str, question_template: str) -> str:
#     # Step 1: Generate knowledge
#     knowledge = call_llm(knowledge_prompt)
#     print("Generated Knowledge:\n", knowledge)
#
#     # Step 2: Use knowledge to answer
#     final_prompt = question_template.format(knowledge=knowledge)
#     answer = call_llm(final_prompt)
#     print("Final Answer:\n", answer)
#     return answer
#
# knowledge_prompt = "Generate 5 relevant facts about climate change. One sentence per fact."
# question_template = """
# Using the following facts about climate change:
# {knowledge}
#
# Question: What are the most urgent actions humans should take to address climate change?
# """
# generated_knowledge(knowledge_prompt, question_template)

# ------------------------------------------------------------------
# STUDENT EXERCISE
# ------------------------------------------------------------------
# Choose a topic you are studying (biology, history, economics, etc.)
# 1. Write a Step 1 prompt to generate 4-5 key facts about the topic
# 2. Write a Step 2 prompt that uses those facts to answer a specific question

my_step1_prompt = """
Generate 5 relevant facts about <your topic here>.
One sentence per fact.
"""

my_step2_prompt = """
Using the following facts about <your topic>:
{knowledge}

Question: <your question here>
"""
