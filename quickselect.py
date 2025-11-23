import random

def quickselect(inp, k):

    if k < 1 or k > len(inp):
        raise ValueError("k is out of bounds")

    # Change to 0 based index
    k = k - 1
    return run_quickselect(inp, 0, len(inp) - 1, k)

def run_quickselect(inp, start, end, k):

    if start >= end:
        return inp[end]

    pivot_idx = partition_inp(inp, start, end)

    if k < pivot_idx:
        # Run Quickselect on the lesser than / equal values
        return run_quickselect(inp, start, pivot_idx - 1, k)
    elif k > pivot_idx:
        # Run Quickselect on the greater than values
        return run_quickselect(inp, pivot_idx + 1, end, k)
    else:
        return inp[pivot_idx]

def partition_inp(inp, start, end):

    # Divide using a randomized pivot
    pivot_idx = random.randint(start, end)

    # Set the pivot as the last element
    inp[pivot_idx], inp[end] = inp[end], inp[pivot_idx]

    # The pivot value
    pivot = inp[end]

    # Start location after which to insert less than values
    i = start - 1

    for j in range(start, end):
        if inp[j] <= pivot:
            i += 1

            # Swap the lower / equal value to the insert location
            inp[i], inp[j] = inp[j], inp[i]

    # Move the pivot to the location where it is greater than the smaller / equal values
    inp[i + 1], inp[end] = inp[end], inp[i + 1]

    # Return the pivot index so that the lesser than and greater than values can be sorted again
    return i + 1

