class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack_temp = []
        stack_ind = []
        out = [0] * len(temperatures)

        for i, t in enumerate(temperatures):
            if stack_temp and stack_temp[-1] < t:
                while stack_temp and (stack_temp[-1] < t):
                    ind = stack_ind.pop()
                    out[ind] = i - ind
                    stack_temp.pop()
                    
                stack_temp.append(t)
                stack_ind.append(i)

            else:
                stack_temp.append(t)
                stack_ind.append(i)
        
        return out