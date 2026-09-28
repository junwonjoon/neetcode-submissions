class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        dp = defaultdict(int)
        for i in range(len(nums)):
            neg, pos = -nums[i], nums[i]
            if i == 0:
                dp[neg] += 1
                dp[pos] += 1
            else:
                temp = defaultdict(int)
                for k in dp:
                    temp[k + neg] = dp[k] + temp[k + neg]
                    temp[k + pos] = dp[k] + temp[k + pos]
                dp = temp
        return dp[target]