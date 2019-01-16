class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        c = 1
        result = []
        for i in xrange(len(digits)-1, -1 , -1):
            t = c + digits[i]
            
            if t >= 10:
                result.append(t % 10)
                c = 1
            else:
                result.append(t)
                c = 0
        
        if c == 1:
            result.append(1)
        return result[::-1]
