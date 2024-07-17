def reverseVowels(s):
    """
    :type s: str
    :rtype: str
    """
    # Take vowels in a set/dict for lookup
    vowels = {
        "a", "e", "i", "o", "u",
        "A", "E", "I", "O", "U"
    }

    # Take char in string s in a list
    s_lst = []
    for char in s:
        s_lst.append(char)

    # Use two pointers one at start of s and one at end
    # if vowels found at both pointers then swap and iterate to next element from both pointers in respect direction
    i = 0
    j = len(s) - 1

    while i < j:
        if s[i] not in vowels and s[j] not in vowels:
            i += 1
            j -= 1
        elif s[i] not in vowels:
            i += 1
        elif s[j] not in vowels:
            j -= 1
        else:
            s_lst[i], s_lst[j] = s_lst[j], s_lst[i]
            i += 1
            j -= 1

    return "".join(s_lst)