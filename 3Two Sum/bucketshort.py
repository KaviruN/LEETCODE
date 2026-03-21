import time
import tracemalloc

nums = [3,3]

target = 6

def measure(func, *args, **kwargs):
    tracemalloc.start()
    start = time.time()

    result = func(*args, **kwargs)

    end = time.time()
    current, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()

    print(f"Execution time: {end - start:.6f} sec")
    print(f"Peak memory usage: {peak / 10**6:.3f} MB")
    return result


def towSum(nums, target):
    numhash = {} #val:index {3: 0, 4: 1, 5: 2, 6: 3}
    for i, n in enumerate(nums):
        diff = target - n
        if diff in numhash:
            return [numhash[diff], i]
        numhash[n] = i # if n:i add to hashmap to after condition checking start is emty  go like {} then add n=3:i=0 and then in i=1 mean n=3 but i=1 so n=3:1i



measure(towSum(nums, target))
print(towSum(nums, target))

# a = {3: 0, 4: 1, 5: 2, 6: 3}

# if 3 in a:
#     print(f'3:{a[3]}')