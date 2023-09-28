class Solution:

    def is_valid(self, temperatures):
        result = []
        for index in range(len(temperatures) - 1):
            second = index + 1
            if temperatures[index] < temperatures[second]:
                result.append(second - index)
                index += 1
            else:
                while second < len(temperatures) - 1:
                    second += 1
                    if temperatures[index] < temperatures[second]:
                        result.append(second - index)
                        break
                result.append(0)

            index += 1
        return result


sol = Solution()
print(sol.is_valid([73,74,75,71,69,72,76,73]))
