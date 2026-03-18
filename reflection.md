# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
When I first ran the game it looked quite simple to get going and understand how to play the game. The mechanism seemed pretty straight forward. However when I started I quickly realized there are many issues in the game mechanism and logic.  

- List at least two concrete bugs you noticed at the start  
  (for example: "the hints were backwards").
1. The first issue I noticed was that the hints always asked to "GO LOWER!" no matter which number I guesses and submitted. I expected the hints to actually help me in a meaningluf way to be able to narrow down the number. However what happened for example in the normal difficulty setting where the range is between 1 and 100, I entered 101 and the hint still asked me to go higher. So that is clearly bug or an issue with the game.

2. A second issue I realized was the number of attemps that the game said is allowed never matched the actual number of attempts that is given. I expected to be given the right amout of attempts so I know how many tries I have however what happend is that it would say Attempts allowed:6 but you're actually given 5 attempts to guess the number instead. 

---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
I used Claudde Code on this project

- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
I asked the AI about why does in the app.py file the difficulty level for hard "return 1, 50" have a smaller range than the normal difficulty "return 1, 100" which makes it easier to guess. Claude Code told me that it was a bug and it seems like te range for Hard and Easy seems logically swapped. Claude Code sugeested ""Hard" returns (1, 50) — a smaller range than Normal, likely meant to be (1, 500) or similar" 

- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).

---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
I ran the code to play and test the game to see things were fixed and also ask the Claude to run tests for different scenarios.

- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.
- Did AI help you design or understand any tests? How?

---

## 4. What did you learn about Streamlit and state?

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
- What is one thing you would do differently next time you work with AI on a coding task?
- In one or two sentences, describe how this project changed the way you think about AI generated code.
