class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dict1 = defaultdict(int)
        for num in nums:
            dict1[num] += 1
        sorted_dict = dict(sorted(dict1.items(), key = lambda item:item[1], reverse = True))
        ans = []
        for key in sorted_dict.keys():
            if len(ans) >= k:
                break
            else:
                ans.append(key)
        return ans