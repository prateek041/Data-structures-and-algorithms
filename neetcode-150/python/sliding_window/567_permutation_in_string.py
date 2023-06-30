class Solution:
    def checkInclusion(self, s1, s2):
        hashMap = {}
        # create a hashmap of all the characters in string s1.
        hashMap = self.createMap(s1, hashMap)

        for i in range(len(s2)):
            if s2[i] in hashMap.keys():
                start, end = i
                for j in range(len(hashMap)):
                    if end in hashMap.key():
                        hashMap[s1[i]]

    # Funtion that creates the hashmap.
    def createMap(self, s1, hashMap):
        for i in range(len(s1)):
            if s1[i] in hashMap.keys():
                hashMap[s1[i]] = hashMap.get(s1[i]) + 1
            else:
                hashMap[s1[i]] = 1

        return hashMap


solution = Solution()
solution.checkInclusion("abcc", "a")
