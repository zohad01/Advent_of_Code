# Read and split ranges
with open("input3.txt", "r") as file:
    ranges = file.read().strip().split(",")

total = 0

# Function to check if a number is invalid (Part 2 rules)
def is_invalid(num):
    s = str(num)
    n = len(s)

    # Try all possible block sizes
    for k in range(1, n // 2 + 1):
        if n % k == 0:  # block must evenly divide length
            block = s[:k]
            repeat_count = n // k
            if repeat_count >= 2 and block * repeat_count == s:
                return True
    return False


# Process each range
for r in ranges:
    start_str, end_str = r.split("-")
    start = int(start_str)
    end = int(end_str)

    for num in range(start, end + 1):
        if is_invalid(num):
            total += num

print(total)
