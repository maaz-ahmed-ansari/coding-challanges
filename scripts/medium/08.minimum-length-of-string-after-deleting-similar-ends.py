def minimumLength(s):
    """
    :type s: str
    :rtype: int
    """
    i = 0
    j = len(s) - 1
    
    while i < j and s[i] == s[j]:
        ch = s[i]
        while i < j and s[i] == ch:
            i += 1
        while j >= i and s[j] == ch:
            j -= 1
    
    return j - i + 1


# Example 1:

# Input: s = "ca"
# Output: 2
# Explanation: You can't remove any characters, so the string stays as is.

# Example 2:

# Input: s = "cabaabac"
# Output: 0
# Explanation: An optimal sequence of operations is:
# - Take prefix = "c" and suffix = "c" and remove them, s = "abaaba".
# - Take prefix = "a" and suffix = "a" and remove them, s = "baab".
# - Take prefix = "b" and suffix = "b" and remove them, s = "aa".
# - Take prefix = "a" and suffix = "a" and remove them, s = "".

# Example 3:

# Input: s = "aabccabba"
# Output: 3
# Explanation: An optimal sequence of operations is:
# - Take prefix = "aa" and suffix = "a" and remove them, s = "bccabb".
# - Take prefix = "b" and suffix = "bb" and remove them, s = "cca".