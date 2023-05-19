class Solution:
    def maxProfit(self, nums):
        low = 0
        high = low + 1
        maxPrice = 0
        while high < len(nums):
            # If profit, then calculate max
            if nums[low] < nums[high]:
                price = nums[high] - nums[low]
                maxPrice = max(maxPrice, price)

            else:
                low = high
            high += 1
        return maxPrice


nums = [7, 1, 5, 3, 6, 4]
solution = Solution()
print(solution.maxProfit(nums))
