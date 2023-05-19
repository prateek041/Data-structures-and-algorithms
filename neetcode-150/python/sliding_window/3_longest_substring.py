class Solution:
    def lengthOfLongestSubstring(self, s):
        left = 0
        right = 0
        sub = ""
        maxSub = ""
        while right < len(s):
            if s[right] in sub:
                if len(maxSub) < len(sub):
                    maxSub = sub
                left = right

            else:
                sub += s[right]

            right += 1

        return len(maxSub)


solution = Solution()
print(solution.lengthOfLongestSubstring("aab"))
