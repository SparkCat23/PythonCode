def maior_ponta(nums):
    a = nums[0]
    b = nums[-1]
    n = len(nums)
    l = []
    if a > b:
        for x in range(0,n):
            l.append(a)
        return l
    else:
        for x in range(0,n):
            l.append(b)
        return l