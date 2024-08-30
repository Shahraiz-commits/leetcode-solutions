class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []  # Hold opening brackets
        all_brackets = {'(':')', '[':']', '{':'}'}  # Dictionary to hold brackets
        for char in s:
            if char in all_brackets: stack.append(char)  # If opening bracket, add to stack
            elif(not stack or char != all_brackets[stack.pop()]): return False  # If stack is empty or brackets dont match, return false
        return not stack  # return true if stack is empty, all brackets matched
                
