class Solution:

    def courseScheduler2(self, numOfCourses, prerequisteries):
        prereq = {i: [] for i in range(numOfCourses)}
        for crs, pre in prerequisteries:
            prereq[crs].append(pre)

        visiting = set()
        visted = set()
        res = []

        def dfs(crs):
            if crs in visiting:
                return False
            if crs in visted:
                return True
            visiting.add(crs)
            for nei in prereq[crs]:
                if dfs(nei) == False:
                    return False
            visiting.remove(crs)
            visted.add(crs)
            res.append(crs)
            return True

        for i in range(numOfCourses):
            if dfs(i) == False:
                return []
        return res
