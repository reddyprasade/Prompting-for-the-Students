# Prompting for Students

A collection of beginner-friendly guides covering the most important **prompting techniques** for large language models (LLMs). Each technique is explained with clear definitions, worked examples, tips, and comparisons.

---

## 📚 Prompting Techniques

| # | Technique | Description | File |
|---|-----------|-------------|------|
| 1 | **Zero-Shot Prompting** | Ask the model a task with no examples at all | [Zero-Shot-Prompting.md](./Zero-Shot-Prompting.md) |
| 2 | **Few-Shot Prompting** | Provide 2–5 input/output examples to guide the model | [Few-Shot-Prompting.md](./Few-Shot-Prompting.md) |
| 3 | **Chain-of-Thought (CoT)** | Encourage step-by-step reasoning before the final answer | [Chain-of-Thought-Prompting.md](./Chain-of-Thought-Prompting.md) |
| 4 | **Self-Consistency** | Generate multiple reasoning paths and take the majority vote | [Self-Consistency-Prompting.md](./Self-Consistency-Prompting.md) |
| 5 | **Tree of Thoughts (ToT)** | Explore branching reasoning paths, prune weak ones | [Tree-of-Thoughts-Prompting.md](./Tree-of-Thoughts-Prompting.md) |
| 6 | **ReAct Prompting** | Combine reasoning with external tool actions in a loop | [ReAct-Prompting.md](./ReAct-Prompting.md) |
| 7 | **Role Prompting** | Assign a persona or expert role to shape the model's response | [Role-Prompting.md](./Role-Prompting.md) |

---

## 🗺️ Quick Comparison

| Technique | Examples Needed | Reasoning | Tool Use | Best For |
|-----------|:--------------:|:---------:|:--------:|----------|
| Zero-Shot | ❌ | ❌ | ❌ | Simple, well-known tasks |
| Few-Shot | ✅ (2–5) | ❌ | ❌ | Format & style guidance |
| Chain-of-Thought | Optional | ✅ | ❌ | Multi-step reasoning |
| Self-Consistency | Optional | ✅ (multiple) | ❌ | High-accuracy reasoning |
| Tree of Thoughts | Optional | ✅ (branching) | ❌ | Planning & exploration |
| ReAct | Optional | ✅ | ✅ | Agentic, tool-augmented tasks |
| Role Prompting | ❌ | ❌ | ❌ | Tone, persona & domain focus |

---

## 🚀 Getting Started

If you are new to prompting, we recommend reading the guides in this order:

1. [Zero-Shot Prompting](./Zero-Shot-Prompting.md) — Start here to understand the basics.
2. [Few-Shot Prompting](./Few-Shot-Prompting.md) — Learn how examples improve results.
3. [Chain-of-Thought Prompting](./Chain-of-Thought-Prompting.md) — Unlock step-by-step reasoning.
4. [Self-Consistency Prompting](./Self-Consistency-Prompting.md) — Make reasoning more reliable.
5. [Tree of Thoughts Prompting](./Tree-of-Thoughts-Prompting.md) — Explore complex problem spaces.
6. [ReAct Prompting](./ReAct-Prompting.md) — Connect reasoning to real-world actions.
7. [Role Prompting](./Role-Prompting.md) — Shape the model's persona and style.
