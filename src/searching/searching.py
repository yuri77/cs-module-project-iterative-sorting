def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i

    return -1   # not found


# Write an iterative implementation of Binary Search
def binary_search(arr, target):
    l = 0
    r = len(arr)-1

    while l <= r:
        mid = l+(r-l)//2
        # print("mid", mid)
        if arr[mid] == target:
            return mid
        elif arr[mid] > target:
            r = mid-1
        else:
            l = mid+1
    return -1


test = [0, 1, 5, 6, 13, 8, 49]
print(binary_search(test, 1))
print(binary_search(test, 8))

#recursive implementation#
# def binary_search(arr, target):
#     if not len(arr):
#         return -1
#     else:
#         mid = len(arr)//2
#         if arr[mid] == target:
#             return True
#         else:
#             if target > arr[mid]:
#                 return binary_search(arr[mid+1:], target)
#             else:
#                 return binary_search(arr[:mid], target)

# recursive implementation - returning the index of the item
# def binary_search(arr, l, r, target):
#     if r >= 1:
#         mid = l + (r-l)//2
#         if arr[mid] == target:
#             return mid
#         elif arr[mid] > target:
#             return binary_search(arr, l, mid-1, target)
#         else:
#             return binary_search(arr, mid+1, r, target)
#     else:
#         return -1


# test = [0, 1, 5, 6, 13, 8, 49]
# print(binary_search(test, 0, len(test)-1, 1))
# print(binary_search(test, 0, len(test)-1, 8))
