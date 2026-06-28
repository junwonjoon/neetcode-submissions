class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        if not temperatures:
            return []
        i = 0
        stack = [] 
        lst = [0 for _ in range(len(temperatures))]
        while i < len(temperatures) - 1:
            if temperatures[i] < temperatures[i + 1]:
                lst[i] = 1
            else:
                stack.append([temperatures[i], i])
            stack_to_keep = []
            for item in stack:
                if item[0] < temperatures[i + 1]:
                    lst[item[1]] = i + 1 - item[1]
                else:
                    stack_to_keep.append(item)
            stack = stack_to_keep.copy()
            i += 1
        return lst