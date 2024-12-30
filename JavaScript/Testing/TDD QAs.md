

**Does TDD Feel Slow?**
@[TDD feel slow - UncleBob](https://youtu.be/hFRq2vONviM?si=wJlQblsLCzGTJD0m)


TDD can feel slow, even when it’s faster. Jason Gorman conducted an experiment where he wrote a Roman numerals Kata 6 times over 6 days—alternating between TDD and non-TDD.

**Results:**

- With TDD, he completed it **3 minutes faster** on average.
- Without TDD, he often had to go back and fix mistakes, making it take longer.

**Key Takeaway:** TDD provided a more reliable path, but Gorman **felt** it was slower, even though it was actually more efficient. The difference? TDD gave him **fewer mistakes** and faster completion, but it _felt_ slower because of the upfront effort.


---



**Slow Tests? Fix It!**
@[SlowTests-UncleBob](https://youtu.be/GwANemcxmnw?si=0OffwqCpcWMbFh3x)

Slow tests are a problem. They get ignored, skipped, or deleted. Tests must run fast—no excuses. Modern machines can execute billions of instructions per second; your tests shouldn't take that long.

If your tests are slow, you're likely repeating expensive actions (like logging in) or relying on slow dependencies (databases, web servers).

**Solution**: Optimize your tests, remove redundancy, and keep them fast!


---

How TDD Relates to Code Quality
@[TDD related code quality - UncleBob](https://youtu.be/is41fgDrqn0?si=WxXiUBezJgZncpL3)

https://youtu.be/GvAzrC6-spQ?si=mLekSWrmLGnWr3DD


1. **Fear of Code**  
    You’ve seen messy code and thought, “I should clean this,” but feared breaking it. This fear stifles improvement, causing the code to rot over time. TDD eliminates this fear.
    
2. **The Magic Button**  
    Imagine a button that instantly confirms your code works after any change. TDD gives you that button: tests that ensure safety while you refactor, clean, and improve the code.
    
3. **Aim for 100% Test Coverage**  
    While 100% test coverage is ideal but hard to reach, it’s the goal. The closer you get, the more confidence you have in your code, making decisions easier and reducing defects.
    
4. **Trust the Test Suite**  
    A passing test suite should give you confidence. If you can’t trust your tests, they’re useless. Without solid tests, you risk overlooking bugs and making poor decisions.
    
5. **Extreme Quality**  
    TDD drives high-quality code, minimizing bugs and crashes. The goal is a tiny defect list—if your bug tracker is full, something’s wrong. Aim for a manageable list, not a backlog of thousands.
    

**In Short:**  
TDD ensures clean, reliable, and maintainable code, freeing you from fear and giving you the confidence to refactor and improve continuously.



---

**Why Write Tests First 
@[why write test first - Uncle Bob](https://youtu.be/4SIpyrko-x4?si=6BAAcKNCiP4Jm3Hp)


1. **Testing After the Fact is Painful**  
    Writing tests after the code is done feels pointless. You already know the code works, and testing becomes passive and tedious. Plus, some code is hard to test because it wasn't designed for testing, leading to messy workarounds and gaps in your test suite.
    
2. **Unreliable Test Suite**  
    If you leave holes in your tests, you can't trust the test suite. It might pass, but it doesn't mean anything because you know it's incomplete. A passing test suite with gaps is like a parachute with holes—you can't rely on it.
    
3. **Writing Tests First is Fun**  
    Writing tests first isn't just more effective—it's enjoyable. You experience the satisfaction of seeing a test fail and then making it pass. Each passing test gives you a small boost of accomplishment, making the process rewarding.
    
4. **Test-Driven Design Forces Decoupling**  
    Writing tests first forces you to design code that's decoupled and easy to test. The act of testing pushes you to make your code modular and clean, which ultimately leads to better, more maintainable systems.
    
5. **The Biggest Benefit: Trusting Your Code**  
    The real power of writing tests first is the ability to trust your code. With a solid test suite, you can confidently make changes and know that your code will continue to work. This reliability is the ultimate payoff.
    

**In Summary:**  
Writing tests first leads to better, cleaner, and more reliable code. It’s fun, forces good design, and gives you confidence that your code works—no holes, no doubts.


---
Is TDD overrated ?

no refactor done.. 
changing requirements 
hard to write code that are managable for test.. 
starting first, it feels exagurated.. 
likewise...


---


TDD frontend ?

https://youtube.com/shorts/b9JcPGuoRNQ?si=8f6KOrngfbiO_DDv

JS => I am not agree this.. 

---
Unit test, not TDD:

https://www.youtube.com/shorts/ewnqyjD-T0M

---

**3 Principles of TDD:**

1. **Red: Write a Failing Test**  
    Start with a test that fails. This ensures the test is meaningful and covers the behavior you need.
    
2. **Green: Make It Pass**  
    Write just enough code to pass the test. Focus on functionality, not perfection.
    
3. **Refactor: Clean Up**  
    Once the test passes, refactor the code for clarity and efficiency, ensuring tests still pass.
    

**In Short:**  
Write a failing test, make it pass with minimal code, then clean up—repeat.

**TDD (Test-Driven Development) in a Nutshell:**

1. **Write a failing test.**
2. **Write just enough code to pass the test.**
3. **Refactor the code, keeping tests green.**

Repeat until the feature is complete. TDD ensures clean, reliable, and well-tested code from the start.


---

TDD ?
Development approach where tests written before the code they test.. 

Aim to create: reliable, flexible and modular software.. 

---

TDD worth it ? TDD do or don';t. ?

https://youtube.com/shorts/w8FO3vylieQ?si=IfPXjyH88Z1MHVhH


https://youtube.com/shorts/_iibFgkIo_Q?si=7Zit5nf7MVEQN7x4


---

3 TDD principles:

https://youtube.com/shorts/1xukOX3gBE4?si=-QaJATgD2lTD7hYQ

The **3 Laws of TDD** are:

1. **You may not write production code** until a failing test exists.
2. **You may not write more of a test** than is sufficient to fail, or pass the next bit of code.
3. **You may not write more production code** than is sufficient to pass the test.

In short: Test first, write minimal code, and only write enough to pass the test.

---
https://youtu.be/GvAzrC6-spQ?si=3K7jyFejt-TedEXF


what tdd do?

How many of you are practicing TDD? Great, but let's be clear: writing tests after coding is _not_ TDD. That’s just checking off a box. TDD means **writing tests first**. Why? Because it forces you to know when you're done, to see the test fail, and to ensure every line of code is intentional.

The purpose of tests isn't just to satisfy QA or prove your code works; it's to give you confidence to **refactor**. Without tests, you’ll fear your own code. If you’re afraid to touch it, it will rot, slowing down the entire team. The fault is yours if you let that happen.

To control the beast, you need a **suite of tests you trust**. You must never look at your tests and think "I don’t think I tested everything." The moment that thought arises, you’ve lost control. Writing tests first ensures every decision you make is backed by a test, giving you the freedom to clean up the mess without fear.

---

Benefits of TDD:

https://youtube.com/shorts/y22LVqJRjzw?si=ExDAaPEbcJm_giia



* rector constantly
* easy maintanance
* design is divited into phases.. 
* documentation
* promote continuous change

---

to che