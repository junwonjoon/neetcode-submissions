
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        i = 0
        lst = []
        while i < len(points):
            lst.append([i,(points[i][0] ** 2 + points[i][1] ** 2) ** 0.5])
            i += 1
        lst.sort(key=lambda x:x[1])
        j = 0
        return_lst = [] 
        while j < k:
            return_lst.append(points[lst[j][0]])
            j += 1
        return return_lst

