class Solution:

    def courseScheduler(self, numCoureses, prerequisities):
        prereq = {i: [] for i in range(numCoureses)}
        for crs, pre in prerequisities:
            prereq[crs].append(pre)

        # This will maintain the state of the nodes that we have visted and we are visting
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
            visited.add(crs)
            visiting.remove(crs)
            return True

        for i in range(numCoureses):
            if dfs(i) == False:
                return False
        return True
