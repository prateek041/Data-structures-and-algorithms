class Solution:
    # This is the main function
    def twoSum(self, numbers, target):
        pass

    # This uses iterative binary search, therefore O(1) space complexity.
    def twoSumBinarySearch(self, numbers, target):
        start = 0
        end = len(numbers) - 1

        for index, item in enumerate(numbers):
            diff = target - item
            print("diff is: ", diff)
            while start <= end:
                # calculating the mid
                mid = int((start + end) / 2)
                print("mid is: ", mid)
                if diff > numbers[mid]:
                    print("diff is > number", numbers[mid])
                    start = mid + 1
                elif diff < numbers[mid]:
                    print("diff is < number", numbers[mid])
                    end = mid - 1
                else:
                    return [index + 1, mid + 1]
            return -1

    # This uses hashmap, that makes it O(n) memory usage.
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

    # This is the Brute force method.
    def twoSumBrute(self, numbers, target):
        for i in range(0, len(numbers)):
            num = numbers[i]
            y = target - num
            for j in range(i + 1, len(numbers)):
                if numbers[j] == y:
                    return [i + 1, j + 1]


numbers = [2, 3, 4]
target = 6
solution = Solution()
print(solution.twoSumBinarySearch(numbers, target))
