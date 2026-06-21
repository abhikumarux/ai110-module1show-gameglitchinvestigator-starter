# 🎮 Game Glitch Investigator: The Impossible Guesser

## 🚨 The Situation

You asked an AI to build a simple "Number Guessing Game" using Streamlit.
It wrote the code, ran away, and now the game is unplayable. 

- You can't win.
- The hints lie to you.
- The secret number seems to have commitment issues.

## 🛠️ Setup

1. Install dependencies: `pip install -r requirements.txt`
2. Run the broken app: `python -m streamlit run app.py`

## 🕵️‍♂️ Your Mission

1. **Play the game.** Open the "Developer Debug Info" tab in the app to see the secret number. Try to win.
2. **Find the State Bug.** Why does the secret number change every time you click "Submit"? Ask ChatGPT: *"How do I keep a variable from resetting in Streamlit when I click a button?"*
3. **Fix the Logic.** The hints ("Higher/Lower") are wrong. Fix them.
4. **Refactor & Test.** - Move the logic into `logic_utils.py`.
   - Run `pytest` in your terminal.
   - Keep fixing until all tests pass!

## 📝 Document Your Experience

The game is a number guessing game where you pick a difficulty, get a range, and try to guess the secret number before you run out of attempts.

The first thing I noticed was the hints were completely backwards. I guessed 50 when the secret was 48 and it told me to go higher. That made no sense. The second bug I caught was the New Game button — clicking it only reset the attempt count and picked a new secret, but your score and history from the last game were still sitting there. There was also a weird score bug where guessing the same number twice would fluctuate the score even though nothing changed.

To fix the hints I had to track down where the comparison logic was and swap the messages so "Too High" correctly says go lower and "Too Low" says go higher. The New Game fix meant resetting all session state — score, history, status, and feedback — not just the secret and attempts. The string comparison bug was a little sneaky; on even-numbered attempts the secret was being passed as a string instead of an int, which was messing up the comparison entirely.

## 📸 Demo Walkthrough

Describe your fixed game in numbered steps so a reader can follow along without watching a video:

1. Open the app and use the sidebar to select a difficulty (Easy: 1–20, Normal: 1–100, Hard: 1–50). The sidebar also shows how many attempts you are allowed.
2. Type a number into the "Enter your guess:" field and click **Submit Guess 🚀**. The game will tell you whether your guess is too high (Go LOWER) or too low (Go HIGHER).
3. Keep guessing using the hints to narrow down the secret number. The attempt counter and score update after every guess.
4. When you guess correctly, the screen shows balloons, reveals the secret number, and displays your final score. The fewer attempts it took, the higher your score.
5. Click **New Game 🔁** at any time to fully reset the game — secret number, score, history, and attempt count all start fresh.

**Screenshot** *(optional)*: <!-- Insert a screenshot of your fixed, winning game here -->

## 🧪 Test Results

```
$ python3 -m pytest tests/test_game_logic.py -v
============================= test session starts ==============================
platform darwin -- Python 3.14.2, pytest-9.1.1, pluggy-1.6.0
collected 7 items

tests/test_game_logic.py::test_correct_guess_returns_win PASSED          [ 14%]
tests/test_game_logic.py::test_guess_too_high_returns_go_lower PASSED    [ 28%]
tests/test_game_logic.py::test_guess_too_low_returns_go_higher PASSED    [ 42%]
tests/test_game_logic.py::test_guess_one_above_secret_is_too_high PASSED [ 57%]
tests/test_game_logic.py::test_guess_one_below_secret_is_too_low PASSED  [ 71%]
tests/test_game_logic.py::test_high_hint_does_not_say_higher PASSED      [ 85%]
tests/test_game_logic.py::test_low_hint_does_not_say_lower PASSED        [100%]

============================== 7 passed in 0.00s ===============================
```

## 🚀 Stretch Features

- [ ] [If you choose to complete Challenge 4, describe the Enhanced UI changes here — a screenshot is optional]
