def removeDuplicates(self, nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    # get len(nums)
    nums_len = len(nums)
    # if size of nums is 1 --> return 1 as only 1 element
    if nums_len == 1:
        return 1
    
    # else iterate over nums using two pointers
    # initialize fist pointer at 0
    i = 0
    # iterate over nums starting with 1 index till end  --> this is second pointer  
    for j in range(1, nums_len):
        # compare if second pointer content is > first pointers content
        if nums[j] <= nums[i]:
            # if not greater than, go to next element using 2nd pointer
            continue
        # if greater then increase first pointer and assign it with values of second pointer's content
        else:
            i += 1
            nums[i] = nums[j]
        # and go to next element and repeat untill last element reached in 2nd pointer
    
    return i + 1