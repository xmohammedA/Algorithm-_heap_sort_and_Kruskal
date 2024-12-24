# Algorithm_heap_sort_and_Kruskal’s-Algorithm
---
## Content
- [Heap-Sort Algorithm](#heap-sort-algorithm)
  - [Algorithm Description](#algorithm-description)

  - [Time Complexity Analysis](#time-complexity-analysis)
  - [Example](#example)
- [Kruskal's Algorithm](#kruskals-algorithm)
  - [Algorithm Description](#algorithm-description-1)

  - [Time Complexity Analysis](#time-complexity-analysis-1)
  - [Example](#example-1)
---
 
## Heap-Sort Algorithm

### *Algorithm Description*
   Heap-Sort is a comparison-based sorting algorithm that uses the properties of a binary heap (max-heap or min-heap).<br>
   It efficiently sorts data in O(nlogn) time and is an in-place sorting algorithm, requiring no extra memory for intermediate operations.
   

### *Time Complexity Analysis*
1. Time Complexity:
      - Building the heap: O(n)
      - Sorting the heap: O(nlogn)
      - Total: O(nlogn)
2. Space Complexity: O(1) (in-place sorting).
### *Example*
#### input
![image](https://github.com/user-attachments/assets/2266d064-aeb4-48c9-be10-de265eeda286)
#### steps
1. Build max heap <br>
   ![image](https://github.com/user-attachments/assets/a5a87553-2ce2-45f8-bba6-38b7ce18e15e)
2. Extract Maximum and Sort:
   - 1st extraction: [5, 4, 3, 1, 10]
   - 2nd extraction: [4, 1, 3, 5, 10]
   - 3rd extraction: [3, 1, 4, 5, 10]
   - 4th extraction: [1, 3, 4, 5, 10]
#### Output:
![image](https://github.com/user-attachments/assets/323e553a-65a8-45c8-a7cc-31945aae8898)


## Kruskal's Algorithm

### *Algorithm Description*

Kruskal’s Algorithm is a greedy algorithm used to find the Minimum Spanning Tree (MST)<br> of a connected, weighted graph. The MST is a subset of the edges that connects all vertices<br> in the graph while minimizing the total edge weight and avoiding any cycles.
#### Key Idea:
1. Sort all edges by weight (in ascending order).
2. Add edges one by one to the MST, ensuring no cycles are formed.
3. Use a Disjoint Set Union (DSU) data structure to efficiently detect cycles.


### *Time Complexity Analysis*
1. Sorting Edges: O(ElogE), where E is the number of edges.
2. Initialization of the Disjoint Set data structure takes O(𝑉) time, where 𝑉 is the number of vertices.
   Each edge is considered for inclusion in the Minimum Spanning Tree (MST), <br>
   which involves checking whether it forms a cycle (find operation) and unifying the sets (union operation). we can consider each     
   operation to be roughly 𝑂(log𝑉)in amortized time. Since each operation (find and union) is performed for at most 𝐸 edges, this step takes 𝑂(𝐸log𝑉)time.

  
Overall Time Complexity: O(ElogE+E⋅α(V))≈O(ElogE) for most cases.<br>
Space Complexity: O(V+E), primarily for storing edges and the DSU structure.<br>
Disjoint Set Union (DSU)


### *Example*

#### Input Graph:

![image](https://github.com/user-attachments/assets/779fa150-07d4-4169-8740-389bee3a0505)

#### Steps:
1. Sort Edges by Weight: <br>
   ![image](https://github.com/user-attachments/assets/7ec7f671-cafd-4756-ad0d-83b510bd97d3)

2.Initialize DSU(Disjoint Set Union): Each vertex is its own parent.
3. Iterate Through Edges:
- Add edge (1, 2, 5) → No cycle → MST = [(1, 2, 5)].
- Add edge (3, 4, 5) → No cycle → MST = [(1, 2, 5), (3, 4, 5)].
- Add edge (0, 1, 7) → No cycle → MST = [(1, 2, 5), (3, 4, 5), (0, 1, 7)].
- Add edge (1, 4, 7) → No cycle → MST = [(1, 2, 5), (3, 4, 5), (0, 1, 7), (1, 4, 7)].
- Stop (MST now contains V−1=4 edges).

#### Output
![image](https://github.com/user-attachments/assets/37aa1eaf-d9ea-4d8b-b876-4a41bba10d49)













         

         
   
   
