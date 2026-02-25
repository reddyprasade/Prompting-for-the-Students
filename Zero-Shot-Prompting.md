# Zero-Shot Prompting

## What is Zero-Shot Prompting?

Zero-shot prompting is a technique where you ask a large language model (LLM) to perform a task **without providing any examples**. The model relies entirely on its pre-trained knowledge and the clarity of your instruction to generate a response.

The term "zero-shot" means **zero examples** are given — you simply describe the task and let the model figure out how to complete it.

---

## When to Use Zero-Shot Prompting

- When you need a **quick answer** without crafting example pairs.
- When the task is **simple or well-known** (e.g., translation, summarisation, classification).
- When you want to test the model's **baseline capability** on a task.

---

## Basic Structure

```
[Instruction / Task Description]

[Input (optional)]
```

---

## Examples

### Example 1 — Sentiment Classification

**Prompt:**
```
Classify the sentiment of the following sentence as Positive, Negative, or Neutral.

Sentence: "I absolutely loved the movie; the storyline was gripping!"
```

**Model Output:**
```
Positive
```

---

### Example 2 — Language Translation

**Prompt:**
```
Translate the following English sentence into French.

Sentence: "The weather is beautiful today."
```

**Model Output:**
```
"Le temps est magnifique aujourd'hui."
```

---

### Example 3 — Text Summarisation

**Prompt:**
```
Summarise the following paragraph in one sentence.

Paragraph: "Artificial intelligence (AI) is intelligence demonstrated by machines,
as opposed to natural intelligence displayed by animals including humans.
AI research has been defined as the field of study of intelligent agents,
which refers to any system that perceives its environment and takes actions
that maximise its chance of achieving its goals."
```

**Model Output:**
```
Artificial intelligence refers to machine-demonstrated intelligence aimed at
building systems that perceive their environment and act to achieve their goals.
```

---

### Example 4 — Question Answering

**Prompt:**
```
Answer the following question.

Question: What is the capital of Japan?
```

**Model Output:**
```
The capital of Japan is Tokyo.
```

---

## Tips for Effective Zero-Shot Prompting

| Tip | Why It Helps |
|-----|-------------|
| Be specific and clear in your instruction | Reduces ambiguity |
| State the desired output format | Guides the model's response style |
| Use action verbs (Classify, Summarise, Translate) | Makes the task unambiguous |
| Provide context when needed | Helps the model ground its answer |

---

## Advantages

- ✅ Simple and fast — no need to write examples.
- ✅ Works well for common tasks the model has seen during training.
- ✅ Reduces prompt length.

## Limitations

- ❌ May produce incorrect or vague answers for complex or niche tasks.
- ❌ Model behaviour can be inconsistent without guiding examples.
- ❌ Less effective than few-shot or chain-of-thought for reasoning-heavy tasks.

---

## Comparison with Other Techniques

| Technique | Examples Provided | Reasoning Steps | Best For |
|-----------|:-----------------:|:---------------:|----------|
| Zero-Shot | 0 | No | Simple, well-known tasks |
| Few-Shot | 2–5+ | No | Tasks needing style/format guidance |
| Chain-of-Thought | 0 or few | Yes | Multi-step reasoning tasks |

---

## Further Reading

- [OpenAI Prompt Engineering Guide](https://platform.openai.com/docs/guides/prompt-engineering)
- Brown et al. (2020) — *Language Models are Few-Shot Learners* (GPT-3 paper)
