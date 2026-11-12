<img src="assets/banner.svg" width="100%" alt="Shayan Umer: AI writes the first draft. I plan it, then rebuild it myself. Python first, then up the ladder.">

### `00 // THE RULE`

**If I can't explain a line, it doesn't ship.** AI writes the first draft. I write the spec, turn the code into my own plan in plain English, then close the code and rebuild it from that plan until both print the same thing. That's how I'm learning **Python first**, then climbing to maths, data, machine learning and LLMs, one rung at a time.

### `01 // ACTIVE BENCH`

<a href="https://github.com/shayanlabs/python-projects/tree/main/01-match-scorecard"><img src="assets/bench.svg" width="100%" alt="Active bench: project 01 Match Scorecard, shipped"></a>

> **Just shipped:** [🏏 01 Match Scorecard](https://github.com/shayanlabs/python-projects/tree/main/01-match-scorecard), written by me with the AI's draft closed, and the same output. **Next on the desk:** lists, then project 02.

### `02 // THE LADDER`

<a href="https://github.com/shayanlabs/python-projects"><img src="assets/road.svg" width="100%" alt="The ladder: 01 Python building, 02 Dev tools next, 03 Maths for ML and 04 Data planned"></a>

| # | Rung | What I'll be able to do | Status |
|---|---|---|---|
| 01 | Python | write and read real programs: lists, functions, files, classes | 🛠️ building · [python-projects](https://github.com/shayanlabs/python-projects) |
| 02 | Dev tools | work like an engineer: Git, the terminal, and directing AI coding tools | ⏳ next |
| 03 | Maths for ML | the algebra, calculus and statistics under every model | 🗺️ planned |
| 04 | Data | clean, explore and chart real datasets with NumPy and pandas | 🗺️ planned |

Then: classical ML → neural nets → deep learning → LLMs and agents.

### `03 // FIELD NOTES & FAILURES`

Real mistakes from my notebook, kept on purpose.

<details>
<summary><b>My counter never moved.</b></summary>
<br>

In a gym log, every line said `Set 1`. I'd made the counter but never added to it inside the loop. A counter starts **before** the loop and moves **inside** it.
</details>

<details>
<summary><b>One variable, two jobs.</b></summary>
<br>

I used one counter both to count every set and to remember which set was best. So "Best" always named the *last* set, not the best one. Two jobs need two variables: one keeps the best score, the other remembers where it happened.
</details>

<details>
<summary><b><code>(0.0)</code> is not a list.</b></summary>
<br>

Round brackets around one number give you one plain number. `[0.0, 0.0]` is a list, and `(0.0, 0.0)` is a tuple. One character, and the whole program breaks.
</details>

<details>
<summary><b>I forgot the brackets.</b></summary>
<br>

I wrote `answer.isdecimal` instead of `answer.isdecimal()`. Without the brackets the check never runs, so letters went straight into `int()` and crashed it. A method only does its job when you call it.
</details>

### `04 // HOW I BUILD`

```text
spec      → I write exactly what it must do
draft     → AI writes the first version
plan      → I turn its code into numbered steps in plain English
rebuild   → I close the code and write it again from my plan
same out  → both versions print the same thing on the same input
ship      → only what I can explain; AI never debugs for me
```

### `05 // PING`

Learning to build in the AI era too? Let's trade notes.
[LinkedIn](https://www.linkedin.com/in/shayanlabs) · [Instagram](https://www.instagram.com/shayan.code)

<sub><i>Build with purpose. Finish what you start. Share what you learn.</i></sub>
