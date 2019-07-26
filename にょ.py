def has99(nums):
    for i in range(0,len(nums)-1):
        if nums[i] == nums[i+1]==9:
            return True
        else:
            continue
    return False
    
