class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dictionary_of_frequency = {}
        list_to_return = []
        for key in nums:
            dictionary_of_frequency[key] = 0
        for key in nums:
            dictionary_of_frequency[key] = dictionary_of_frequency[key] + 1
        sorted_items = sorted(dictionary_of_frequency.items(), key=lambda item: item[1], reverse = True)
        list_to_return = []
        for i in range(k):
            list_to_return.append(sorted_items[i][0])
        return list_to_return