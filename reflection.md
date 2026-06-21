# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
    When I first ran the game, I noticed how Attempt was set to 1 with Attempts Left set to 7.
- List at least two concrete bugs you noticed at the start  
  (for example: "the hints were backwards").
    1. Hints are way off; it tells me to go lower when the secret number is out of range of my guess
    2. New Game button doesn't work. It only resets the Attempts to 0 and picks a new secret number, but history and score are the same.

**Bug Reproduction Log**

Document at least 3 bugs you found. Add rows as needed.

| Input                           | Expected Behavior | Actual Behavior                 | Console Output / Error |
|---------------------------------|-------------------|---------------------------------|------------------------|
| Guess of 50, when secreat is 48 | Go Lower          | Go Higher                       | None                   |
| Clicking New Game               | Clear history     | History there                   | None                   |
| Guess 50 twice                  | Score: 0          | Score changes from 0 to -5 to 0 | None                   |

---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
    I used Calude Code for this project.
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
    One suggestion what was correct was when I wnated it to fix the New Game. I only needed one prompt and it understood the assignment and fixed it. I verified it by running it in my browser and testing the button
- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).
    One example that was incorrect was fixing the high/low logic. I didn't specify to look at both files and it only looked at one of them and made changes that didn't fix the issue so I had to work and tell it what it was currently doing and what I wanted it done and then told it to look at specific lines and FIXITs and files and then it fixed them.

---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
    It was really up to me since no documentation was provided on the game expectations so I fixed and ran it and if it did what I wanted it to do, I considered it fixed
- Describe at least one test you ran (manual or using pytest) and what it showed you about your code.
    The test I ran using pytest was checking different cases with different numbers to see the high/low logic
- Did AI help you design or understand any tests? How?
    Yes AI helped me design, run, and understand the test cases. It provided good documentation so it was easy to understand

---

## 4. What did you learn about Streamlit and state?

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?
    Every time you click a button or type something in a Streamlit app, the entire script runs from top to bottom again — so any regular variable you set just resets to its starting value. Session state is basically a way to save certain variables so they survive those reruns, kind of like putting something in a drawer instead of leaving it on the counter where it keeps getting cleared off.

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
      One habit is working with AI and working at it in chunks instead of giving a whole list and having it do it all at once.
- What is one thing you would do differently next time you work with AI on a coding task?
      One thing I would do diffetently is document the requirement and the objective of whatever it is that I'm creating and then work at it in chunks and create test cases as I go
- In one or two sentences, describe how this project changed the way you think about AI generated code.
      I thought AI is too advanced and can do anything you want it done, but doing this project showed me that you really have to be specific in what you want it done and go step by step.
