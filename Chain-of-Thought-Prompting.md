# Chain-of-Thought (CoT) Prompting

## What is Chain-of-Thought Prompting?

Chain-of-Thought (CoT) prompting is a technique where the model is encouraged to **show its intermediate reasoning steps** before producing a final answer. Instead of jumping straight to an answer, the model "thinks out loud", breaking a complex problem into smaller, manageable sub-steps.

This approach was introduced by Wei et al. (2022) and significantly improves performance on tasks that require **arithmetic reasoning, commonsense reasoning, and multi-step logic**.

---

## When to Use Chain-of-Thought Prompting

- Tasks requiring **multi-step arithmetic** (e.g., word problems).
- Tasks requiring **logical deduction** (e.g., if-then reasoning).
- Tasks requiring **commonsense reasoning** (e.g., cause-and-effect).
- Any complex problem where intermediate steps matter.

---

## Two Variants

### 1. Few-Shot CoT
Provide examples that include step-by-step reasoning before the answer.

### 2. Zero-Shot CoT
Add the phrase **"Let's think step by step."** to the prompt — no examples needed.

---

## Basic Structure (Few-Shot CoT)

```
[Question 1]
[Step-by-step reasoning for Question 1]
Answer: [Answer 1]

[Question 2]
[Step-by-step reasoning for Question 2]
Answer: [Answer 2]

[New Question]
```

---

## Examples

### Example 1 — Few-Shot CoT (Arithmetic)

**Prompt:**
```
Q: Roger has 5 tennis balls. He buys 2 more cans of tennis balls.
Each can has 3 tennis balls. How many tennis balls does he have now?

A: Roger starts with 5 tennis balls.
   He buys 2 cans × 3 balls = 6 new tennis balls.
   Total = 5 + 6 = 11 tennis balls.
   The answer is 11.

Q: The cafeteria had 23 apples. If they used 20 to make lunch and
bought 6 more, how many apples do they have?

A:
```

**Model Output:**
```
The cafeteria started with 23 apples.
They used 20, so 23 - 20 = 3 apples remained.
Then they bought 6 more: 3 + 6 = 9 apples.
The answer is 9.
```

---

### Example 2 — Zero-Shot CoT

**Prompt:**
```
A store sells shirts for $15 each. If you buy 3 or more, you get a 20% discount.
Maria buys 4 shirts. How much does she pay in total?

Let's think step by step.
```

**Model Output:**
```
Step 1: Price per shirt = $15.
Step 2: Maria buys 4 shirts, which qualifies for the 20% discount.
Step 3: Discount amount = 20% of $15 = $3 per shirt.
Step 4: Discounted price per shirt = $15 - $3 = $12.
Step 5: Total cost = 4 × $12 = $48.
Maria pays $48 in total.
```

---

### Example 3 — Logical Reasoning

**Prompt:**
```
Q: All mammals are warm-blooded. Dolphins are mammals.
Are dolphins warm-blooded? Explain your reasoning.

A: Let's think step by step.
   Premise 1: All mammals are warm-blooded.
   Premise 2: Dolphins are mammals.
   Conclusion: Therefore, dolphins must be warm-blooded.
   The answer is Yes.

Q: All birds have wings. Penguins are birds. Can penguins fly?
Explain your reasoning.

A:
```

**Model Output:**
```
Let's think step by step.
Premise 1: All birds have wings.
Premise 2: Penguins are birds.
Therefore, penguins have wings.
However, having wings does not necessarily mean a bird can fly.
Penguins have wings adapted for swimming, not flight.
The answer is No, penguins cannot fly.
```

---

### Example 4 — Commonsense Reasoning

**Prompt:**
```
Q: If I put a wet umbrella inside a closed bag, what happens to the bag?

Let's think step by step.
```

**Model Output:**
```
Step 1: The umbrella is wet, meaning it contains moisture/water.
Step 2: Placing it inside a closed bag traps the moisture inside.
Step 3: With no airflow, the moisture cannot evaporate.
Step 4: The inside of the bag will become damp/wet.
The bag will get wet and humid on the inside.
```

---

## Tips for Effective CoT Prompting

| Tip | Why It Helps |
|-----|-------------|
| Use "Let's think step by step" for zero-shot CoT | Triggers the reasoning mode |
| Show clear, correct reasoning in few-shot examples | Model mimics the demonstrated structure |
| Break complex problems into numbered steps | Keeps reasoning organised and traceable |
| Ask for the final answer explicitly at the end | Prevents the model from stopping mid-reasoning |
| Use CoT for problems with multiple steps | Overhead is not worth it for trivial questions |

---

## Advantages

- ✅ Significantly improves accuracy on reasoning tasks.
- ✅ Produces **interpretable** outputs — you can follow the reasoning.
- ✅ Works with zero-shot (just add "Let's think step by step").
- ✅ Helps detect where the model goes wrong (debugging reasoning).

## Limitations

- ❌ Longer outputs → higher token cost.
- ❌ Not necessary (and may hurt performance) for simple factual tasks.
- ❌ Model may produce plausible-sounding but **incorrect reasoning chains**.
- ❌ Effectiveness depends on model size — smaller models benefit less.

---

## Comparison with Other Techniques

| Technique | Examples | Reasoning Steps | Best For |
|-----------|:--------:|:---------------:|----------|
| Zero-Shot | 0 | No | Simple tasks |
| Few-Shot | 2–5+ | No | Format/style guidance |
| CoT (Few-Shot) | 2–5+ | Yes | Complex reasoning with examples |
| CoT (Zero-Shot) | 0 | Yes | Quick reasoning without examples |
| Self-Consistency | 0 or few | Yes (multiple paths) | High-accuracy reasoning |

---

## Further Reading

- Wei et al. (2022) — *Chain-of-Thought Prompting Elicits Reasoning in Large Language Models*
- Kojima et al. (2022) — *Large Language Models are Zero-Shot Reasoners*
- [OpenAI Prompt Engineering Guide](https://platform.openai.com/docs/guides/prompt-engineering)
