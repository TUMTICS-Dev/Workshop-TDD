# Workshop-TDD

This is a workshop for practicing Test-Driven Development (TDD) in Python.

## Before You Start

During Test-Driven Development (TDD), it's important to refrain from looking ahead at the code you will be writing. The objective is to learn how to build your code incrementally, by starting with a simple test and then writing only the minimum amount of code necessary to pass that test.

When writing your tests, focus only on testing for correct inputs, as there is no need to test for invalid inputs in this exercise. By following this approach, you can ensure that your code is reliable, maintainable, and thoroughly tested.

## Test-Driven Development (TDD) Process

The TDD process involves the following steps:

1. Write a test.
2. Run the test.
3. If the test fails, change the code to correct it.
4. Repeat the process until your test passes successfully.

## Problem Requirement

### Q1: Sum of even numbers

Write a function that takes a list of numbers and returns the sum of all the even numbers in the list. Start with the simplest test case of an empty list and move to one and two numbers.
Examples:

* Empty list: `[] -> None`
* One number: `[1] -> 0`
* Two numbers: `[1, 2] -> 2`

### Q2: Handle an unknown amount of numbers

The function should be able to handle an unknown amount of numbers.

Examples:

* `[1, 2, 3] -> 2`
* `[1, 2, 3, 4] -> 6`

### Q3: Handle invalid inputs

If an input number is negative, the function should throw an exception with the message "elements in the list must be integers".

Examples:

* `[1, a, 3] -> exception with the message "elements in the list must be integers"`