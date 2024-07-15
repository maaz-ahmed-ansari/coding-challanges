def sortArray(nums):
    """
    :type nums: List[int]
    :rtype: List[int]
    """
    map = dict()
    result = []

    # map the number and it's occurences
    for num in nums:
        if num not in map:
            map[num] = 1
        else:
            map[num] += 1
    
    # Go from minimum element to (including) maximum element in given list
    # At each iteration check if that num/element is found in mapped dictionar
    # If found then add into result, the number of times it appears in given list
    for x in range(min(nums), max(nums)+1):
        if x in map:
            result.extend(
                [x] * map[x]
            )
    
    return result


    # Slight Difference
    map = dict()
    # result = []

    for num in nums:
        if num not in map:
            map[num] = 1
        else:
            map[num] += 1

    i = 0
    for x in range(min(nums), max(nums)+1):
        if x in map:
            while map[x] > 0:
                nums[i] = x
                i += 1
                map[num] -= 1
    
    return nums