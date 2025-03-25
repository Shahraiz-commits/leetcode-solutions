class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        negative = False
        num_str = str(x)
        if(num_str.startswith('-')):
            num_str = num_str.lstrip('-')
            negative = True
        reversed_str = num_str[::-1]
        if(negative):
            reversed_str  = '-' + reversed_str
        answer = int(reversed_str)
        if(-2**31 <= answer <= 2**31 - 1):
            return answer
        else:
            return 0
