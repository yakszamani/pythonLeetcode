class Solution(object):
    def romanToInt(self, j) :
        romanfigures = {
            "I" : 1,
            "V" : 5,
            "X" : 10,
            "L" : 50,
            "C" : 100,
            "D" : 500,
            "M" : 1000,
        }
        answer = 0
        j = j.replace("IV", "IIII").replace("IX", "VIIII")
        j = j .replace("XL", "XXXX").replace("XC", "LXXXX")
        j = j.replace("CD", "CCCC"). replace ("CM", "DCCCC")

        for no in j:
            answer = answer + romanfigures[no]
        return answer
        
        """
        :type s: str
        :rtype: int
        """


    