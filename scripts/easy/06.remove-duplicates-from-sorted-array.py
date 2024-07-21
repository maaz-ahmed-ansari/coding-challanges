def removeDuplicates(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    len_nums = len(nums)
    if len_nums == 1:
        return 1
    
    i = 0
    j = 1
    while j < len_nums:
        if nums[j] <= nums[i]:
            j += 1
        else:
            i += 1
            nums[i] = nums[j]
            j += 1
    
    return i + 1