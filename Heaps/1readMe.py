import heapq

minHeap = [9, 8, 7, 6, 5, 4, 3, 2, 1]
maxHeap = [-i for i in minHeap]
heapq.heapify(minHeap)
print("----------------------------------")
print("Min Heap:")
print(minHeap)
# heapq.heapify will always create a minHeap

print("--------------------------------------------")
heapq.heapify(maxHeap)
print("Max Heap")
print(maxHeap)

# Other Methods are heapq.heappop() and heapq.heappush()
