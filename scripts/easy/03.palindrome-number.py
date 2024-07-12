def isPalindrome(x):
    """
    :type x: int
    :rtype: bool
    """
    # Approach 1 -- converting to string
    if x < 0:
        return False
    
    return str(x) == str(x)[::-1]

    # Approach 2 -- without converting to string ----------------
    if x < 0:
        return False
    
    num = x
    reversed = 0

    while x > 0:
        reversed = (reversed * 10) + (x % 10)
        x //= 10
    
    return num == reversed

    # -----------------------------------------
    # Approach 3 -- Using string conversion and comparision via two pointer
    if x < 0:
        return False
    
    x_str = str(x)

    i = 0
    j = len(x_str) - 1

    while(i < j):
        if x_str[i] != x_str[j]:
            return False
        
        i += 1
        j -= 1
    
    return True