# Algorithm_heap_sort_and_Kruskal
## Heap-Sort Algorithm

1. Algorithm Description
2. Steps Involved in Heap-Sort
3. Time Complexity Analysis
4. Example

### Algorithm Description
   Heap-Sort is a comparison-based sorting algorithm that uses the properties of a binary heap (max-heap or min-heap).
   It efficiently sorts data in O(nlogn) time and is an in-place sorting algorithm, requiring no extra memory for intermediate operations.
   
### Steps Involved in Heap-Sort
 1. Build a Max Heap:
     - Traverse all non-leaf nodes and ensure the max heap property for each node using a process called heapify.
 2. Sort the Array
      1. Swap the root with the last element in the heap and then heapify the reduced heap.
      2. Repeat until all elements are sorted.
### Time Complexity Analysis
- Time Complexity:
      - Building the heap: O(n)
      - Sorting the heap: O(nlogn)
      - Total: O(nlogn)
- Space Complexity: O(1) (in-place sorting).
### Example
#### input
![image](https://github.com/user-attachments/assets/2266d064-aeb4-48c9-be10-de265eeda286)



         

         
   
   
