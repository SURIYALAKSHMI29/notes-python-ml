import tracemalloc
from time import perf_counter as pc

with open("large_file.txt", "w") as f:
    for i in range(1, 10_000_001):
        f.write(f"Line {i}\n")


def read_all(file):
    with open(file, "r") as f:
        return f.readlines()


def yield_lines(file):
    with open(file, "r") as f:
        for line in f:
            yield line


file = "large_file.txt"

# read all lines at once
tracemalloc.start()
start = pc()
lines = read_all(file)
end = pc()
current, peak = tracemalloc.get_traced_memory()
print(f"read_all_lines -> Time: {end-start:.4f}s, Memory: {peak/1024/1024:.2f} MB")
tracemalloc.stop()

print()

# read lines using generator
tracemalloc.start()
start = pc()
for line in yield_lines(file):
    pass
end = pc()
current, peak = tracemalloc.get_traced_memory()
print(f"yield lines -> Time: {end-start:.4f}s, Memory: {peak/1024/1024:.2f} MB")
tracemalloc.stop()

# Output:
# when file size is 10_000_001
# read_all_lines -> Time: 2.5501s, Memory: 598.91 MB
# yield lines -> Time: 2.3569s, Memory: 0.02 MB

# when file size is 100_001
# read_all_lines -> Time: 0.0237s, Memory: 5.73 MB
# yield lines -> Time: 0.0218s, Memory: 0.02 MB

# Explanation:
# read_all() will consume huge memory because f.readlines() loads everything into RAM
# yield_lines() will consume very little memory because it reads one line at a time

# peak/1024/1024 -> converting bytes into mb
# bytes/1024 -> KB/1024 -> MB
