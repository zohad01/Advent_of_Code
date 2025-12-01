# Day 1: Secret Entrance
[Link to Original Problem](https://adventofcode.com/2025/day/1)

## 🧩 Problem Summary
The puzzle involves opening a safe with a circular dial numbered **0 to 99**. The dial starts at **50**.

**Part 1:**
We get a list of instructions (e.g., `L68`, `R14`). `L` means rotate Left (subtract), `R` means rotate Right (add). The goal is to follow the instructions and count how many times the dial **stops** exactly on `0` after a rotation is finished.

**Part 2:**
The rules change. Instead of just checking where the dial *stops*, we need to count how many times it touches `0` **during** the rotation (every "click").

## 💡 My Approach

### Part 1: Modulo Arithmetic
Since the dial is a circle from 0-99, this is a classic modulo problem.
- **Left Rotation:** `dial = (dial - amount) % 100`
- **Right Rotation:** `dial = (dial + amount) % 100`

I just updated the position after each command and incremented my counter if `dial == 0`.

### Part 2: Simulation
For the second part, doing the math to calculate how many times we crossed zero was getting complicated (especially with large rotations like `R1000`).

Since it's Day 1 and the numbers aren't massive, I decided to just **simulate the ticks**:
- I used a `for` loop to move the dial 1 step at a time.
- Checked if `dial == 0` inside the loop.
- This catches every single time it passes zero, which solved the "method 0x434C49434B" requirement.

## 📝 Key Learnings
- **Modulo Operator (`%`):** Python handles negative modulo correctly (e.g., `-10 % 100` becomes `90`), which made the "Left" turns very easy to write without extra `if` statements.
- **Input Parsing:** Used simple string slicing (`cmd[1:]`) to separate the letter from the number.