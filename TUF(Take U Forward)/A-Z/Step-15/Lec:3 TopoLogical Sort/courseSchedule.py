class Solution:

    def courseSchedule(self, numOfCourses, prerequisities):
        prereq = {i: [] for i in range(numOfCourses)}
        for crs, pre in prerequisities:
            prereq[crs].append(pre)

        visiting = set()
        visited = set()

        def dfs(crs):
            if crs in visiting:
                return False
            if crs in visited:
                return True
            visiting.add(crs)
            for nei in prereq[crs]:
                if dfs(nei) == False:
                    return False
            visiting.remove(crs)
            visited.add(crs)
            return True

        for i in range(numOfCourses):
            if dfs(i) == False:
                return False
        return True
