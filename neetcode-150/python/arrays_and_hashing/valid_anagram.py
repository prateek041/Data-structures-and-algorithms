class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # using hashmap
        s_map = self.generate_map(s)
        t_map = self.generate_map(t)

        for key, value in s_map:

            

    def generate_map(self, x: str)-> dict:
        map = {}
        for char in x:
            map[char] = map[char] + 1 or 0
        return map
