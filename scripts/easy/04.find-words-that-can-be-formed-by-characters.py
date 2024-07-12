def countCharacters(words, chars):
    """
    :type words: List[str]
    :type chars: str
    :rtype: int
    """
    # track characters in chars with number of time each distinct char appear
    chars_dict = dict()

    for char in chars:
        if char not in chars_dict:
            chars_dict[char] = 1
        else:
            chars_dict[char] += 1
    
    # Iterate over each word and compare with chars_dict
    # if any char in word is not found in chars_dict then this is not good string
    # If number of time a character in word is greater than number of times it appreas in chars_dict then this is not good string
    # If these checks passes then add len(word) to result 
    # at the end return result

    result = 0

    for word in words:
        word_dict = dict()

        for char in word:
            is_skip = False
    
            if char not in chars_dict:
                is_skip = True
                break
            elif char not in word_dict:
                word_dict[char] = 1
            else:
                word_dict[char] += 1
            
            if word_dict[char] > chars_dict[char]:
                is_skip = True
                break

        if is_skip:
            continue
        
        result += len(word) 
    
    return result


# Example 1:

# Input: words = ["cat","bt","hat","tree"], chars = "atach"
# Output: 6
# Explanation: The strings that can be formed are "cat" and "hat" so the answer is 3 + 3 = 6.
# Example 2:

# Input: words = ["hello","world","leetcode"], chars = "welldonehoneyr"
# Output: 10
# Explanation: The strings that can be formed are "hello" and "world" so the answer is 5 + 5 = 10.