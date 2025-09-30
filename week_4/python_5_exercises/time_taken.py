from functools import reduce
from time import perf_counter


def time_taken(func):
    def wrapper(*args, **kwargs):
        start = perf_counter()
        result = func(*args, **kwargs)
        end = perf_counter()
        print(f"Time taken: {end-start:.4f} seconds")
        return result

    return wrapper


@time_taken
def compute_squared_sum(n):
    l1 = range(n)
    return reduce(lambda total, x: total + (x**2), range(n), 0)


print(compute_squared_sum(10_00_000))
