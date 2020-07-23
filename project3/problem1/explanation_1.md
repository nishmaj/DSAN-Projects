# Problem 1 - Finding the Square Root of an Integer

The basic idea of the algorithm is to implement a variance of the binary search by finding the closest number s such that its square is below the input n (i.e s2 <= n < (s+1)2 ). The method consists of repeatedly bisecting the initial interval by computing the middle point and selecting the subinterval in which the middle_squared is bigger or smaller then the given number n. For testing the correctness of the implemented algorithm, the sqrt and floor built-in functions of the Math module have been used.

## Time Complexity: O(log(n)) 
As the binary search takes O(log n), where n represents the input number itself.

## Space Complexity: O(1) 
Memory use is independent to the input. Each loop run is independent. As a consequence, the space complexity is constant, O(1).
