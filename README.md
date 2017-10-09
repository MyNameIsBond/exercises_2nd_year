# exercises_2nd_year
Second year solvings.



Some stuff
#A D V A N C E D T A S K S

1. Write a function that takes an input a list of numbers and outputs a list of all numbers in the original
list that are Kaprekar numbers. A Kaprekar number is a non-negative integer, the representation of
whose square can be split into two parts that add up to the original number. For example, 45 is a
Kaprekar number, as 452 = 2025 𝑎𝑛𝑑 20 + 25 = 45. 9 is also a Kaprekar number, as 9
2 =
81 𝑎𝑛𝑑 8 + 1 = 9.

2. Given a system of N equations with N unknown variables, write a program to solve this system using a
numeric method. Input: 2x + y + 3z = 14, x – y + z = 4, x + 3y – z = 2 Output: x = 2, y = 1, z = 3
Hint: Store all coefficients of the variables on the left hand side in a matrix and the equations’ solution in a
column vector. The overall system solution can be found using the formula: x = inv(A)*B, where A is the left
hand side coefficient matrix and B is the right hand side solution vector column. Note: This method only
works if there is one solution to the system.