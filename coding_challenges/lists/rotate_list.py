# Rotates given list by 1 position


def rotate_list(arr):
    last_element = arr[len(arr)-1]
    # Right shift
    for i in range(len(arr)-1, 0, -1):
        arr[i] = arr[i-1]
    arr[0] = last_element
    return arr
