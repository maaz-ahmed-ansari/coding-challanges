def minPairSum(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    nums = sorted(nums)

    i = 0
    j = len(nums) - 1
    result = 0

    while i < j:
        result = max(result, (nums[i] + nums[j]))
        i += 1
        j -= 1

    return result
        

# Example 1:

# Input: nums = [3,5,2,3]
# Output: 7
# Explanation: The elements can be paired up into pairs (3,3) and (5,2).
# The maximum pair sum is max(3+3, 5+2) = max(6, 7) = 7.

# Example 2:

# Input: nums = [3,5,4,2,4,6]
# Output: 8
# Explanation: The elements can be paired up into pairs (3,5), (4,4), and (6,2).
# The maximum pair sum is max(3+5, 4+4, 6+2) = max(8, 8, 8) = 8.