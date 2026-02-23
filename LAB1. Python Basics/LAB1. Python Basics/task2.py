def increas(arr):
    return all(x < y for x, y in zip(arr, arr[1:]))

