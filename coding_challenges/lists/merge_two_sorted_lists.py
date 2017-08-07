# Merge arr1 and arr2 and return resulted list
def mergeArrays(arr1, arr2):
    index_arr1 = 0
    index_arr2 = 0
    index_result = 0
    result = [None for _ in range(len(arr1) + len(arr2))]

    # Traverse both lists and insert smaller value into result list
    while (index_arr1 < len(arr1)) and (index_arr2 < len(arr2)):
        if (arr1[index_arr1] < arr2[index_arr2]):
            result[index_result] = arr1[index_arr1]
            index_result += 1
            index_arr1 += 1
        else:
            result[index_result] = arr2[index_arr2]
            index_result += 1
            index_arr2 += 1

    # If one list is traversed completely, while other list is left then
    # copy all the remaining elements into result list
    while (index_arr1 < len(arr1)):
        result[index_result] = arr1[index_arr1]
        index_result += 1
        index_arr1 += 1
    while (index_arr2 < len(arr2)):
        result[index_result] = arr2[index_arr2]
        index_result += 1
        index_arr2 += 1
    return result