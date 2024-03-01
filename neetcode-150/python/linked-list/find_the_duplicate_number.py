class Solution:

    # This approach is O(1) space and O(N)time complexity.
    def find_duplicate_number(self, nums: list[int]) -> int:
        slow_pointer, fast_pointer = 0, 0
        while True:
            slow_pointer = nums[slow_pointer]
            fast_pointer = nums[nums[fast_pointer]]
            if slow_pointer == fast_pointer:
                break

        slow_pointer = 0
        while True:
            slow_pointer = nums[slow_pointer]
            fast_pointer = nums[fast_pointer]
            if slow_pointer == fast_pointer:
                break

        return slow_pointer

    # This approach is o(N) time but O(N) space.
    def find_duplicate_number_memory_inefficient(self, nums: list[int]) -> int:
        map = {}
        for num in nums:
            if num in map.keys():
                return num
            else:
                map[num] = 1
        return 0
