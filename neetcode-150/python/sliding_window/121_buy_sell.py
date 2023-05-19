class Solution:
    def maxProfit(self, nums):
        maxComb = []
        # Create all possible collections.
        for i in range(len(nums)):
            max = 0
            for j in range(i + 1, len(nums)):
                if nums[j] - nums[i] > max:
                    max = nums[j] - nums[i]
            maxComb.append(max)

        final_max = 0
        for item in maxComb:
            if item > final_max:
                final_max = item

        return final_max


nums = [7, 6, 4, 3, 1]
solution = Solution()
print(solution.maxProfit(nums))
