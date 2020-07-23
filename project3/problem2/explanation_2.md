# Problem 2 - Search in a Rotated Sorted Array

The rotated array is able to be searched using a Binary Search Algorithm. The logic behind the algorithm is based on the search of the middle index in the input array. 

## Time Complexity: O(log n)
Since it uses the binary search algorithm. The algorithm at each iteration halves the search space by comparing the mid value with the first and last element in the subarray. The algorithm stops when the mid value is the first element in the sequence (subarray) with the minimum value. 

## Space Complexity: O(1)
Since the algorithm takes constant space resources. The implemented functions use iteration to traverse the array and, therefore, do not require extra storage depending on the input size.