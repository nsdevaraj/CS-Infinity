


Initially, we have no tests, no code, but the 'system' can be considered Green because we have no failing tests. The very first action is to convert to a state of Red (at least one test is failing)

#### Red: Write the first failing test
#### Green: Write code to make the test pass
#### Refactor step




. Consider how you name your tests, as maintaining your tests and making changes to them will become a 'cost' to your development



 first principle of TDD:

> You are not allowed to write any production code unless it is for making a failing unit test pass


What is the simplest code that will make the test go green?


It's just to return a constant:

```
    public String convert(int number) {        return "1";    }
```

_**This is known as "Faking it".**_ Don't be concerned too much by this.



Some of the guiding principles for TDD are _**"KISS" (or "keep it simple stupid")**_, and _**"YAGNI" ("you ain't going to need it")**_. Both of these principles are subtly different but they both agree that in the context of TDD, the focus should be to just write enough code to pass the test, using the simplest solution to do so. This helps keep the design as clean and clear as possible.

Even Kent Beck, the pioneer of TDD, has suggested a principle of his own: _**"fake it until you make it"**_. This is what we've just done.


While normally code should conform to the _**Don't Repeat Yourself (a.k.a. DRY) principle**_, that doesn't mean you need to remorselessly refactor out duplication as soon as you see it.

Experienced designers know that "the best decisions are made with the maximum possible information". Therefore pragmatic designers try to defer design decisions for as long as they can.

This is not about ignoring duplication, but about tolerating it for a short time, as a trade-off to get a clearer picture of any emerging patterns in your code. Sometimes if you remove a pattern of duplication immediately it leads to less optimal designs. By waiting for the duplication to happen three times, you allow the possibility of a larger more subtle pattern to emerge that requires a different design decision.

So, until we see three cases of obvious redundancy, we will defer refactoring it out. This is known as the _Rule of Three_.




We can easily spot a rule-of-three violation in the implementation now. This is a chance for us to make a leap from a specific solution to a more generic one:

```
    public String convert(int number) {        return String.valueOf(number);    }
```

It's also important to keep duplication as low as possible in tests, so we convert our three methods to a parameterized test case:

```
    @ParameterizedTest    @CsvSource({ "1,1", "2,2", "4,4" })    void convert_number_to_FizzBuzz_string(int input, String expectedOutput) {        assertEquals(expectedOutput, new FizzBuzz().convert(input));    }
```


We now try to use the third implementation strategy of **_triangulation_**. We do this by creating a specific test case, that forces the behaviour of your code to change.
This is a strategy performed as a small step, where the implementation for the specific tests can start to reveal the underlying patterns that will give clues to the eventual generic solution.



#### What about invalid inputs?

When doing katas, we like to focus on the Happy Path. There is certainly a time and a place for protection from bad input (e.g. in user interfaces!), but that's not what we're practising here. Besides, good code design would suggest separating the responsibility of checking input validity from the responsibility of executing the algorithm. So if this were a real system, the `FizzBuzz` class might be wrapped by a `FizzBuzzInputChecker` class which ensured that `FizzBuzz` was only ever fed valid numbers.



referred {

https://www.codurance.com/katas/fizzbuzz#Frequently-Asked-Questions


}






to check {

https://www.youtube.com/watch?v=qkblc5WRn-U


}

















