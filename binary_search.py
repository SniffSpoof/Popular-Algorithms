def binary_search(arr, x):
    left = 0
    right = len(arr) - 1
 
    while left <= right:
 
        mid = (right + left) // 2
 
        if arr[mid] < x:
            left = mid + 1
 
        elif arr[mid] > x:
            right = mid - 1
 
        else:
            return mid
 
    return -1
 
arr = [2, 3, 4, 10, 11, 15, 19, 20, 24, 40]
x = 24
 
result = binary_search(arr, x)
 
if result != -1:
    print("Элемент найден, индекс = ", str(result))
else:
    print("Элемент отсутствует в массиве")
