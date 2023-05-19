class Solution:
    def threeSum(self, nums):
        # Sort the array first
        nums.sort()

        results = []
        for i in range(len(nums)):
            x = nums[i]
            if x > 0:
                break
            if i > 0 and x == nums[i - 1]:
                continue
            left, right = i + 1, len(nums) - 1
            while left < right:
                sum = 0 - x
                if nums[left] + nums[right] < sum:
                    left += 1
                elif nums[right] + nums[left] > sum:
                    right -= 1
                else:
                    results.append([x, nums[left], nums[right]])
                    left += 1
                    right -= 1

        return results


nums = [-1, 0, 1, 2, -1, -4]
solution = Solution()
print(solution.threeSum(nums))
