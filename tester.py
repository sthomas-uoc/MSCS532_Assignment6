# Tests the selection algorithms

import random
import time

import psutil
import os
import gc

from quickselect import quickselect
from deterministic_select import mom_select

def test_runner():

    nums = [2, 3, 5, 1, 4, 7]
    k_th = random.randint(1, len(nums))

    print(f"kth: {k_th}")
    
    result = sorted(nums)[k_th - 1]

    print("Starting quickselect select")
    qs_kth = quickselect(nums, k_th)

    print("Starting mom_select select")
    moms_kth = mom_select(nums, k_th)

    print(f"Quickselect selected: {qs_kth}, expected: {result}, kth: {k_th}")

    assert qs_kth == result

    print("Starting mom_select select")
    moms_kth = mom_select(nums, k_th)

    print(f"MoM select selected: {moms_kth}, expected: {result}, kth: {k_th}")

    assert moms_kth == result

    nums = [5, 3, 8, 5, 2, 9, 5, 3, 1, 8, 7, 6, 2, 3, 4, 8, 9, 1, 6, 0]

    k_th = random.randint(1, len(nums))

    print(f"kth: {k_th}")
    
    result = sorted(nums)[k_th - 1]

    print("Starting quickselect select")
    qs_kth = quickselect(nums, k_th)

    print(f"Quickselect selected: {qs_kth}, expected: {result}, kth: {k_th}")

    assert qs_kth == result

    print("Starting mom_select select")
    moms_kth = mom_select(nums, k_th)

    print(f"MoM select selected: {moms_kth}, expected: {result}, kth: {k_th}")

    assert moms_kth == result

    # Input sizes
    sizes = [ 10, 50, 100, 200, 500]

    # Data sort options
    input_opts = ["rand", "sorted", "rev_sorted"]
    # input_opts = ["rev_sorted"]

    # Get PID for capturing stats
    pid = os.getpid()

    # Disable global garbage collection
    gc.disable()

    for size in sizes:
        nums = gen_random_numbers(size, 0, 5000000)

        k_th = random.randint(1, len(nums))
    
        # print(f"kth: {k_th}")
        
        result = sorted(nums)[k_th - 1]
    
        for input_opt in input_opts:
            if input_opt == "rand":
                nums = nums
            elif input_opt == "sorted":
                nums.sort()
            else:
                nums.sort()
                nums.reverse()

            # print(f"nums: {nums}")

            orig_nums = nums[:len(nums)]
    
            # Run garbage collection before running quickselect
            gc.collect()

            memory_usage_before = psutil.Process(pid).memory_info().rss
            
            # Capture time
            start_time = time.time()
            
            # print("Starting quickselect select")
            qs_kth = quickselect(nums, k_th)
        
            # print(f"Quickselect selected: {qs_kth}, expected: {result}, kth: {k_th}")
        
            end_time = time.time()
        
            memory_usage_after = psutil.Process(pid).memory_info().rss
            
            print(f"Quickselect selected {size} {input_opt} nums in {(end_time - start_time):.6f} seconds using {(memory_usage_after - memory_usage_before)/ (1024 * 1024)} MB memory")
        
            assert qs_kth == result

            nums = orig_nums[:len(nums)]
            
            # print(f"nums: {nums}")
            # Run garbage collection before running momselect 
            gc.collect()

            mem_usage_before = psutil.Process(pid).memory_info().rss
            
            # Capture time
            start_time = time.time()
            
            # print("Starting mom_select select")
            moms_kth = mom_select(nums, k_th)
        
            # print(f"MoM select selected: {moms_kth}, expected: {result}, kth: {k_th}")
        
            end_time = time.time()
        
            mem_usage_after = psutil.Process(pid).memory_info().rss
            
            print(f"Mom select selected {size} {input_opt} nums in {(end_time - start_time):6f} seconds using {(memory_usage_after - memory_usage_before)/ (1024 * 1024)} MB memory")
        
            assert moms_kth == result
            

    print(f"Ok")

# Function that returns requested number of random numbers in a range
def gen_random_numbers(count, min, max):
    return [random.randint(min, max) for _ in range(count)]

if __name__ == "__main__":
    test_runner()
