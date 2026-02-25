# Tree of Thoughts (ToT) Prompting

## What is Tree of Thoughts Prompting?

Tree of Thoughts (ToT) prompting is an advanced prompting framework where the model **explores multiple reasoning branches** in a tree structure, evaluates each intermediate thought, and searches for the best solution path. Unlike Chain-of-Thought which follows a single linear path, ToT allows **backtracking and exploration** — much like a human who considers several ideas, discards weak ones, and pursues the most promising.

ToT was introduced by Yao et al. (2023) and is particularly useful for tasks that require **planning, search, and deliberate multi-step decision-making**.

> **Analogy:** CoT is like walking a straight road. ToT is like navigating a maze — you explore multiple routes and backtrack when you hit a dead end.

---

## When to Use Tree of Thoughts Prompting

- Problems requiring **strategic planning** (e.g., puzzles, games).
- Tasks with **multiple viable approaches** to explore.
- Creative writing where different story branches should be evaluated.
- Math problems where different solution strategies exist.
- Any task where "thinking ahead" and **backtracking** helps.

---

## How It Works

```
Step 1: Decompose the problem into a series of thought steps.
Step 2: Generate multiple candidate "thoughts" (branches) at each step.
Step 3: Evaluate each thought for promise (sure / maybe / impossible).
Step 4: Use search (BFS or DFS) to explore the most promising paths.
Step 5: Return the best complete solution found.
```

---

## ToT vs. CoT vs. Self-Consistency

```
CoT:               Q → t1 → t2 → t3 → Answer (single path)

Self-Consistency:  Q → [Path 1 → A1]
                     → [Path 2 → A2]   majority vote → Answer
                     → [Path 3 → A3]

Tree of Thoughts:  Q → t1a → t2a → t3a → ✅ Answer
                        ↓
                      t1b → t2b → ❌ Dead end (backtrack)
                        ↓
                      t1c → t2c → t3c → t4c → ✅ Better Answer
```

---

## Example — Creative Writing Planning

### Task
> Write the opening paragraph of a mystery novel set in a lighthouse.

### Step 1: Generate Opening Concepts (Branches)
```
Thought A: Start with the lighthouse keeper discovering a body.
Thought B: Start with a detective arriving at the lighthouse during a storm.
Thought C: Start with an anonymous letter that leads the protagonist to the lighthouse.
```

### Step 2: Evaluate Each Branch
```
Thought A — Rating: PROMISING
  Immediately hooks the reader with action and mystery.

Thought B — Rating: PROMISING
  Classic noir setup; storm adds atmosphere.

Thought C — Rating: LESS PROMISING
  Slower start; may lose the reader's attention.
```

### Step 3: Expand Promising Branches
```
Branch A → Keeper finds body → Was it murder? → Who had access?
Branch B → Detective arrives → Lighthouse is locked → Keeper is missing
```

### Step 4: Select Best Path and Generate Output
```
Selected: Branch B

Output:
"The storm had turned the coast into a wall of black water and white foam 
by the time Detective Clara Hayes reached the lighthouse. The iron door 
was bolted from the inside. The light above still turned, indifferent, 
sweeping its cold beam across the chaos below. But of Thomas Briggs, 
the keeper who had tended this tower for thirty years, there was no sign."
```

---

## Example — Puzzle Solving (Game of 24)

### Task
> Use the numbers 4, 8, 8, 2 with operations +, -, ×, ÷ to make 24.

### ToT Exploration
```
Branch 1: (4 + 8) × 2 = 24 ✅  → Evaluate: SURE → Output this solution.
Branch 2:  8 ÷ 8 + 4 = ... → Only reaches 5 → IMPOSSIBLE, prune.
Branch 3:  8 × 2 + 8 = 24 ✅  → Evaluate: SURE → Also valid.
```

**Final Answer:** `(4 + 8) × 2 = 24`

---

## Prompting Template for ToT

```
You are solving [problem]. Think through this step by step using
the Tree of Thoughts approach:

1. Generate 3 different initial approaches.
2. For each approach, rate it as: Promising / Neutral / Dead End.
3. Expand only the Promising approaches by one more step.
4. Continue until you reach a complete solution.
5. Present the best final answer.

Problem: [Insert problem here]
```

---

## Tips for Effective ToT Prompting

| Tip | Why It Helps |
|-----|-------------|
| Explicitly ask for multiple branches | Prevents the model collapsing to one path |
| Include evaluation criteria | Guides the pruning of poor branches |
| Use BFS for shallow wide problems | Explores breadth before depth |
| Use DFS for deep sequential problems | Finds one path quickly |
| Combine with a scoring rubric | Makes evaluation objective |

---

## Advantages

- ✅ Finds better solutions by exploring multiple paths.
- ✅ Can backtrack — avoids getting stuck on wrong approaches.
- ✅ Mirrors human deliberate thinking and planning.
- ✅ Especially powerful for creative and combinatorial tasks.

## Limitations

- ❌ **Most expensive** technique — many model calls needed.
- ❌ Requires careful prompt design for evaluation criteria.
- ❌ Overkill for simple or straightforward tasks.
- ❌ Challenging to implement without an orchestration framework.

---

## Comparison with Related Techniques

| Technique | Search Strategy | Cost | Best For |
|-----------|:--------------:|:----:|----------|
| Chain-of-Thought | Single path | Low | Linear reasoning |
| Self-Consistency | Parallel paths + vote | Medium | Robust answers |
| Tree of Thoughts | Tree + pruning | High | Planning & exploration |
| ReAct | Act → Observe loop | Medium | Tool-use & agentic tasks |

---

## Further Reading

- Yao et al. (2023) — *Tree of Thoughts: Deliberate Problem Solving with Large Language Models*
- Long (2023) — *Large Language Model Guided Tree-of-Thought*
- [Princeton NLP ToT Repository](https://github.com/princeton-nlp/tree-of-thought-llm)
