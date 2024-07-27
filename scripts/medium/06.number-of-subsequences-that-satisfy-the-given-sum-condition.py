def numSubseq(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: int
    """
    # Take modulo since result will become very large for large sized array
    M = (10 ** 9) + 7
    n = len(nums)
    l = 0
    r = n - 1

    result = 0

    # Create array containing powers of 2 at each array index i.e. 2^index 
    power = [1]
    for i in range(1, n):
        power.append((power[i-1] * 2) % M)

    #1. Sort the array
    nums_sorted = sorted(nums)

    #2. iterate with l = 0 and r = n-1 till l <= r
    while l <= r:
        if nums_sorted[l] + nums_sorted[r] <= target:
            # if min + max <= target then result += 2 ^ (r-l)
            # and increase l
            result = (result + power[r-l]) % M
            l += 1
        else:
            # else decrease r
            r -= 1
    
    return result


# Example 1:

# Input: nums = [3,5,6,7], target = 9
# Output: 4
# Explanation: There are 4 subsequences that satisfy the condition.
# [3] -> Min value + max value <= target (3 + 3 <= 9)
# [3,5] -> (3 + 5 <= 9)
# [3,5,6] -> (3 + 6 <= 9)
# [3,6] -> (3 + 6 <= 9)

# Example 2:

# Input: nums = [3,3,6,8], target = 10
# Output: 6
# Explanation: There are 6 subsequences that satisfy the condition. (nums can have repeated numbers).
# [3] , [3] , [3,3], [3,6] , [3,6] , [3,3,6]

# Example 3:

# Input: nums = [2,3,3,4,6,7], target = 12
# Output: 61
# Explanation: There are 63 non-empty subsequences, two of them do not satisfy the condition ([6,7], [7]).
# Number of valid subsequences (63 - 2 = 61).