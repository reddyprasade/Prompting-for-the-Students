# ReAct Prompting

## What is ReAct Prompting?

ReAct (short for **Re**asoning + **Act**ing) is a prompting technique that combines **chain-of-thought reasoning** with **action-taking** in an interleaved loop. The model alternates between:

1. **Thought** — Internal reasoning about what to do next.
2. **Action** — Calling an external tool (e.g., search engine, calculator, code executor, database).
3. **Observation** — The result returned by the tool.

This loop continues until the model has enough information to give a final answer.

ReAct was introduced by Yao et al. (2022) and is the foundation for many modern **AI agent frameworks** (LangChain, AutoGPT, etc.).

---

## When to Use ReAct Prompting

- Tasks requiring **up-to-date information** (e.g., current news, stock prices).
- Tasks requiring **tool use** (calculators, search engines, APIs, databases).
- Multi-step tasks where **intermediate results** are needed.
- Building **autonomous AI agents** that interact with the environment.

---

## The ReAct Loop

```
Question → Thought → Action → Observation → Thought → Action → Observation → ... → Answer
```

```
Thought:      "I need to find the current price of gold."
Action:       Search("current gold price per ounce 2024")
Observation:  "Gold is trading at $2,340 per troy ounce."
Thought:      "Now I have the price. I can answer the question."
Answer:       "The current gold price is approximately $2,340 per troy ounce."
```

---

## Available Action Types (Common)

| Action | Description |
|--------|-------------|
| `Search(query)` | Search the web for information |
| `Lookup(term)` | Look up a term on the current page |
| `Calculate(expression)` | Evaluate a mathematical expression |
| `ReadFile(path)` | Read a file from the filesystem |
| `RunCode(code)` | Execute a snippet of code |
| `Finish(answer)` | Return the final answer |

---

## Example 1 — Factual Question with Web Search

**Question:** What is the population of Australia, and what is 10% of that number?

```
Thought 1: I need to find the current population of Australia.
Action 1:  Search("current population of Australia 2024")
Observation 1: Australia's population is approximately 26.5 million people (2024).

Thought 2: Now I need to calculate 10% of 26.5 million.
Action 2:  Calculate(26500000 * 0.10)
Observation 2: 2,650,000

Thought 3: I now have both pieces of information to answer the question.
Action 3:  Finish("Australia's population is approximately 26.5 million.
            10% of that is 2,650,000 people.")
```

**Final Answer:** Australia's population is approximately 26.5 million. 10% of that is 2,650,000 people.

---

## Example 2 — Multi-Step Research Task

**Question:** Who directed the highest-grossing film of 2023, and what other movies has that director made?

```
Thought 1: I need to find out what the highest-grossing film of 2023 was.
Action 1:  Search("highest grossing film worldwide 2023")
Observation 1: The highest-grossing film of 2023 was "Barbie", grossing over $1.4 billion.

Thought 2: Now I need to find out who directed Barbie.
Action 2:  Search("Barbie 2023 film director")
Observation 2: "Barbie" (2023) was directed by Greta Gerwig.

Thought 3: Now I need to find other movies directed by Greta Gerwig.
Action 3:  Search("Greta Gerwig filmography as director")
Observation 3: Greta Gerwig has directed: Lady Bird (2017), Little Women (2019), Barbie (2023).

Thought 4: I have all the information needed.
Action 4:  Finish("The highest-grossing film of 2023 was Barbie, directed by Greta Gerwig.
            She has also directed Lady Bird (2017) and Little Women (2019).")
```

---

## Example 3 — Code Execution Task

**Question:** What is the square root of the sum of the first 10 perfect squares?

```
Thought 1: I need to compute the sum of the first 10 perfect squares (1²+2²+...+10²).
Action 1:  RunCode("import math; total = sum(i**2 for i in range(1, 11)); print(total)")
Observation 1: 385

Thought 2: Now I need to compute the square root of 385.
Action 2:  RunCode("import math; print(round(math.sqrt(385), 4))")
Observation 2: 19.6214

Thought 3: I have the answer.
Action 3:  Finish("The sum of the first 10 perfect squares is 385.
            Its square root is approximately 19.6214.")
```

---

## ReAct Prompt Template

```
Solve the following problem step by step.
Use the following format:

Thought: [Your internal reasoning]
Action: [The tool to call and its input]
Observation: [The result of the action]
... (Repeat Thought/Action/Observation as needed)
Thought: [Final reasoning]
Answer: [Your final answer]

Available tools: Search, Calculate, Finish

Question: [Insert question here]
```

---

## Tips for Effective ReAct Prompting

| Tip | Why It Helps |
|-----|-------------|
| Clearly define available actions | Model knows what tools it can use |
| Always include a `Finish` action | Signals when to stop the loop |
| Use specific action formats (e.g., `Search("query")`) | Makes parsing easier |
| Keep observations concise | Prevents context window overflow |
| Limit maximum steps | Prevents infinite reasoning loops |

---

## Advantages

- ✅ Enables the model to access **real-time, up-to-date information**.
- ✅ Handles **complex multi-step tasks** that require external tools.
- ✅ Reasoning is **transparent and auditable** (every thought is shown).
- ✅ Foundation of modern **agentic AI systems**.

## Limitations

- ❌ Requires access to **external tool integrations**.
- ❌ More complex to implement than standard prompting.
- ❌ Can be **slow** due to multiple tool calls.
- ❌ Model may hallucinate observations if tools are not truly connected.

---

## Comparison with Related Techniques

| Technique | Uses Tools | Reasoning | Best For |
|-----------|:----------:|:---------:|----------|
| Chain-of-Thought | No | Yes | Static reasoning |
| ReAct | Yes | Yes | Dynamic, tool-augmented tasks |
| Tree of Thoughts | No | Yes (branching) | Planning & exploration |

---

## Further Reading

- Yao et al. (2022) — *ReAct: Synergizing Reasoning and Acting in Language Models*
- [LangChain ReAct Agent Documentation](https://python.langchain.com/docs/modules/agents/agent_types/react)
- [OpenAI Function Calling](https://platform.openai.com/docs/guides/function-calling)
