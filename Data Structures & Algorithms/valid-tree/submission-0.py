class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # trees can not have a loop
        # trees need to have all the nodes connected
        
        if not edges:
            return True

        edgesMap = { i:[] for i in range(n)}
        for n1, n2 in edges:
            edgesMap[n1].append(n2)
            edgesMap[n2].append(n1)

        
        visited = set()
        def dfs(i, prev):
            if i in visited:
                return False

            visited.add(i)

            for n in edgesMap[i]:
                if n == prev:
                    continue
                if not dfs(n, i):
                    return False

            return True

        return dfs(0, -1) and n == len(visited)
            