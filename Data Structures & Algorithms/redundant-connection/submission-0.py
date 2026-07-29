class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        # if we have n nodes and n edges we will alvays end up with a cycle

        parent = [i for i in range(len(edges) + 1)]
        rank = [1] * (len(edges) + 1)

        def find(n):
            p = parent[n]
            while p != parent[p]:
                parent[p] = parent[parent[p]] # improves speed 
                p = parent[p]
            return p

        #return false if cant compile
        def union(n1, n2):
            p1, p2 = find(n1), find(n2)

            if p1 == p2:
                return False

            if rank[p1] > rank[p2]:
                parent[p2] = p1
                rank[p1] += rank[p2]
            else:
                parent[p1] = p2
                rank[p2] += rank[p1]
            return True

        res = []
        for n1, n2 in edges:
            if not union(n1, n2):
                res.append([n1, n2])

        return res[-1]