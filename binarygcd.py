import time

start_time = time.time()

m = int(input("Enter the first number: "))
n = int(input("Enter the second number: "))

def gcd(m, n):
    # Base cases
    if m == 0:
        return n
    if n == 0:
        return m

    # If both m and n are even
    if m % 2 == 0 and n % 2 == 0:
        return 2 * gcd(m // 2, n // 2)

    # If m is even and n is odd
    elif m % 2 == 0:
        return gcd(m // 2, n)

    # If m is odd and n is even
    elif n % 2 == 0:
        return gcd(m, n // 2)

    # If both m and n are odd and m > n
    elif m >= n:
        return gcd((m - n) // 2, n)

    # If both m and n are odd and m < n
    else:
        return gcd(m, (n - m) // 2)

result = gcd(m, n)
print("The greatest common divisor of", m, "and", n, "is", result)
end_time = time.time()
print("Time taken:", end_time - start_time, "seconds")
