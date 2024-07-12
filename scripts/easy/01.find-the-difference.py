def findTheDifference(s, t):
    """
    :type s: str
    :type t: str
    :rtype: str
    """

    # Approach 1 - Using Dictionary --------------
    map = dict()

    for i in s:
        if i not in map:
            map[i] = 1
        else:
            map[i] += 1
    
    for char in t:
        if char not in map:
            return char

        map[char] -= 1

        if map[char] < 0:
            return char


    # Approach - 2 Using Unicode conversion --------------

    diff = 0

    for char in t:
        diff += ord(char)
    
    for char in s:
        diff -= ord(char)
    
    return chr(diff)
    
# The ord() function returns the number representing the unicode code of a specified character.
# The chr() function returns the character that represents the specified unicode.