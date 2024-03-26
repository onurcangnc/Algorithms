import time

start_time = time.time()
A = [8,3,9,7,2]

def frequencyCount(A):
    return sum(A)

print(frequencyCount(A))
end_time = time.time()
execution_time = end_time - start_time
print(execution_time)
