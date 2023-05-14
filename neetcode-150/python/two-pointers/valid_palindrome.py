# In the program I mainly learnt about strings


class Solution:
    def isPalindrome(self, s: str) -> bool:
        filtered = ""
        # Create the string after removing all non alphanumeric values
        for char in s:
            if (
                (char >= "a" and char <= "z")
                or (char >= "A" and char <= "Z")
                or (char >= "0" and char <= "9")
            ):
                filtered += char.lower()

        start = 0
        end = len(filtered) - 1

        while start < end:
            if filtered[start] != filtered[end]:
                print("this was executed")
                return False
            start += 1
            end -= 1

        return True


solution = Solution()
print(solution.isPalindrome("A man, a plan, a canal: Panama"))
