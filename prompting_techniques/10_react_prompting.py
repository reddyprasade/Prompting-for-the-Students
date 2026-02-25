"""
=============================================================
Prompting Technique 10: ReAct Prompting
(Reasoning + Acting)
=============================================================

WHAT IS IT?
-----------
ReAct (Reasoning + Acting) is a prompting framework that interleaves
reasoning traces with action calls. The model alternates between:

  - THOUGHT: The model reasons about what to do next.
  - ACTION: The model calls a tool or takes an action (e.g., search, calculate).
  - OBSERVATION: The result of the action is fed back to the model.
  - ... (repeats until a final answer is reached)

This creates a "thinking while doing" loop that is the foundation
of modern AI agents.

WHEN TO USE IT?
---------------
- Building AI agents that use tools (search, calculators, databases)
- Question answering that requires up-to-date information
- Multi-step tasks requiring external lookups
- Autonomous task completion workflows

STRUCTURE:
----------
Question: <question>

Thought 1: <reasoning about what to do>
Action 1: <tool_name>[<query>]
Observation 1: <result of the action>

Thought 2: <reasoning about observation>
Action 2: <tool_name>[<query>]
Observation 2: <result>

...

Thought N: I now know the final answer.
Final Answer: <answer>

=============================================================
"""

# ------------------------------------------------------------------
# Example 1: ReAct Trace for a Factual Question
# ------------------------------------------------------------------
react_example_1 = """
Question: What is the population of the capital city of Australia,
and which continent is Australia on?

Thought 1: I need to find the capital city of Australia first.
Action 1: Search[capital city of Australia]
Observation 1: The capital of Australia is Canberra.

Thought 2: Now I need the population of Canberra.
Action 2: Search[population of Canberra 2024]
Observation 2: The population of Canberra is approximately 472,000 (2024).

Thought 3: I also need to confirm the continent Australia belongs to.
Action 3: Search[continent of Australia]
Observation 3: Australia is both a country and a continent; it is located
in the continent of Australia/Oceania.

Thought 4: I now have all the information needed to answer the question.
Final Answer: The capital of Australia is Canberra, with a population of
approximately 472,000. Australia is located on the continent of Oceania
(also called Australia/Oceania).
"""

# ------------------------------------------------------------------
# Example 2: ReAct Trace for a Calculation Task
# ------------------------------------------------------------------
react_example_2 = """
Question: If a jacket costs $120 and is on sale for 25% off, and
there is an additional 8% sales tax, what is the final price?

Thought 1: I need to calculate the discounted price first.
Action 1: Calculate[120 * (1 - 0.25)]
Observation 1: 120 * 0.75 = 90.0

Thought 2: Now I apply the 8% sales tax to $90.
Action 2: Calculate[90 * (1 + 0.08)]
Observation 2: 90 * 1.08 = 97.2

Thought 3: The final price is $97.20.
Final Answer: The final price of the jacket is $97.20.
"""

# ------------------------------------------------------------------
# Example 3: ReAct Prompt Template for Students
# ------------------------------------------------------------------
react_prompt_template = """
Answer the following question using a step-by-step Reasoning + Acting process.
For each step, use the format:
  Thought N: <your reasoning>
  Action N: <action_type>[<query or expression>]
  Observation N: <result>

Available actions:
  Search[query]      - Look up information
  Calculate[expr]    - Evaluate a math expression
  Lookup[term]       - Look up a definition or fact

When you have enough information, write:
  Final Answer: <your answer>

Question: {question}

Thought 1:
"""

# ------------------------------------------------------------------
# Simulated ReAct Agent (without API)
# ------------------------------------------------------------------
# This demonstrates the loop structure a ReAct agent uses.

class SimulatedToolbox:
    """Simulated tools for demonstration purposes."""

    @staticmethod
    def search(query: str) -> str:
        knowledge_base = {
            "capital of france": "The capital of France is Paris.",
            "population of paris": "Paris has a population of approximately 2.1 million in the city proper.",
            "eiffel tower height": "The Eiffel Tower is 330 meters tall.",
        }
        query_lower = query.lower()
        for key, value in knowledge_base.items():
            if key in query_lower:
                return value
        return f"No result found for: {query}"

    @staticmethod
    def calculate(expression: str) -> str:
        try:
            result = eval(expression, {"__builtins__": {}}, {})
            return str(result)
        except Exception as e:
            return f"Calculation error: {e}"


def simulate_react_step(thought: str, action_type: str, query: str, tools: SimulatedToolbox) -> str:
    """Execute one ReAct step."""
    print(f"  Thought: {thought}")
    print(f"  Action:  {action_type}[{query}]")

    if action_type.lower() == "search":
        observation = tools.search(query)
    elif action_type.lower() == "calculate":
        observation = tools.calculate(query)
    else:
        observation = f"Unknown action: {action_type}"

    print(f"  Observation: {observation}\n")
    return observation


print("=== ReAct Prompting Examples ===\n")

print("--- Example 1: Factual Multi-Step Question ---")
print(react_example_1)

print("--- Example 2: Calculation Task ---")
print(react_example_2)

print("--- Example 3: ReAct Prompt Template ---")
print(react_prompt_template.format(question="What is the height of the Eiffel Tower in feet?"))

print("--- Simulated ReAct Agent Demo ---")
tools = SimulatedToolbox()
print("Question: What is the capital of France and its population?\n")
obs1 = simulate_react_step(
    "I need to find the capital of France.",
    "Search", "capital of France", tools
)
obs2 = simulate_react_step(
    "Now I need the population of Paris.",
    "Search", "population of Paris", tools
)
print("  Final Answer: The capital of France is Paris, with a city population of approximately 2.1 million.")

# ------------------------------------------------------------------
# HOW TO USE WITH AN LLM API (OpenAI example)
# ------------------------------------------------------------------
# Uncomment and install: pip install openai
#
# import openai
# import re
# openai.api_key = "YOUR_API_KEY"
#
# def react_agent(question: str, max_steps: int = 6) -> str:
#     messages = [{"role": "user", "content": react_prompt_template.format(question=question)}]
#     tools = SimulatedToolbox()
#
#     for step in range(max_steps):
#         response = openai.chat.completions.create(
#             model="gpt-4o-mini",
#             messages=messages,
#             stop=["Observation"]
#         )
#         text = response.choices[0].message.content
#         print(text)
#
#         if "Final Answer:" in text:
#             break
#
#         # Parse action
#         action_match = re.search(r"Action \d+: (\w+)\[(.+?)\]", text)
#         if action_match:
#             action_type = action_match.group(1)
#             query = action_match.group(2)
#             if action_type == "Search":
#                 observation = tools.search(query)
#             elif action_type == "Calculate":
#                 observation = tools.calculate(query)
#             else:
#                 observation = "Unknown action"
#             observation_text = f"\nObservation {step+1}: {observation}\n"
#             print(observation_text)
#             messages.append({"role": "assistant", "content": text})
#             messages.append({"role": "user", "content": observation_text})
#
# react_agent("What is 15% tip on a $85 restaurant bill?")

# ------------------------------------------------------------------
# STUDENT EXERCISE
# ------------------------------------------------------------------
# Write a ReAct trace (Thought/Action/Observation) for the question:
# "How many days are between January 15th and March 20th of the same year?"
#
# Use the format shown in the examples above.

my_react_trace = """
Question: How many days are between January 15th and March 20th of the same year?

Thought 1: <your reasoning>
Action 1: <action type>[<query>]
Observation 1: <result>

Thought 2: <your reasoning>
...

Final Answer: <answer>
"""
