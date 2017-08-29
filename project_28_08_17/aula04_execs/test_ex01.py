
def MDC(a,b):
    m=a
    n=b
    while m != 0:
        m, n = n % m, m

    return n

def test_ex01():
    assert MDC(2,4) == 2
    assert MDC(5,25) == 5
    assert MDC(72,64) == 8
