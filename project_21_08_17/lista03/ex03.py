def common_end(a,b):
    aLast = (len(a)-1)
    bLast = (len(b)-1)
    if a[0] == b[0] or a[aLast] == b[bLast]:
        return True
    else:
        return False