class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        #DFS dolution
        ajd = { i:[] for i in range(n)}
        for n1, n2 in edges:
            ajd[n1].append(n2)
            ajd[n2].append(n1)


        visited = set()

        def dfs(node):
            for nei in ajd[node]:
                if nei in visited:
                    continue
                visited.add(nei)
                dfs(nei)
            visited.add(node)

        res = 0
        for i in range(n):
            if i not in visited:
                dfs(i)
                res += 1

        return res
            


        


        # Union find algorithm