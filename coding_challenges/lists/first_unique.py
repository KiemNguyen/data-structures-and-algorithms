# Returns first unique integer from list


def first_unique(arr):
    is_repeated = False
    for i in range(len(arr)):
        for j in range(i+1,len(arr),1):
            if arr[i] == arr[j]:
                is_repeated = True
        if is_repeated is False:
            return arr[i]
        is_repeated = False
