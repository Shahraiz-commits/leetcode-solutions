class Solution:
    def reverseVowels(self, s: str) -> str:
        s = list(s)
        l = 0
        r = len(s) - 1
        vowels = 'aeiouAEIOU'
        swapped = False
        while l < r:
            swapped = False
            if(s[l] in vowels and s[r] in vowels):
                temp = s[l]
                s[l] = s[r]
                s[r] = temp
                swapped = True
            if(s[l] not in vowels or swapped):
                l+=1
            if(s[r] not in vowels or swapped):
                r-=1
        return ''.join(s)
