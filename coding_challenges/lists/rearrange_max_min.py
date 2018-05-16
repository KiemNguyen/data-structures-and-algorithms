# Rearrange sorted list into max min form
# first position will have the largest number,
# second position will have the smallest number,
# and the third will have second largest and so on.

def rearrange_max_min(arr):
    pointer_small = 0
    pointer_large = len(arr) - 1
    result = [None for _ in range(len(arr))]
    switch_pointer = True # Flag to switch pointers

    for i in range(len(arr)):
        if switch_pointer:
            result[i] = arr[pointer_large]
            pointer_large -= 1
        else:
            result[i] = arr[pointer_small]
            pointer_small += 1
        switch_pointer = not switch_pointer # Switch the flag

    for j in range(len(arr)):
        arr[j] = result[j]
    return arr

arr = [1, 2, 3, 4, 5, 6, 7]
print(rearrange_max_min(arr))
