class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        dp = defaultdict(int)
        dp[nums[0]] += 1
        dp[-nums[0]] += 1
        for num in nums[1:]:
            temp = defaultdict(int)
            for k in dp:
                temp[k - num] = dp[k] + temp[k - num]
                temp[k + num] = dp[k] + temp[k + num]
            dp = temp
        return dp[target]