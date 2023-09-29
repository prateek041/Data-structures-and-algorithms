class Solution:
    def dailyTemperatures(self, temperatures):
        answers = [0] * len(temperatures)
        stack = []
        indexStack = []
        for index in range(len(temperatures)):
            if stack[-1] < temperatures[index]:
                stack.pop()
                valIndex = indexStack.pop()
                answers[valIndex] = index - valIndex
            else:
                stack.push(temperatures[index])
                indexStack.push(index)
        return answers


sol = Solution()
print(sol.dailyTemperatures([73,74,75,71,69,72,76,73]))