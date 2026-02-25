# Prompting for Students 🎓

A hands-on educational resource covering **10 essential LLM prompting techniques** — from beginner to advanced — with clear explanations, real examples, and student exercises.

---

## 📚 What is Prompting?

**Prompting** is the art of communicating with a Large Language Model (LLM) to get useful, accurate, and well-formatted responses. The way you phrase your input dramatically affects the quality of the output. Learning prompting techniques is a core skill for anyone working with AI tools.

---

## 🗂️ Repository Structure

```
Prompting-for-the-Students/
│
├── README.md
├── requirements.txt
│
└── prompting_techniques/
    ├── 01_zero_shot_prompting.py
    ├── 02_few_shot_prompting.py
    ├── 03_chain_of_thought_prompting.py
    ├── 04_role_prompting.py
    ├── 05_instruction_prompting.py
    ├── 06_self_consistency_prompting.py
    ├── 07_prompt_chaining.py
    ├── 08_tree_of_thought_prompting.py
    ├── 09_generated_knowledge_prompting.py
    └── 10_react_prompting.py
```

---

## 🧠 Prompting Techniques Covered

| # | Technique | Difficulty | Best For |
|---|-----------|------------|----------|
| 1 | [Zero-Shot Prompting](#1-zero-shot-prompting) | ⭐ Beginner | Quick tasks, Q&A, translation |
| 2 | [Few-Shot Prompting](#2-few-shot-prompting) | ⭐ Beginner | Custom formats, classification |
| 3 | [Chain-of-Thought (CoT)](#3-chain-of-thought-cot-prompting) | ⭐⭐ Intermediate | Math, logic, reasoning |
| 4 | [Role / Persona Prompting](#4-role--persona-prompting) | ⭐ Beginner | Expert answers, tutoring |
| 5 | [Instruction Prompting](#5-instruction-prompting) | ⭐ Beginner | Formatting, tone control |
| 6 | [Self-Consistency](#6-self-consistency-prompting) | ⭐⭐⭐ Advanced | High-accuracy reasoning |
| 7 | [Prompt Chaining](#7-prompt-chaining) | ⭐⭐ Intermediate | Multi-step workflows |
| 8 | [Tree-of-Thought (ToT)](#8-tree-of-thought-tot-prompting) | ⭐⭐⭐ Advanced | Complex planning, puzzles |
| 9 | [Generated Knowledge](#9-generated-knowledge-prompting) | ⭐⭐ Intermediate | Fact-grounded answers |
| 10 | [ReAct](#10-react-prompting-reasoning--acting) | ⭐⭐⭐ Advanced | AI agents, tool use |

---

## 🚀 Getting Started

```bash
# Clone the repository
git clone https://github.com/reddyprasade/Prompting-for-the-Students.git
cd Prompting-for-the-Students

# (Optional) Install dependencies to run with a real LLM API
pip install -r requirements.txt

# Run any technique file to see the example prompts printed
python prompting_techniques/01_zero_shot_prompting.py
python prompting_techniques/03_chain_of_thought_prompting.py
```

> **Note:** All files run without an API key and print the prompt examples to the console.
> To get actual LLM responses, uncomment the API sections and add your `OPENAI_API_KEY`.

---

## 📖 Technique Summaries

### 1. Zero-Shot Prompting
**File:** `01_zero_shot_prompting.py`

Give the model a task with **no examples** — just a clear instruction.

```
Classify the sentiment of this review as Positive, Negative, or Neutral.

Review: "The battery life is amazing but the camera quality is disappointing."

Sentiment:
```

---

### 2. Few-Shot Prompting
**File:** `02_few_shot_prompting.py`

Provide **2–5 input/output examples** before the actual task so the model learns the pattern.

```
Review: "Best purchase ever!"  → Category: LOVE
Review: "Broke after one day." → Category: HATE
Review: "Decent product."      → Category:
```

---

### 3. Chain-of-Thought (CoT) Prompting
**File:** `03_chain_of_thought_prompting.py`

Encourage the model to **reason step by step** before giving a final answer.

```
A bakery makes 120 cookies in the morning and 80 in the afternoon.
They sell 75 cookies. How many are left?

Let's think step by step.
```

---

### 4. Role / Persona Prompting
**File:** `04_role_prompting.py`

Assign a **role or identity** to the model to shape its tone, style, and expertise level.

```
You are an experienced data scientist.
Explain overfitting to a beginner using a real-world analogy.
```

---

### 5. Instruction Prompting
**File:** `05_instruction_prompting.py`

Write **precise, explicit instructions** including format, tone, length, and constraints.

```
Extract name, age, city, and occupation from the text.
Return as a valid JSON object. No explanation — only JSON.

Text: "Hi, I'm Sarah, 28, software engineer in San Francisco."
```

---

### 6. Self-Consistency Prompting
**File:** `06_self_consistency_prompting.py`

Generate **multiple reasoning paths** (run the prompt N times) then take a **majority vote** for the final answer.

```
Run prompt 5 times → ["$5.75", "$5.75", "$5.75", "$5.50", "$5.75"]
                                                    ↑ error
Majority vote → Final Answer: $5.75 ✅
```

---

### 7. Prompt Chaining
**File:** `07_prompt_chaining.py`

Break complex tasks into a **sequence of smaller prompts** where each output feeds into the next.

```
Prompt 1: Generate outline    → Outline
Prompt 2: Write introduction  → Introduction (uses Outline)
Prompt 3: Create SEO title    → Title + Meta (uses Introduction)
```

---

### 8. Tree-of-Thought (ToT) Prompting
**File:** `08_tree_of_thought_prompting.py`

Explore **multiple reasoning branches simultaneously**, evaluate them, and converge on the best solution.

```
Imagine 3 experts solving the problem:
  Expert 1: [approach A] ...
  Expert 2: [approach B] ...
  Expert 3: [approach C] ...
[Evaluation → Best approach wins]
```

---

### 9. Generated Knowledge Prompting
**File:** `09_generated_knowledge_prompting.py`

First generate **relevant background facts**, then use those facts as grounding context to answer the real question.

```
Step 1: "Generate 5 facts about photosynthesis."
Step 2: "Using these facts: [facts] → Why are plants green?"
```

---

### 10. ReAct Prompting (Reasoning + Acting)
**File:** `10_react_prompting.py`

Interleave **reasoning traces with tool actions** in a loop — the foundation of AI agents.

```
Thought 1: I need to find the capital of France.
Action 1:  Search[capital of France]
Observation 1: Paris

Thought 2: Now I need the population.
Action 2:  Search[population of Paris]
Observation 2: ~2.1 million

Final Answer: Paris, ~2.1 million
```

---

## 💡 Tips for Better Prompting

1. **Be specific** — vague prompts get vague answers.
2. **Specify the format** — tell the model if you want JSON, bullet points, a table, etc.
3. **Set the context** — background information helps the model reason better.
4. **Use examples** — few-shot examples dramatically improve output quality.
5. **Iterate** — if the first prompt doesn't work, refine it.
6. **Control the length** — tell the model how long the response should be.
7. **Add constraints** — "Do not include X" is as powerful as "Include Y".

---

## 🔗 Further Reading

- [Prompt Engineering Guide](https://www.promptingguide.ai/)
- [OpenAI Prompt Engineering](https://platform.openai.com/docs/guides/prompt-engineering)
- [Chain-of-Thought Prompting Elicits Reasoning in LLMs (Wei et al., 2022)](https://arxiv.org/abs/2201.11903)
- [Tree of Thoughts (Yao et al., 2023)](https://arxiv.org/abs/2305.10601)
- [ReAct: Synergizing Reasoning and Acting (Yao et al., 2022)](https://arxiv.org/abs/2210.03629)
- [Self-Consistency (Wang et al., 2022)](https://arxiv.org/abs/2203.11171)

---

## 🤝 Contributing

Found an error or want to add a new technique? Feel free to open an issue or submit a pull request!

---

## 📄 License

This project is licensed under the [Apache License 2.0](LICENSE).
