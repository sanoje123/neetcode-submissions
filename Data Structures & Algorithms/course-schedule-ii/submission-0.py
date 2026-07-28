class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:

        # Topological sort O(p(prerequisites) + n(courses))
        hash_pre = {c:[] for c in range(numCourses)}
        for pre in prerequisites:
            hash_pre[pre[0]].append(pre[1])

        output = []
        visited, cycle= set(), set()

        def dfs(crs):
            if crs in cycle:
                return False

            if crs in visited:
                return True

            cycle.add(crs)
            for pre in hash_pre[crs]:
                if dfs(pre) == False:
                    return False
            
            cycle.remove(crs)
            visited.add(crs)
            output.append(crs)
            return True

        for c in range(numCourses):
            if dfs(c) == False:
                return []

        return output
