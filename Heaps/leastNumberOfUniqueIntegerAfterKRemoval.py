import heapq


class Solution:

    def removal(self, nums, k):
        # create count of the values
        count = {}
        for i in nums:
            count[i] = 1 + count.get(i, 0)

        minHeap = []
        for i in count:
            heapq.heappush(minHeap, [i, count[i]])

        while k > 0 and minHeap:
            val, freq = heapq.heappop(minHeap)
            if k >= freq:
                k = k - freq
                del count[val]

        return len(count)


arr = [4, 3, 1, 1, 3, 3, 2]
k = 3
sol = Solution()
ans = sol.removal(arr, k)
print("Answer is: ", ans)
