# 🎯 Number Guessing Game

A lightweight, interactive command-line number guessing game built in Python. The game challenges players to find a randomly generated number within a limited number of attempts, offering dynamic proximity hints along the way.

---

## ✨ Features

- **Dynamic Proximity Feedback:** Informs the player if a guess is too high, too low, or within a close range ($\le 5$) of the target.
- **Attempt Tracking & Limits:** Enforces a configurable guess cap (default: 7) and displays attempts remaining after each round.
- **Error Handling:** Gracefully handles non-numeric or invalid inputs without crashing or penalizing attempts.
- **Modular Design:** Wrapped inside a reusable function with customizable parameters (`low`, `high`, `max_attempts`, and `close_threshold`).

---

## 🚀 Getting Started

### Prerequisites

You only need **Python 3.x** installed. No external packages or dependencies are required.

### Installation

1. Clone this repository:
   ```bash
   git clone [https://github.com/](https://github.com/)<your-username>/<your-repo-name>.git
