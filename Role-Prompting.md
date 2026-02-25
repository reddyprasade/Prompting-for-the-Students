# Role Prompting

## What is Role Prompting?

Role prompting (also called **persona prompting**) is a technique where you assign a **specific identity, role, or persona** to the language model before asking it a question. By telling the model "You are an expert X", you prime it to respond with the tone, vocabulary, depth, and style appropriate for that role.

This is one of the simplest yet most effective prompting techniques for shaping the **quality, tone, and focus** of model outputs.

---

## When to Use Role Prompting

- When you need **domain-specific expertise** (e.g., medical, legal, coding).
- When you want a **specific communication style** (e.g., teacher, coach, critic).
- When building **interactive agents or chatbots** with a defined personality.
- When you want the model to **adopt a perspective** for debate or analysis.

---

## Basic Structure

```
You are [role/persona]. [Additional context about the role.]

[Your question or task]
```

---

## Examples

### Example 1 — Expert Explainer

**Without Role Prompting:**
```
Prompt: What is machine learning?
Output: Machine learning is a type of artificial intelligence that allows systems 
        to learn from data...
```

**With Role Prompting:**
```
Prompt: You are a university professor specialising in artificial intelligence, 
        explaining concepts to first-year students. Use simple analogies and 
        avoid heavy jargon.
        
        What is machine learning?

Output: Think of machine learning like teaching a child to recognise cats.
        You don't give the child a rulebook that says "cats have four legs, 
        pointed ears, and whiskers." Instead, you show them hundreds of photos 
        of cats and dogs. Over time, the child's brain learns the patterns on 
        its own. Machine learning works the same way — instead of a child's 
        brain, we use algorithms; instead of photos, we use data.
```

---

### Example 2 — Code Reviewer

**Prompt:**
```
You are a senior software engineer with 15 years of experience in Python.
Your job is to review code for correctness, readability, and efficiency.
Be concise but specific in your feedback.

Review the following code:

def find_max(numbers):
    max_val = 0
    for num in numbers:
        if num > max_val:
            max_val = num
    return max_val
```

**Model Output:**
```
Issues found:

1. Bug — Incorrect initial value:
   Setting max_val = 0 fails for lists containing only negative numbers.
   Example: find_max([-5, -3, -1]) returns 0, which is wrong.
   Fix: Use max_val = numbers[0] or max_val = float('-inf').

2. No input validation:
   The function crashes with an IndexError if an empty list is passed.
   Fix: Add a guard clause — if not numbers: return None (or raise ValueError).

3. Pythonic alternative:
   Python has a built-in max() function. Unless you have a specific reason
   not to use it, prefer: return max(numbers)

Corrected version:
   def find_max(numbers):
       if not numbers:
           raise ValueError("List must not be empty")
       return max(numbers)
```

---

### Example 3 — Debate Opponent

**Prompt:**
```
You are a skilled debate opponent arguing against the following position.
Present the three strongest counterarguments with supporting evidence.

Position: "Social media has been a net positive for society."
```

**Model Output:**
```
Counterargument 1 — Mental Health Crisis:
Research from the American Psychological Association links heavy social media 
use to increased rates of anxiety, depression, and loneliness, particularly 
among teenagers. The algorithmic design of platforms maximises engagement, 
not wellbeing.

Counterargument 2 — Spread of Misinformation:
Social media algorithms amplify emotionally engaging content, which is often 
sensational or false. Studies show misinformation spreads 6× faster than 
accurate news on platforms like Twitter/X (Vosoughi et al., 2018).

Counterargument 3 — Erosion of Privacy and Democracy:
The Cambridge Analytica scandal demonstrated how personal data harvested 
from social platforms can be weaponised to manipulate elections. Surveillance 
capitalism undermines informed democratic participation.
```

---

### Example 4 — Socratic Tutor

**Prompt:**
```
You are a Socratic tutor. Instead of giving direct answers, guide the student 
to the answer through targeted questions. Never reveal the answer directly.

Student question: "Why does ice float on water?"
```

**Model Output:**
```
Great question! Let's think through it together.

First, what do you know about density? How would you describe what density means?

[After student responds]

Good. Now, when water freezes into ice, do you think the molecules pack 
together more tightly or less tightly than in liquid water?

[After student responds]

Interesting — so if the molecules are spaced further apart in ice, what does 
that tell us about ice's density compared to liquid water?

[After student responds]

And now — if ice is less dense than water, what would you expect to happen 
when you place it in a glass of water?
```

---

## Popular Role Prompting Templates

```
You are an expert [domain] with [X] years of experience. [Task description]

You are a [role] helping a [audience]. Explain [topic] in terms they can understand.

You are a strict [role] (e.g., editor, code reviewer). Identify all problems with [input].

You are a [historical figure / fictional character]. Respond in character to: [question]

You are a helpful [job title] at a [company type]. Help the user with: [task]
```

---

## Tips for Effective Role Prompting

| Tip | Why It Helps |
|-----|-------------|
| Be specific about the role and expertise level | Calibrates depth and vocabulary |
| Define the target audience | Adjusts complexity of the response |
| Add behavioural constraints ("be concise", "use bullet points") | Shapes output format |
| Combine with other techniques (CoT, few-shot) | Boosts both style and accuracy |
| Use negative constraints ("do not use jargon") | Prevents unwanted behaviours |

---

## Advantages

- ✅ Simple to implement — just add a role description.
- ✅ Dramatically improves tone, style, and relevance of answers.
- ✅ Versatile — works for education, coding, creative writing, analysis.
- ✅ Helps build consistent personas for chatbots and agents.

## Limitations

- ❌ Does not give the model new knowledge it wasn't trained on.
- ❌ Model may break character for sensitive or out-of-scope requests.
- ❌ Overly restrictive roles can limit helpful answers.

---

## Comparison with Other Techniques

| Technique | Primary Purpose | Complexity | Best For |
|-----------|:--------------:|:----------:|----------|
| Zero-Shot | Task completion | Low | Simple tasks |
| Few-Shot | Format/style guidance | Low–Medium | Consistent formatting |
| Chain-of-Thought | Step-by-step reasoning | Medium | Complex reasoning |
| Role Prompting | Tone & persona control | Low | Domain-specific, stylistic tasks |

---

## Further Reading

- [OpenAI Prompt Engineering Guide — Tactic: Ask the model to adopt a persona](https://platform.openai.com/docs/guides/prompt-engineering)
- Salewski et al. (2023) — *In-Context Impersonation Reveals Large Language Models' Strengths and Biases*
