# CP1404 Practical Reflection

Write short but thoughtful answers to each of the following.  
Replace each `...` with your meaningful answer.

## Estimates

Regarding the **estimates** that you did for practical tasks...

### How was your estimate accuracy usually?

My estimate accuracy was generally reasonable but varied depending on the task’s complexity.  For straightforward tasks like fixing `repeat_string` in `testing.py`, I was close to accurate.  However, for tasks involving new APIs, like `wiki.py`, I underestimated the time needed to handle exceptions and test edge cases.

### How did your estimate accuracy improve or change during the course of the subject?

Over time, my estimates became more accurate as I gained experience with Python and common pitfalls.  Early on, I didn’t account for debugging time, like handling `DisambiguationError` in `wiki.py`.  Later, I started factoring in research and testing, which improved my planning for tasks like writing doctests or assert statements.

### What did you learn from doing these estimates?

I learned that breaking tasks into smaller steps—like separating function implementation, testing, and exception handling—helps create realistic estimates.   I also realized the importance of anticipating challenges, such as API quirks or unclear requirements, which often take longer than expected.

## Code Reviews

### What have you learned from being reviewed by other people?

Being reviewed taught me to write clearer, more maintainable code.   For example, feedback on `testing.py` highlighted that consistent variable names (e.g., `length` vs.   `n` in `is_long_word`) improve readability.   Reviews also showed me how small oversights, like missing edge cases in `format_sentence`, can be caught early.

### What have you learned from doing code reviews of other people?

Reviewing others’ code helped me spot common mistakes, like incomplete exception handling or unclear docstrings, which made me more critical of my own work.   For instance, reviewing a peer’s `wiki.py` showed me the value of concise error messages, which I then applied to my own projects.


### Good Code Review 1

https://github.com/JiangJinsong/cp1404practicals/pull/6

### Explanation

In this review, I provided specific feedback. I explained why the change aligned with the function’s purpose and included a test case to demonstrate.    My comments were constructive, clear, and included a code snippet, which helped the peer implement the fix quickly.

### Good Code Review 2

https://github.com/JiangJinsong/cp1404practicals/pull/6

### Explanation

For this `wiki.py` review, I pointed out that the peer didn’t handle empty inputs gracefully, which could crash the program.    I also praised their clear exception handling for `DisambiguationError`, balancing positive feedback with actionable suggestions, which encouraged improvement without being overly critical.

## Practicals

### Regarding the **practical tasks** overall, what would you change if you were in charge of the subject?

I’d introduce more guided examples for complex topics like API usage before tasks like `wiki.py`.   While the tasks were engaging, clearer scaffolding for exception handling or doctests early on would help build confidence.   I’d also add optional stretch goals, like enhancing `format_sentence` to handle multiple punctuation marks, to challenge advanced students.

### What did you do really well for practicals in this subject?

I excelled at writing thorough tests, such as the doctests for `is_long_word` and `format_sentence` in `testing.py`, which caught edge cases early.   I also became proficient at debugging API-related issues, like handling `PageError` in `wiki.py`, by carefully reading documentation and testing iteratively.
