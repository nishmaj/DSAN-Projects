Problem 6  -- Union and Intersection of Two Linked Lists

To calculate the union, a deep copy of both lists has been created. After that, find the end of the first list and point it to the start of the second.

To calculate the intersecion, a hash map with the key being the node value and the value being the number of occurences has been used. Hash map has been populated with the first list and then iterate through the second to find matches.

Time complexity of union: O(n) 
Since the function has three independent loops looping n times

Space complexity of union: O(n) 
Since each variable in the list is allocated to a new variable

Time complexity of intersection: O(n) 
Since the function loops n times

Space complexity of intersection: O(n) 
Since each variable in the list is allocated to a new variable
