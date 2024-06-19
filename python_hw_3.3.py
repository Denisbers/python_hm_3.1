def sep(arr):
    i = len(arr) - len(arr) // 2
    return [arr[:i], arr[i:]]

my_list = [1, 2, 3, 4, 5, 6]
print(sep(my_list))