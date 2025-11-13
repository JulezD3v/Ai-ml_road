def binary_search(arr, low, high, key):
    if low > high:
        return -1  # Base case: not found

    mid = (low + high) // 2  

    if arr[mid] == key:
        return mid
    elif key < arr[mid]:
        return binary_search(arr, low, mid - 1, key)
    else:
        return binary_search(arr, mid + 1, high, key)

# Example usage
arr = [1, 3, 5, 7, 9, 11, 13]
key = 7
result = binary_search(arr, 0, len(arr) - 1, key)

print("Element found at index:", result)
