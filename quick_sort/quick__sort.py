def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[0]
        left = []
        right = []
        for i in arr[1:]:
            if i < pivot:
                left.append(i)
            else:
                right.append(i)
        return quick_sort(left) + [pivot] + quick_sort(right)

# Example usage:
arr = [64, 34, 25, 12, 22, 11, 90]
sorted_arr = quick_sort(arr)
print("Sorted array is:", sorted_arr)
