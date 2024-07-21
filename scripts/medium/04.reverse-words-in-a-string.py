def reverseWords(s):
    """
    :type s: str
    :rtype: str
    """
    # Approach 1 - Using built-in string functions
    s_lst = s.strip().split()
    result = ''
    for word in s_lst[::-1]:
        result += word + ' '
    
    return result[0:len(result)-1]