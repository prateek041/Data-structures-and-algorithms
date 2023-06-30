class Solution:
    def lengthOfLongestSubstring(self, s):
        if len(s) <= 1:
            return len(s)

        start = 0
        max_length = 0
        matchSet = set()
        for end in range(len(s)):
            if s[end] in matchSet:
                max_length = max(max_length, len(matchSet))

                # shrink from the left
                while s[start] != s[end]:
                    matchSet.remove(s[start])
                    start += 1
                # we found the repeated character, so remove it as well.
                start += 1  # This makes the window unique again.

            # if end is not present in set
            matchSet.update(s[end])
            end += 1

        return max(max_length, len(matchSet))


solution = Solution()
print(solution.lengthOfLongestSubstring("pwwkew"))
