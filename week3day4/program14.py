def sqrt_binary(n):
    low = 0
    high = n

    while low <= high:
        mid = (low + high) // 2

        if mid * mid == n:
            return mid
        elif mid * mid < n:
            low = mid + 1
        else:
            high = mid - 1

    return high

print(sqrt_binary(25))