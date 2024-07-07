class Solution(object):
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """

        diff = 0
        for char_t in t:
            diff += ord(char_t)
        
        for char_s in s:
            diff -= ord(char_s)
        
        return chr(diff)
    
# The ord() function returns the number representing the unicode code of a specified character.
# The chr() function returns the character that represents the specified unicode.