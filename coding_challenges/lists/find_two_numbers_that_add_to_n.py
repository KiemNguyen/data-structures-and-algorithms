# Return 2 elements of arr that sum to the given value


def find_sum(arr, value):
    result = []
    first_num = 0
    # Sort the list
    sort_nums(arr)

    # Assign pointer1 at the start and pointer2 at the end
    pointer1 = 0
    pointer2 = len(arr) - 1

    while pointer1 != pointer2:
        # Calculate sum of pointer1 + pointer2
        sum = arr[pointer1] + arr[pointer2]
        # If sum of two pointers is less than the given value, move pointer1 to the right
        if (sum < value):
            pointer1 += 1
        elif (sum > value): # If sum of two pointers is greater than the given value, move pointer2 to the left
            pointer2 -= 1
        else:
            result.append(arr[pointer1])
            result.append(arr[pointer2])
            return result


# Helper sort function


def sort_nums(arr):
    for i in range(len(arr)-1):
        index = i
        for j in range(i+1,len(arr),1):
            if (arr[j] < arr[index]):
                index = j
        smaller_num = arr[index]
        arr[index] = arr[i]
        arr[i] = smaller_num


