import heapq


class Solution:

    def lastWeight(self, stones):
        stones = [-i for i in stones]
        heapq.heapify(stones)
        while len(stones) > 1:
            firstStone = heapq.heappop(stones)
            secondStone = heapq.heappop(stones)
            if secondStone > firstStone:
                heapq.heappush(stones, (firstStone - secondStone) * -1)
        stones.append(0)
        return abs(stones[0])


stones = [2, 7, 4, 1, 8, 1]
sol = Solution()
lastWeight = sol.lastWeight(stones)

print("Last Weight Of The Stone is:", lastWeight)
