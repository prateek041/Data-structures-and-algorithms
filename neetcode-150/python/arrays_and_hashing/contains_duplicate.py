from typing import List


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # using hashmap
        map = {}
        for item in nums:
            if item in map:
                return True
            else:
                map[item] = 1
        return False

