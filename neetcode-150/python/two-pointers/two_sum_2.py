class Solution:
    def twoSum(self, numbers, target):
        map = {}
        # Create a map
        for i in range(len(numbers)):
            map[numbers[i]] = i

        for i in range(0, len(numbers)):
            num = numbers[i]
            y = target - num
            if y in map:
                return [i + 1, map[y] + 1]


solution = Solution()
print(solution.twoSum([2, 7, 11, 15], 9))
