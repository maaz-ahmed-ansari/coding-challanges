def frequencySort(s):
    """
    :type s: str
    :rtype: str
    """
    char_dict = dict()

    for char in s:
        if char not in char_dict:
            char_dict[char] = 1
        else:
            char_dict[char] += 1
    
    sorted_s = sorted(
        char_dict.items(),
        key = lambda x: -x[1]
    )

    res = ''
    for item in sorted_s:
        res += item[0] * item[1]
        
    return res

# Approach
# 1. Map the occurences of chars in s in a dict
# 2. Sort the dict by value in descending order
# 3. Concat the chars along with frequency to form resulting required string


# Example 1:

# Input: s = "tree"
# Output: "eert"
# Explanation: 'e' appears twice while 'r' and 't' both appear once.
# So 'e' must appear before both 'r' and 't'. Therefore "eetr" is also a valid answer.

# Example 2:

# Input: s = "cccaaa"
# Output: "aaaccc"
# Explanation: Both 'c' and 'a' appear three times, so both "cccaaa" and "aaaccc" are valid answers.
# Note that "cacaca" is incorrect, as the same characters must be together.

# Example 3:

# Input: s = "Aabb"
# Output: "bbAa"
# Explanation: "bbaA" is also a valid answer, but "Aabb" is incorrect.
# Note that 'A' and 'a' are treated as two different characters.