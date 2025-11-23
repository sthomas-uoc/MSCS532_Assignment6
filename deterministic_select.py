
def mom_select(inp, k):

    if k < 1 or k > len(inp):
        raise ValueError("k is out of bounds")

    # Change to 0 based index
    k = k - 1
    return run_momselect(inp, 0, len(inp) - 1, k)

def ins_sort(inp):
    for i in range(1, len(inp)):
        val = inp[i]
        j = i - 1
        while j >= 0 and val < inp[j]:
            inp[j + 1] = inp[j]
            j -= 1
        inp[j + 1] = val

    return inp

def run_momselect(inp, start, end, k):

    if start >= end:
        return inp[end]

    # Split in to 5 groups and sort them
    groups = [ins_sort(inp[i: i+5]) for i in range(start, end + 1, 5)]

    # Medians of the groups
    medians = [groups[i][len(groups[i])//2] for i in range(len(groups))]

    pivot = run_momselect(medians, 0, len(medians) - 1, len(medians)//2)

    pivot_idx = partition_inp(inp, start, end, pivot)

    if k < pivot_idx:
        # Run momselect on the lesser than / equal values
        return run_momselect(inp, start, pivot_idx - 1, k)
    elif k > pivot_idx:
        # Run momselect on the greater than values
        return run_momselect(inp, pivot_idx + 1, end, k)
    else:
        return inp[pivot_idx]

def partition_inp(inp, start, end, pivot):

    for j in range(start, end):
        if inp[j] == pivot:
            inp[j], inp[end] = inp[end], inp[j]
            break

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


