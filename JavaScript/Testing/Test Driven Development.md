  


TDD:
* test driven development - development is driven by tests.. as name suggests
* development technique - describe behaviour of code before implementation
* automated testing - write code describes your requirement and validates your app
* reduce bugs & improve maintainability - results are seen only in long run
* testing code - powerful way to level up as developer - not only fun , also teach you about your code in unexpected ways & better debugging


* TDD - not fit when requirement changes frequently ( any software should not ) - clear requirements TDD improves productivity
* follow Red Green Refactor - short repetative development cycle -  run failing tests, make it working right , refactor the code 
  
Write a failing test, make it pass with minimal code, then clean up—repeat.

**3 Principles of TDD:**

1. **Red: Write a Failing Test**  
    Start with a test that fails. This ensures the test is meaningful and covers the behavior you need.
    
2. **Green: Make It Pass**  
    Write just enough code to pass the test. Focus on functionality, not perfection.
    
3. **Refactor: Clean Up**  
    Once the test passes, refactor the code for clarity and efficiency, ensuring tests still pass.
    



Testing types:  ( functional )

most prominant 3 of TDD: 

Unit tests  - validate behaviour of individual func/methods or units of code
Integration tests  - testing multiple units of code together 
End to end tests - run whole app in simulated environment and emulate user behaivors



![[Pasted image 20250127125558.png]]



Benefits of TDD: 
* Improved code quality and design  
* Reduced debugging time  
* Increased code coverage  
* Early detection of bugs  
* Better understanding of requirements  ( works as documentation )
* Increased confidence in code changes / refactor  


**3. Outside-In TDD**  
  
* **Focus:** Starts with the user interface (UI) or the highest-level component and gradually moves inwards, testing interactions with lower-level components.  

Key Principles: 
* **Start with the public interface:** Begin by writing tests for the public methods of the top-level class.  
* **Test interactions:** Focus on how components interact with each other, ensuring that data flows correctly between them.  
* **Stub or mock dependencies:** Replace lower-level components with stubs or mocks to isolate the component under test.  

Benefits:  
* Drives a clear and well-defined architecture.  
* Ensures that the system integrates correctly from the top down.  
* Helps identify and resolve integration issues early in the development process.  



![[Pasted image 20250127130223.png]]




Q/As


TDD slower?
TDD gave him **fewer mistakes** and faster completion, but it _felt_ slower because of the upfront effort.


Slow tests ?
Optimize your tests, remove redundancy, and keep them fast!


TDD relates to code Quality ?
TDD ensures clean, reliable, and maintainable code, freeing you from fear and giving you the confidence to refactor and improve continuously.



Why write test first :
Writing tests first leads to better, cleaner, and more reliable code. It’s fun, forces good design, and gives you confidence that your code works—no holes, no doubts.
writing test last hard to split things for testing after development 
don't write tests lazy 








