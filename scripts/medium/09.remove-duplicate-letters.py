def removeDuplicateLetters(s):
    """
    :type s: str
    :rtype: str
    """
    n = len(s)

    # Map the last indices of each character appearing in s
    last_index = dict()
    # take dict for status of character whether aken into result or not
    is_taken = dict()
    
    # go through all elements in s and map last index and is_taken to False
    for i in range(n):
        last_index[s[i]] = i
        is_taken[s[i]] = False

    # Result list 
    result = []

    # iterate over the list
    for i in range(n):
        ch = s[i]
        # check if the character is taken
        if is_taken[ch]:
            # if taken then ignore and continue to next character
            continue
        
        # else
        # if pop last element from the result list 
        # if s[i] is smaller than result[-1] and result[-1] appear again after s[i]
        # and if len(result) > 0
        while len(result) > 0 and result[-1] > ch and last_index[result[-1]] > i:
            is_taken[result[-1]] = False
            result.pop()

        # add the character in result and make is_taken flag for it to True
        result.append(ch)
        is_taken[ch] = True
    
    return ''.join(result)

# Example 1:

# Input: s = "bcabc"
# Output: "abc"

# Example 2:

# Input: s = "cbacdcbc"
# Output: "acdb"