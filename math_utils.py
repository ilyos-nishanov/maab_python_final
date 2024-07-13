def is_prime(n):
    num = n-1
    while num > 1:
        if n % num == 0:
            return False
        num -= 1
    return True