"""
There are two approaches of solving this problem.
- Memory efficient way (Dutch Flag Algorithm)
- Memory in-efficient way
"""

"""
Memory in-efficient solution.
"""

from typing import List


class Solution:
    def pivot_array_in_eff(self, nums: List[int], pivot: int):
        left_subarray = []
        right_subarray = []
        center = 0

        for item in nums:
            if item < pivot:
                left_subarray.append(item)
            elif item > pivot:
                right_subarray.append(item)
            else:
                center += 1

        result = left_subarray + [pivot]*center + right_subarray
        return result

    def pivot_array_eff(self, nums:List[int], pivot: int):
        """
        Space: O(1) since we are optimising a single result array in-place.
        Time: O(N) since we are performing N comparison operations in O(1) time.
        """
        # First pass would be about calculating how many elements are to the left,
        # right and center of the pivot.
        left = 0
        center = 0
        for item in nums:
            if item < pivot:
                left += 1
            elif item == pivot:
                center += 1

        # second pass is about forming the final array.
        result = [0]*len(nums)
        lesser_index, center_index, greater_index = 0, left, left+center
        for item in nums:
            if item < pivot:
                result[lesser_index] = item
                lesser_index += 1
            elif item > pivot:
                result[greater_index] = item
                greater_index += 1
            else:
                result[center_index] = item
                center_index += 1
        return result
