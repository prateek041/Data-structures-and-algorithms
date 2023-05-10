class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        map = {}
        # First we need to create a data structure which can be queried to find the count of each individual digit.
        # This can be done using a nested for loop and the result directly stored into a bucket (array).
        # But instead we are going to use a hashmap that will do the work in O(n) time instead of O(n^w).

        for item in nums:
            map[item] = map.get(item, 0) + 1

        # Now we can create a bucket, that will store the occurences of each unique number. The array index is the number of occurence and the array, present at that index contains all the unique numbers that occur "index" number of times.
        bucket = [[] for i in range(len(nums) + 1)]
        for key, value in map.items():
            bucket[value].append(key)

        # Now iterate through the bucket in reverse order. There is an array at every index of bucket.
        # For example, at the index 2, the array contains all the elements that appear 2 times in the original array.
        answer = []
        for i in range(len(bucket) - 1, 0, -1):
            for item in bucket[i]:
                answer.append(item)
                if len(answer) == k:
                    return answer


nums = [1, 1, 1, 2, 2, 3]
k = 2
solution = Solution()
print(solution.topKFrequent(nums, k))
