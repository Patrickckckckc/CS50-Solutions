# CS50 Python Programming

This repository contains my solutions and projects from **CS50’s Introduction to Programming with Python** by Harvard University (EdX).  
The course covers the fundamentals of programming using **Python**, including data structures, algorithms, functions, classes, and best coding practices.

---

## 📚 Course Structure

Each folder represents a week of the course, focusing on different programming concepts:

| Week | Topic | Description |
|------|--------|-------------|
| 0 | Variables and Data Types | First steps in Python: input/output and basic operations. |
| 1 | Conditionals | Control flow and decision-making. |
| 2 | Loops | Iterations using `for` and `while`. |
| 3 | Functions | Code modularization and reusability. |
| 4 | Exceptions | Error handling and validation. |
| 5 | Libraries | Using external modules and packages. |
| 6 | File I/O | Reading and writing files. |
| 7 | Regular Expressions | Advanced text processing. |
| 8 | Final Project | Integrating all learned concepts. |

---

## 🎮 Final Project: Tic Tac Toe (Python)

My final project is a **Tic Tac Toe game** developed entirely in Python.  
It allows two players to compete in the console, displaying the board and validating each move.

### 🔑 Additional Features
- **Single-player mode vs AI** with three difficulty levels:
  - Easy → random moves.  
  - Normal → win/defend strategy + random fallback.  
  - Impossible → unbeatable AI using the **minimax algorithm**.  
- **Board rendering** with the `tabulate` library for a clean, user-friendly display.  
- **Error handling** with custom exceptions (`MoveError`) for invalid or repeated moves.  
- **Winner detection** that checks all possible winning combinations and declares ❌, ⭕, or Draw.  
- **Input validation** to ensure smooth gameplay and prevent crashes.  

---


