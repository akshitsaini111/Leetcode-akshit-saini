class Solution:

    def courseScheduler(self, numCoureses, prerequisities):
        prereq = {i: [] for i in range(numCoureses)}
