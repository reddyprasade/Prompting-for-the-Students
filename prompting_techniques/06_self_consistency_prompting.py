"""
=============================================================
Prompting Technique 6: Self-Consistency Prompting
=============================================================

WHAT IS IT?
-----------
Self-Consistency is an advanced decoding strategy for Chain-of-Thought
prompting. Instead of generating a single reasoning path, you generate
MULTIPLE diverse reasoning paths (by running the prompt several times
with some variation), then pick the most consistent / most common answer.

The intuition: if many different reasoning paths all lead to the same
answer, that answer is more likely to be correct.

STEPS:
------
1. Write a Chain-of-Thought prompt for a reasoning problem.
2. Generate multiple completions (N times, temperature > 0).
3. Parse the final answer from each completion.
4. Take the majority vote as the final answer.

WHEN TO USE IT?
---------------
- Complex math reasoning
- Multi-step logic puzzles
- Tasks where a single model run might make errors
- Any CoT task where higher accuracy is needed

NOTE: This requires calling the LLM multiple times, so it costs
      more tokens/API calls than a single-run approach.

=============================================================
"""

import random
from collections import Counter

# ------------------------------------------------------------------
# Example Prompt (used for multiple runs)
# ------------------------------------------------------------------
self_consistency_prompt = """
A store sells apples for $0.50 each and oranges for $0.75 each.
Alice buys 4 apples and 3 oranges. She pays with a $10 bill.
How much change does she receive?

Let's think step by step.
"""

# ------------------------------------------------------------------
# Simulated Responses (in practice, these come from LLM API calls)
# ------------------------------------------------------------------
# Simulating what multiple LLM runs might return:

simulated_responses = [
    """
    Cost of apples: 4 × $0.50 = $2.00
    Cost of oranges: 3 × $0.75 = $2.25
    Total: $2.00 + $2.25 = $4.25
    Change: $10.00 - $4.25 = $5.75
    Answer: $5.75
    """,
    """
    Apples cost $0.50 each, so 4 apples = 4 * 0.5 = $2.
    Oranges cost $0.75 each, so 3 oranges = 3 * 0.75 = $2.25.
    Total bill = 2 + 2.25 = $4.25.
    Change from $10 = 10 - 4.25 = $5.75.
    Answer: $5.75
    """,
    """
    4 apples × $0.50 = $2.00
    3 oranges × $0.75 = $2.25
    Total spent = $4.25
    Change = $10 - $4.25 = $5.75
    Answer: $5.75
    """,
    """
    4 × 0.50 = 2.00
    3 × 0.75 = 2.25
    Total = 4.50  ← (error in one run)
    Change = 10 - 4.50 = $5.50
    Answer: $5.50
    """,
    """
    Apples: 4 × 0.50 = 2.00
    Oranges: 3 × 0.75 = 2.25
    Total = 4.25
    Change = 10.00 - 4.25 = 5.75
    Answer: $5.75
    """
]

# ------------------------------------------------------------------
# Self-Consistency: Extract Answers and Vote
# ------------------------------------------------------------------

def extract_answer(response: str) -> str:
    """Simple extraction: find the last line starting with 'Answer:'."""
    for line in reversed(response.strip().split("\n")):
        line = line.strip()
        if line.lower().startswith("answer:"):
            return line.split(":", 1)[1].strip()
    return "unknown"

def self_consistency_vote(responses: list) -> str:
    """Return the most common answer across all responses."""
    answers = [extract_answer(r) for r in responses]
    vote_counts = Counter(answers)
    most_common_answer, count = vote_counts.most_common(1)[0]
    return most_common_answer, vote_counts

# Run self-consistency
final_answer, votes = self_consistency_vote(simulated_responses)

print("=== Self-Consistency Prompting ===\n")
print("Prompt:")
print(self_consistency_prompt)
print(f"Generated {len(simulated_responses)} reasoning paths.\n")
print("Extracted Answers and Votes:")
for answer, count in votes.items():
    print(f"  {answer!r:15s} → {count} vote(s)")
print(f"\n✅ Final Answer (majority vote): {final_answer}")

# ------------------------------------------------------------------
# HOW TO USE WITH AN LLM API (OpenAI example)
# ------------------------------------------------------------------
# Uncomment and install: pip install openai
#
# import openai
# openai.api_key = "YOUR_API_KEY"
#
# def get_cot_response(prompt: str, temperature: float = 0.7) -> str:
#     response = openai.chat.completions.create(
#         model="gpt-4o-mini",
#         messages=[{"role": "user", "content": prompt}],
#         temperature=temperature
#     )
#     return response.choices[0].message.content
#
# def self_consistency_api(prompt: str, n: int = 5) -> str:
#     responses = [get_cot_response(prompt) for _ in range(n)]
#     answer, votes = self_consistency_vote(responses)
#     print("All answers:", [extract_answer(r) for r in responses])
#     print(f"Final Answer: {answer}")
#     return answer
#
# self_consistency_api(self_consistency_prompt, n=5)

# ------------------------------------------------------------------
# STUDENT EXERCISE
# ------------------------------------------------------------------
# Write a new math word problem prompt and simulate 5 responses.
# Use the self_consistency_vote() function to find the majority answer.
#
# 1. Write the problem prompt
# 2. Simulate/collect 5 responses (or run the API 5 times)
# 3. Call extract_answer() on each
# 4. Call self_consistency_vote() to find the best answer

my_problem_prompt = """
<Write your math or logic problem here>

Let's think step by step.
"""
