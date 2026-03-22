# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it? 
The game looked complete, the UI was well developed no errors in the wording or bugs until I started playin game the game, it didn't crash when i played it.
- List at least two concrete bugs you noticed at the start  
  (for example: "the hints were backwards").
1.The score did not match with the score the user had and what was displayed.
2. Clicking on new game did not actually start a new game 
---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)? 
Claude 
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
Hard difficulty secret out of range ✅
app.py:136 — new game hardcodes random.randint(1, 100) instead of using the difficulty range. Hard's range is 1–50, so a secret of 61 is possible after clicking New Game.
I clicked on hard difficult and realized it was true.
- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).Hard difficulty range is wrong (Logic Bug)
f difficulty == "Hard":
    return 1, 50   # ← Should be harder, not easier than Normal (1–100)
Hard gives a range of 1–50, which is easier than Normal (1–100). Hard should have a wider range, e.g. 1, 500., 
it should be between 1-50 instead of what the AI suggested

---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
I played the game to check if the bug was fixed 
- Describe at least one test you ran (manual or using pytest)  

  and what it showed you about your code.
- Did AI help you design or understand any tests? How?
Yes. I described the bugs I suspected and the AI confirmed them by reading the code. For the score bug specifically, the AI suggested a test: use the debug panel to find the secret number, guess it immediately on the first attempt, and compare the result to the expected score. That test produced 70 points instead of 90, which verified both the bug and the root cause.
---

## 4. What did you learn about Streamlit and state?

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?

Streamlit reruns are similar to recomposition in Jetpack Compose — every time the user interacts with the app, the whole script runs again from the top. Just like how remember in Compose keeps a value alive across recompositions, Streamlit's session_state keeps values like score and attempts alive across reruns. Without it, everything would reset on every click.
---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?

Not just accepting the code but testing it, asking AI for help and verifying all the help from AI, so i would say a testing habit
  - This could be a testing habit, a prompting strategy, or a way you used Git.
- What is one thing you would do differently next time you work with AI on a coding task?

How to write code prompt so the AI would be able to help me achieve all my goals 
- In one or two sentences, describe how this project changed the way you think about AI generated code.

Yes honestly this looked like a simple project so didn't expect errors but there was so i would also debugg the code before i assume is production reafy