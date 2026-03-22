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

- [x] **Game Purpose:** So basically this is a number guessing game built with Streamlit. You pick a difficulty — Easy, Normal, or Hard — and the game picks a secret number within that range. You have a limited number of attempts to guess it, and after each guess it tells you to go higher or lower. The fewer attempts you use, the more points you get. Pretty simple concept, except the AI that built it left a bunch of bugs in it.

- [x] **Bugs Found:**
  1. The hints were completely backwards — if your guess was too high it told you to go higher, and if it was too low it told you to go lower. So basically the game was actively misleading you.
  2. The New Game button didn't actually reset the game. It would say "New game started" but then block you from typing anything because the status was still set to "won" or "lost" from the previous game.
  3. attempts started at 1 instead of 0, so the very first guess was being counted as attempt 2.
  4. On top of that, the score formula had an extra `+1` that made it double count the attempt — so both bugs stacked and you were losing 20 points instead of 10 on every win.
  

- [x] **Fixes Applied:**
  1. Fixed the hint messages in check_guess — both the normal branch and the except TypeError branch had them swapped, so I had to fix both.
  2. Added proper resets to the New Game block: status back to "playing", score to 0, and history to an empty list so the game actually starts fresh.
  3. Changed attempts to start at 0 instead of 1.
  4. Updated the New Game button to use random.randint(low, high) so the secret number always stays within the correct difficulty range.
  5. Moved all 4 functions from app.py into logic_utils.py so the tests could actually import and use them.
  6. Fixed the existing tests since they were comparing the full tuple return value to a plain string — updated them to unpack (outcome, message) properly, and added 3 new tests to specifically verify the hint direction bug was fixed.

## 📸 Demo

- ![My Screenshot](screenshot.png) [Insert a screenshot of your fixed, winning game here]

## 🚀 Stretch Features

- [ ] [If you choose to complete Challenge 4, insert a screenshot of your Enhanced Game UI here]
