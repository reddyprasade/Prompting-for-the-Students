# Self-Consistency Prompting

## What is Self-Consistency Prompting?

Self-consistency prompting is an enhancement over standard Chain-of-Thought (CoT) prompting. Instead of generating **one** reasoning path, the model is asked to generate **multiple diverse reasoning paths** for the same question. The final answer is determined by **majority vote** — the answer that appears most often across all reasoning paths is selected.

This technique was introduced by Wang et al. (2022) and consistently outperforms single-path CoT on a range of reasoning benchmarks.

> **Key Idea:** If multiple independent lines of reasoning all reach the same answer, that answer is much more likely to be correct.

---

## When to Use Self-Consistency Prompting

- Tasks where a **single CoT output** is unreliable or inconsistent.
- High-stakes reasoning tasks where **accuracy is critical**.
- Arithmetic, commonsense, and symbolic reasoning problems.
- When you can afford **multiple API calls** (it's more expensive).

---

## How It Works

```
Step 1: Write a CoT-style prompt for the question.
Step 2: Sample N different reasoning paths (e.g., N = 5 or 10).
Step 3: Extract the final answer from each path.
Step 4: Take the majority vote as the final answer.
```

---

## Example

### Question
> A factory produces 120 units per day. Due to a new machine, production increases by 25%. How many units are produced per day after the increase?

---

### Reasoning Path 1
```
Original production = 120 units/day.
Increase = 25% of 120 = 0.25 × 120 = 30 units.
New production = 120 + 30 = 150 units/day.
Answer: 150
```

### Reasoning Path 2
```
25% increase means the new rate is 125% of the original.
125% of 120 = 1.25 × 120 = 150.
Answer: 150
```

### Reasoning Path 3
```
Each 10% of 120 = 12 units.
25% = 2 × 12 + 0.5 × 12 = 24 + 6 = 30 units.
New total = 120 + 30 = 150.
Answer: 150
```

### Reasoning Path 4
```
I need to find 25% more than 120.
25% = 1/4. One quarter of 120 = 30.
120 + 30 = 150.
Answer: 150
```

### Reasoning Path 5
```
Percentage increase formula: new = old × (1 + rate/100)
new = 120 × (1 + 25/100) = 120 × 1.25 = 150
Answer: 150
```

### Majority Vote
| Path | Answer |
|------|--------|
| Path 1 | 150 ✅ |
| Path 2 | 150 ✅ |
| Path 3 | 150 ✅ |
| Path 4 | 150 ✅ |
| Path 5 | 150 ✅ |

**Final Answer: 150** (5/5 votes)

---

## Example with a Harder Question (where paths may diverge)

### Question
> If it takes 5 machines 5 minutes to make 5 widgets, how long does it take 100 machines to make 100 widgets?

### Reasoning Path 1 (Correct)
```
5 machines make 5 widgets in 5 minutes.
So 1 machine makes 1 widget in 5 minutes.
100 machines each make 1 widget in 5 minutes → 100 widgets in 5 minutes.
Answer: 5
```

### Reasoning Path 2 (Incorrect — proportional error)
```
5 machines → 100 machines is 20× more machines.
5 widgets → 100 widgets is 20× more widgets.
The 20× factors cancel, so time stays the same: 5 minutes.
Answer: 5
```

### Reasoning Path 3 (Correct)
```
Rate per machine = 1 widget per 5 minutes.
100 machines × 1 widget/5 min = 20 widgets/min.
To make 100 widgets: 100 / 20 = 5 minutes.
Answer: 5
```

### Majority Vote → **Final Answer: 5 minutes** ✅

---

## Tips for Effective Self-Consistency Prompting

| Tip | Why It Helps |
|-----|-------------|
| Use temperature > 0 when sampling paths | Encourages diverse reasoning approaches |
| Sample at least 5 paths for reliable results | More votes = more robust majority |
| Extract answers consistently (e.g., "Answer: X") | Makes aggregation easier |
| Use majority vote, not average | Works for both numerical and categorical answers |
| Combine with few-shot CoT examples | Grounds the reasoning style |

---

## Advantages

- ✅ More accurate than single-path CoT on difficult reasoning tasks.
- ✅ Robust to occasional reasoning errors in individual paths.
- ✅ No additional training or fine-tuning needed.
- ✅ Easy to implement — run the same prompt N times.

## Limitations

- ❌ **Expensive** — requires N times more API calls.
- ❌ Slower than single-pass methods.
- ❌ If the model consistently makes the same systematic error, majority vote will still be wrong.
- ❌ Overkill for simple tasks.

---

## Comparison with Related Techniques

| Technique | Reasoning Paths | Aggregation | Best For |
|-----------|:--------------:|:-----------:|----------|
| Chain-of-Thought | 1 | None | General reasoning |
| Self-Consistency | N (multiple) | Majority vote | High-accuracy reasoning |
| Tree of Thoughts | Branching tree | Best path search | Exploration-heavy tasks |

---

## Further Reading

- Wang et al. (2022) — *Self-Consistency Improves Chain of Thought Reasoning in Language Models*
- [OpenAI Prompt Engineering Guide](https://platform.openai.com/docs/guides/prompt-engineering)
