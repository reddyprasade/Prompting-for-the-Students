"""
=============================================================
Prompting Technique 8: Tree-of-Thought (ToT) Prompting
=============================================================

WHAT IS IT?
-----------
Tree-of-Thought (ToT) prompting extends Chain-of-Thought by exploring
MULTIPLE reasoning paths simultaneously, like branches of a tree.
The model (or system) evaluates which branches look most promising,
backtracks when a path fails, and continues with the best paths.

ANALOGY: A chess player doesn't just think one move ahead — they
mentally explore many possible sequences, evaluate each, and choose
the best move. ToT does the same for reasoning tasks.

VARIANTS:
---------
1. Prompt-based ToT: Use a single prompt that instructs the model
   to consider multiple approaches, evaluate them, and choose the best.
2. Multi-agent ToT: Multiple LLM calls generate different branches,
   and a "critic" call evaluates and selects the best path.

WHEN TO USE IT?
---------------
- Complex puzzles and planning problems
- Creative tasks needing multiple options evaluated
- Strategic decision making
- Problems where the first approach might be wrong

=============================================================
"""

# ------------------------------------------------------------------
# Example 1: Simple Prompt-Based ToT (Single Prompt)
# ------------------------------------------------------------------
tot_single_prompt = """
Imagine three different experts are solving the following problem.
Each expert shares one step of their thinking, then all experts
continue to the next step. If any expert realizes their approach
is wrong, they stop and acknowledge it. Continue until one or more
experts reach a final answer.

Problem: "A farmer has 17 sheep. All but 9 run away. How many sheep
are left?"

Expert 1:
Expert 2:
Expert 3:
"""

# ------------------------------------------------------------------
# Example 2: Multi-Step ToT for a Planning Problem
# ------------------------------------------------------------------
tot_planning = """
Three strategic advisors are helping plan a product launch for a
new mobile app. They each suggest a different initial approach.
After sharing their approach, they evaluate each other's ideas and
converge on the best combined strategy.

Product: A language learning app targeting adult professionals.

Advisor 1 (Marketing Expert): My initial approach is...
Advisor 2 (Product Manager): My initial approach is...
Advisor 3 (Growth Hacker): My initial approach is...

[Evaluation Round]
All advisors evaluate the three approaches and vote on the best
elements to combine into a final strategy:

Final Strategy:
"""

# ------------------------------------------------------------------
# Example 3: ToT for Creative Writing
# ------------------------------------------------------------------
tot_creative = """
Three authors are each writing a different opening line for a short
story about a robot who discovers emotions for the first time.

Author 1 (writes literary fiction):
Author 2 (writes science fiction thrillers):
Author 3 (writes children's books):

Each author reflects on which opening is most engaging and why.
Then, together they craft a final opening line that combines the
best elements.

Final Opening Line:
"""

# ------------------------------------------------------------------
# Example 4: Multi-Agent ToT (Programmatic Approach)
# ------------------------------------------------------------------
# In a full implementation, you would:
# 1. Run N "generator" prompts to produce N reasoning branches
# 2. Run an "evaluator" prompt to score each branch
# 3. Select the highest-scoring branch and continue from there

generator_prompt_template = """
Solve the following problem using a step-by-step approach.
Approach #{n}: Try a {strategy} strategy.

Problem: {problem}

Step-by-step reasoning:
"""

evaluator_prompt_template = """
You are evaluating different reasoning approaches for the following problem.

Problem: {problem}

Here are {n} different reasoning paths:
{paths}

Score each path from 1-10 based on:
- Correctness
- Logical soundness
- Completeness

Scores and recommendation:
"""

# Example problem
problem = "You have a 3-liter jug and a 5-liter jug. How can you measure exactly 4 liters of water?"

strategies = ["trial and error", "algebraic", "visual/diagrammatic"]

print("=== Tree-of-Thought Prompting Examples ===\n")

print("1. Simple ToT (Single Prompt — 3 Experts):")
print(tot_single_prompt)

print("2. ToT for Planning:")
print(tot_planning)

print("3. ToT for Creative Writing:")
print(tot_creative)

print("4. Multi-Agent ToT — Generator Prompts:")
for i, strategy in enumerate(strategies, 1):
    print(generator_prompt_template.format(n=i, strategy=strategy, problem=problem))

print("\nEvaluator Prompt Template:")
print(evaluator_prompt_template.format(problem=problem, n=3, paths="[branch 1], [branch 2], [branch 3]"))

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
# def tree_of_thought(problem: str, strategies: list, n_branches: int = 3) -> str:
#     # Generate multiple branches
#     branches = []
#     for i, strategy in enumerate(strategies[:n_branches], 1):
#         prompt = generator_prompt_template.format(n=i, strategy=strategy, problem=problem)
#         branch = call_llm(prompt)
#         branches.append(f"Approach {i} ({strategy}):\n{branch}")
#         print(f"Generated branch {i}")
#
#     # Evaluate branches
#     paths_text = "\n\n".join(branches)
#     eval_prompt = evaluator_prompt_template.format(
#         problem=problem, n=n_branches, paths=paths_text
#     )
#     evaluation = call_llm(eval_prompt)
#     print("Evaluation:\n", evaluation)
#     return evaluation
#
# tree_of_thought(problem, strategies)

# ------------------------------------------------------------------
# STUDENT EXERCISE
# ------------------------------------------------------------------
# Use the single-prompt ToT pattern to solve the following problem.
# Ask 3 experts with different backgrounds (e.g., mathematician,
# programmer, logician) to reason through the problem.
#
# Problem: "Is it better to study one subject for 4 hours straight,
#            or to split your study into 4 one-hour sessions with breaks?"

my_tot_prompt = """
Three experts with different backgrounds are answering the following question.
They each share their perspective, then evaluate each other's points and
reach a consensus.

Question: <your question here>

Expert 1 (<background>):
Expert 2 (<background>):
Expert 3 (<background>):

[Discussion and Consensus]
Final Recommendation:
"""
