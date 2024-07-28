def numberOfGoodPartitions(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    # Map last index of appearance of the number in nums
    mapped = {
        nums[i]: i for i in range(len(nums))
    }
    
    # Take 0th index to i and max index for first element appeared in nums
    i = 0
    j = mapped[nums[i]]
    result = 1
    
    # go from 0 to n-1 for i
    for i in range(len(nums)):
        # check if i > j
        if i > j:
            # if yes -> one partition found -> 2 possiblilities with remaining subarray
            # Multiply result with 2 and take it's modulo
            result = (result * 2) % (10 ** 9 + 7)
        # assig j with maximum index of nums[i] or existing j
        j = max(j, mapped[nums[i]])

    return result


# Example 1:

# Input: nums = [1,2,3,4]
# Output: 8
# Explanation: The 8 possible good partitions are: ([1], [2], [3], [4]), ([1], [2], [3,4]), ([1], [2,3], [4]), ([1], [2,3,4]), ([1,2], [3], [4]), ([1,2], [3,4]), ([1,2,3], [4]), and ([1,2,3,4]).

# Example 2:

# Input: nums = [1,1,1,1]
# Output: 1
# Explanation: The only possible good partition is: ([1,1,1,1]).

# Example 3:

# Input: nums = [1,2,1,3]
# Output: 2
# Explanation: The 2 possible good partitions are: ([1,2,1], [3]) and ([1,2,1,3]).