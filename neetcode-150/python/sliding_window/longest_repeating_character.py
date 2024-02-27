class Solution:
    def character_replacement(self, s, k):
        start = 0
        end = 0
        count = {}
        res = 0
        while start <= end and end < len(s):
            count[s[end]] = 1 + count.get(s[end], 0)
            max_occur = max(count.values())
            window_len = (end - start) + 1
            # check if valid.
            if window_len - max_occur <= k:
                # check what is max
                if window_len > res:
                    res = window_len
                end += 1
            # invalid window length.
            else:
                count[s[start]] = count.get(s[start]) - 1
                start += 1
                end += 1
        return res

s = "AABABBA"
k = 1
sol = Solution()
print(sol.character_replacement(s, k))