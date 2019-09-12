def merge_sort(arr):

    if len(arr) <= 1:
        return arr

    midpoint = int(len(arr) / 2)

    left, right = merge_sort(arr[:midpoint]), merge_sort(arr[midpoint:])

    return merge(left, right)


def merge(left, right):

    result = []
    lp = rp = 0

    while lp < len(left) and rp < len(right):

        if left[lp] < right[rp]:

            result.append(left[lp])
            lp += 1

        else:

            result.append(right[rp])
            rp += 1

    result.extend(left[lp:])
    result.extend(right[rp:])

    return result



array = [5, 5, 3, 6, 77, 4, 9, 4, 3, 2, 1]
print(array)

print(merge_sort(array))

