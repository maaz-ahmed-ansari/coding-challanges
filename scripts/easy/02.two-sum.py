def twoSum(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """

    map = dict()

    for idx in range(len(nums)):
        required = target - nums[idx]

        if required in map:
            return [idx, map[required]]
        
        map[nums[idx]] = idx
    
    return []