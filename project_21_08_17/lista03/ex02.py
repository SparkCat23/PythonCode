def same_first_last(nums):
    l = len(nums)
    if l == 0:
        return False
    elif l == 1:
        return True
    elif l > 1:
        if nums[0] == nums[l-1]:
            return True
        else:
            return False
