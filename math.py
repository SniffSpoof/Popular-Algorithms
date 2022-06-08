def fast_pow(a, b):
    if b == 0:
        return 1
    if b == -1:
        return 1. / a
    p = fast_pow(a, b // 2)
    p *= p
    if b % 2:
        p *= a
    return p
	
