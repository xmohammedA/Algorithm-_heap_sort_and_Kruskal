def heapify(arr, n, i):
    largest = i  # Initialize largest as root
    left = 2 * i + 1  
    right = 2 * i + 2  

    # Check if left is larger
    if left < n and arr[left] > arr[largest]:
        largest = left

    # Check if right is larger
    if right < n and arr[right] > arr[largest]:
        largest = right

    # If the largest is not root
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]  # Swap
        heapify(arr, n, largest)

def heap_sort(arr):
    n = len(arr)

    # Build max heap
              #      start      end    step
    for i in range(n // 2 - 1  , -1,   -1):
        heapify(arr, n, i)

    # Extract elements from the heap
    for i in range(n - 1 , 0 , -1):
        arr[i], arr[0] = arr[0], arr[i]  # Swap
        heapify(arr, i, 0)


data = [ 4 , 10 , 3 , 5 , 1 , 51 , 2 , 6 , 7 ,-1 ]
heap_sort(data)
print("Sorted array:", data)
