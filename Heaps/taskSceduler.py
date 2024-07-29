import heapq
from collections import deque


class Solution:

    def scheduler(self, tasks, n):
        tasksCount = {}
        for i in tasks:
            tasksCount[i] = 1 + tasksCount.get(i, 0)

        tasks = [-i for i in tasksCount.values()]
        heapq.heapify(tasks)
        q = deque()
        time = 0
        while q or tasks:
            time += 1
            if tasks:
                cnt = 1 + heapq.heappop(tasks)
                if cnt:
                    q.append([cnt, time + n])
            if q and q[0][1] == time:
                heapq.heappush(tasks, q.popleft()[0])
        return time


tasks = ["A", "A", "A", "B", "B", "B"]
n = 2
sol = Solution()
time = sol.scheduler(tasks, n)
print("Time Taken To Compelete all The task: ", time)
