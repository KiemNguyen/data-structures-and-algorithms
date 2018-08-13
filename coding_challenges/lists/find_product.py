# Returns resulted list where each index has product of all numbers in the array
# except the number on the current index


def find_product(arr):
    product = 1  # store all previous products before i
    result = [None for _ in range(len(arr))]
    for i in range(len(arr)):
        current_product = 1  # store current product of i
        # product of values to the right of i
        for j in range(i + 1, len(arr), 1):
            current_product *= arr[j]
        # current_product * product of all values to the left of i
        result[i] = current_product * product
        product = product * arr[i]
    return result


arr = [1, 2, 3, 4]
print(find_product(arr))
