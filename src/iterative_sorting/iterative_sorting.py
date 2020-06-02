# TO-DO: Complete the selection_sort() function below
def selection_sort(arr):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        cur_index = i
        smallest_index = cur_index
        # print("i", i)  # Your code here
        for j in range(i+1, len(arr)):
            if arr[j] < arr[smallest_index]:
                smallest_index = j
        arr[cur_index], arr[smallest_index] = arr[smallest_index], arr[cur_index]

        # print("arr", arr)

    return arr


result = selection_sort([1, 5, 8, 4, 2, 9, 6, 0, 3, 7])
print(result)

# TO-DO:  implement the Bubble Sort function below


def bubble_sort(arr):
    swap = False
    l = len(arr)

    for i in range(l):
        # print("i", i)
        # last ith element is already sorted- largest element bubble down (swapped ) to the end at each iteration
        for j in range(l-1-i):
            # print("j", j)
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swap = True
        if not swap:
            break
        # if not swap:
        #     break

    return arr


# result = bubble_sort([1, 2, 3])
# print(result)
'''
STRETCH: implement the Count Sort function below

Counting sort is a sorting algorithm that works on a set of data where
we specifically know the maximum value that can exist in that set of
data. The idea behind this algorithm then is that we can create "buckets"
from 0 up to the max value. This is most easily done by initializing an
array of 0s whose length is the max value + 1 (why do we need this "+ 1"?).

Each buckets[i] then is responsible for keeping track of how many times 
we've seen `i` in the input set of data as we iterate through it.
Once we know exactly how many times each piece of data in the input set
showed up, we can construct a sorted set of the input data from the 
buckets. 

What is the time and space complexity of the counting sort algorithm?
'''


def counting_sort(arr, maximum=None):
    # Your code here

    return arr
