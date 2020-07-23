# problem 3 -- Data Compression - Huffman Coding

Min heap is being used to allow for easy merging of the frequency nodes. Pythons heapq library makes the addition and removal of nodes easier.

The time complexity of encode() is O(nlogn) 
Since make_frequency_dict takes O(n) time, min_heapify_dict takes O(n) time, merge_nodes takes O(logn), make_codes takes O(n), get_encoded_text takes O(n). These all result in a complexity of nlogn

The space complexity of encode() is O(n) 
Since n is the size of the string. There is a linear space complexity.

The time complexity of decode() is O(n) 
Since there is a for loop going through each character in the encoded_text, n being the size of the encoded_text.

The space complexity of decode() is O(1) 
Since there is only one variable is allocated