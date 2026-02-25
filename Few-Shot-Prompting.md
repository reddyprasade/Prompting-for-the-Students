# Few-Shot Prompting

## What is Few-Shot Prompting?

Few-shot prompting is a technique where you provide the model with **a small number of input–output examples** (called "shots") inside the prompt before presenting the actual task. These examples act as demonstrations, teaching the model the desired format, style, or reasoning pattern without any weight updates or fine-tuning.

- **1 example** = One-shot prompting  
- **2–5+ examples** = Few-shot prompting  
- **0 examples** = Zero-shot prompting  

---

## When to Use Few-Shot Prompting

- When the task has a **specific output format** you want the model to follow.
- When zero-shot results are **inconsistent or inaccurate**.
- When you need the model to **mimic a particular style or tone**.
- When working with **custom classification labels** the model may not know natively.

---

## Basic Structure

```
[Example 1 Input] → [Example 1 Output]
[Example 2 Input] → [Example 2 Output]
[Example 3 Input] → [Example 3 Output]

[Actual Input] → ?
```

---

## Examples

### Example 1 — Sentiment Classification

**Prompt:**
```
Classify each sentence as Positive, Negative, or Neutral.

Sentence: "I love this product, it works perfectly!"
Sentiment: Positive

Sentence: "The service was terrible and slow."
Sentiment: Negative

Sentence: "The package arrived on Tuesday."
Sentiment: Neutral

Sentence: "This is the worst experience I have ever had."
Sentiment:
```

**Model Output:**
```
Negative
```

---

### Example 2 — Named Entity Recognition

**Prompt:**
```
Extract the person's name and city from each sentence.

Sentence: "Alice moved to Paris last year."
Name: Alice | City: Paris

Sentence: "Bob is visiting Tokyo for a conference."
Name: Bob | City: Tokyo

Sentence: "Maria just arrived in New York for her new job."
Name:
```

**Model Output:**
```
Name: Maria | City: New York
```

---

### Example 3 — Text Style Transfer

**Prompt:**
```
Rewrite each formal sentence in a casual, friendly tone.

Formal: "We regret to inform you that your application has been unsuccessful."
Casual: "Hey, sorry to say your application didn't make it through this time."

Formal: "Please be advised that the meeting has been rescheduled to Thursday."
Casual: "Just a heads-up — the meeting has been moved to Thursday."

Formal: "We would like to express our gratitude for your continued patronage."
Casual:
```

**Model Output:**
```
"Thanks so much for sticking with us — we really appreciate it!"
```

---

### Example 4 — Arithmetic Word Problems

**Prompt:**
```
Solve the word problem and provide only the numerical answer.

Problem: "Sara has 8 apples. She gives 3 to her friend. How many does she have left?"
Answer: 5

Problem: "A train travels 60 km/h for 2 hours. How far does it travel?"
Answer: 120

Problem: "There are 5 shelves with 12 books each. How many books in total?"
Answer:
```

**Model Output:**
```
60
```

---

## Tips for Effective Few-Shot Prompting

| Tip | Why It Helps |
|-----|-------------|
| Use 2–5 diverse, representative examples | Covers different patterns and edge cases |
| Keep examples consistent in format | Reduces confusion about output structure |
| Place the actual query last | Follows the natural demonstration → question order |
| Choose high-quality, unambiguous examples | Garbage in, garbage out |
| Match example difficulty to real task | Avoids misleading the model |

---

## Advantages

- ✅ More accurate than zero-shot for complex or format-sensitive tasks.
- ✅ No model fine-tuning required.
- ✅ Quickly adaptable to new tasks just by swapping examples.

## Limitations

- ❌ Longer prompts consume more tokens (higher cost).
- ❌ Performance depends heavily on the quality of chosen examples.
- ❌ May not generalise well if examples are not representative.
- ❌ Context window limits how many examples can be provided.

---

## Comparison with Other Techniques

| Technique | Examples Provided | Reasoning Steps | Best For |
|-----------|:-----------------:|:---------------:|----------|
| Zero-Shot | 0 | No | Simple, well-known tasks |
| Few-Shot | 2–5+ | No | Tasks needing style/format guidance |
| Chain-of-Thought | 0 or few | Yes | Multi-step reasoning tasks |

---

## Further Reading

- Brown et al. (2020) — *Language Models are Few-Shot Learners* (GPT-3 paper)
- [OpenAI Prompt Engineering Guide](https://platform.openai.com/docs/guides/prompt-engineering)
