import heapq
from collections import deque


class Solution:

    def tasks(self, tasks, coolingTime):
        # First of we will get the counts odf all the task and we will use the task that occurs most number of time to reduce the time
        taskCount = {}
        for i in tasks:
            taskCount[i] = 1 + taskCount.get(i, 0)

        tasks = [-i for i in taskCount.values()]
        # we will create a max heap to get the task count of the task that we got most frequent
        heapq.heapify(tasks)
        # we will also use a queue and puch those tas whivh are in cooling period
        q = deque()
        # initial time will be zero
        time = 0
        while tasks or q:
            time += 1
            if tasks:
                cnt = 1 + heapq.heappop(tasks)
                if cnt:
                    q.append([cnt, time + coolingTime])
            if q and q[0][1] == time:
                heapq.heappush(tasks, q.popleft()[0])

        return time
