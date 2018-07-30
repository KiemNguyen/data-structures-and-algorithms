# Returns second maximum value from given list

def find_second_largest(arr):
    largest = 0
    second_largest = 0
    for i in range(len(arr)):
        if arr[i] > largest:
            second_largest = largest
            largest = arr[i]
        elif arr[i] > second_largest:
            second_largest = arr[i]
    return second_largest
