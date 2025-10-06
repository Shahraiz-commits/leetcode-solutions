class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_frequency = {} # alphabet - frequency
        t_frequency = {}
        
        for alph in s:
            s_frequency[alph] = s_frequency.get(alph, 0) + 1
        for alph in t:
            t_frequency[alph] = t_frequency.get(alph, 0) + 1

        return s_frequency == t_frequency
