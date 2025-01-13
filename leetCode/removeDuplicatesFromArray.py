class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        left = 1

        for right in range(1, len(nums)):
            if nums[right] != nums[right - 1]:
                nums[left] = nums[right]
                left += 1
        return left
    

    '''
    1. initializing left pointer to 1 
    for i in elements of array, initializing the array to start with 1
    if right pointer is not right-1 from array
    store the value of right pointer to left and increment the value of left pointer
    return the left pointer
    '''