#  Re-Arrange Positive and Negative Values of Given List


def rearrange_negative_positive(arr):
    new_list = [None for _ in range(len(arr))]
    new_list_index = 0
    for i in range(len(arr)):
        if arr[i] < 0:
            new_list[new_list_index] = arr[i]
            new_list_index += 1
    for j in range(len(arr)):
        if arr[j] > 0:
            new_list[new_list_index] = arr[j]
            new_list_index += 1
    for k in range(len(arr)):
        arr[k] = new_list[k]
