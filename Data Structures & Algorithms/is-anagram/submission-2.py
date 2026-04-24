class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_occurances = {}

        for c in s:
            c_occurance = s_occurances.get(c, 0)
            s_occurances[c] = c_occurance + 1
        
        for c in t:
            c_occurance = s_occurances.get(c, None)

            if not c_occurance:
                return False

            s_occurances[c] -= 1

            if not s_occurances[c]:
                del s_occurances[c]

        return not s_occurances
        