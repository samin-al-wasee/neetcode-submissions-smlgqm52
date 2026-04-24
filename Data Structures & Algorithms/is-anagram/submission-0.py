class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_occurances = {}
        t_occurances = {}

        for c in s:
            c_occurance = s_occurances.get(c, 0)
            s_occurances[c] = c_occurance + 1
        
        for c in t:
            c_occurance = t_occurances.get(c, 0)
            t_occurances[c] = c_occurance + 1

        if len(s_occurances.keys()) != len(t_occurances.keys()):
            return False

        for key in s_occurances.keys():
            if s_occurances.get(key, 0) != t_occurances.get(key, 0):
                return False
        else:
            return True
        