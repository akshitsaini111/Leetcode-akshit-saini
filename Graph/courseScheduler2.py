class Solution:

    def courseScheduler2(self, numCourses, prerequisities):
        prereq = {i: [] for i in range(numCourses)}
        for crs, pre in prerequisities:
            prereq[crs].append(pre)

        visiting = set()
        visited = set()
        res = []

        def dfs(crs):
            if crs in visiting:
                return False
            if crs in visited:
                return True
            visiting.add(crs)
            for nei in prereq[crs]:
                if dfs(nei) == False:
                    return False
            visited.add(crs)
            visiting.remove(crs)
            res.append(crs)
            return True

        for i in range(numCourses):
            if dfs(i) == False:
                return []
        return res
