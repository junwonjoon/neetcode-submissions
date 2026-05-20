class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dictionary = {}
        lst = []
        for num in nums:
            if num not in dictionary:
                dictionary[num] = 1
            else:
                dictionary[num] = dictionary[num] + 1
        sorted_dict = sorted(dictionary.items(), key = lambda item:item[1], reverse=True)
        for key,value in sorted_dict:
            lst.append(key)
            if len(lst) >= k:
                break
        return lst