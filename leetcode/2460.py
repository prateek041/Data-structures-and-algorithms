class Solution:
    def applyOperations(self, nums):
        # performing operations.
        for i in range(len(nums) - 1):
            if (nums[i] == nums[i+1]):
                nums[i] = nums[i] * 2
                nums[i+1] = 0

        # fixing positions.
        # Imagine splitting the output array into two halves,
        # one containing non-zero numbers, and other zero numbers,
        # the good_half variable stores the index of last
        # non-zero number.
        good_half = 0 # starting from the beginning of the array.
        for i in range(len(nums)):
        # encountered a non-zero number, put it on the
        # correct index using good_half, and increase the
        # value of good_half.
            if (nums[i] != 0):
                nums[i], nums[good_half] = nums[good_half], nums[i]
                good_half += 1

        return nums


    def find_right(self, nums):
        for i in range(len(nums) - 1, -1, -1):
            if (nums[i] != 0):
                return i
        return -1


solution = Solution()
solution.applyOperations([847,847,0,0,0,399,416,416,879,879,206,206,206,272])
