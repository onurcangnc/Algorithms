import time

start_time = time.time()

m = int(input("Enter the first number: "))
n = int(input("Enter the second number: "))

def gcd(m, n):
    while n != 0:
        remainder = m % n
        m = n
        n = remainder
    return m

result = gcd(m, n)
print("The greatest common divisor of ", m, " and ", n, " is ", result)
end_time = time.time()
print("Time taken: ", end_time - start_time, " seconds" )