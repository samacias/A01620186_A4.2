import sys
import time

start = time.time()

filname = sys.argv[1]
numbers = []

with open(filname, 'r') as file:
    for line in file:
        try:
            number = float(line.strip())
            numbers.append(number)
        except ValueError:
            print(f"Invalid data skipped:", line.strip()) 

# Calculate statistics
# Mean
total = 0
for num in numbers:
    total += num
mean = total / len(numbers) 

# Median
n = len(numbers)

for i in range(n):
    for j in range(i + 1, n):
        if numbers[i] > numbers[j]:
            temp = numbers[i]
            numbers[i] = numbers[j]
            numbers[j] = temp

if n % 2 == 0:
    median = (numbers[n // 2 - 1] + numbers[n // 2]) / 2
else:
    median = numbers[n // 2]    

# Mode
freq = {}

for num in numbers:
    if num in freq:
        freq[num] += 1
    else:
        freq[num] = 1

max_count = 0
mode = numbers[0]

for key in freq:
    if freq[key] > max_count:
        max_count = freq[key]
        mode = key

# Variance
variance_sum = 0
for num in numbers:
    variance_sum += (num - mean) ** 2

variance = variance_sum / len(numbers)

# Standard Deviation
std_dev = variance ** 0.5

# Print results
print(f"Mean: {mean}")
print(f"Median: {median}")      
print(f"Mode: {mode}")
print(f"Variance: {variance}")
print(f"Standard Deviation: {std_dev}")
end = time.time()
print(f"Execution time: {end - start} seconds")

with open('statistics.txt', 'w') as file:
    file.write(f"Mean: {mean}\n")
    file.write(f"Median: {median}\n")
    file.write(f"Mode: {mode}\n")
    file.write(f"Variance: {variance}\n")
    file.write(f"Standard Deviation: {std_dev}\n")
    file.write(f"Execution time: {end - start} seconds\n")