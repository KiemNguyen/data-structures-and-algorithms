# Returns minimum value from given list


def find_minimum(arr):
    minimum = arr[0]
    for i in range(len(arr)):
        if arr[i] < minimum:
            minimum = arr[i]
    return minimum
