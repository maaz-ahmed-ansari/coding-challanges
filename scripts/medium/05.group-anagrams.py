def groupAnagrams(strs):
    """
    :type strs: List[str]
    :rtype: List[List[str]]
    """
    mapped = dict()
    result = []

    for s in strs:
        s_sorted = ''.join(sorted(s))
        if s_sorted in mapped:
            mapped[s_sorted].append(s)
        else:
            mapped[s_sorted] = [s]

    for v in mapped.values():
        result.append(v)
    
    return result
    

# Example 1:

# Input: strs = ["eat","tea","tan","ate","nat","bat"]
# Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
# Example 2:

# Input: strs = [""]
# Output: [[""]]
# Example 3:

# Input: strs = ["a"]
# Output: [["a"]]