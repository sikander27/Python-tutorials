def bubbleSort(arr):
    """
    compares adjacent element
    time-complexity = o(n2)
    space-complexity = o(2)
    """
    for i in range(len(arr)):
        swapped = False
        for j in range(0, len(arr) - i - 1):  # -1 because we are lookin at j + 1 in next line
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
        if not swapped:
            break
    return arr


def insertionSort(arr):
    """
    Insertion sort is a sorting algorithm that places an unsorted element 
    at its suitable place in each iteration.
    Insertion sort works similarly as we sort cards in our hand in a card game.
    ime-complexity = o(n2)
    space-complexity = o(1)
    """
    for step in range(1, len(arr)):
        key = arr[step]
        j = step - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j = j - 1
        arr[j + 1] = key
        print(arr)
    return arr


def mergeSort(arr):
    """
    Uses Divide and Conquere algo and then combines
    time complexity : O(nlogn)
    space complexity : O(n)
    """
    if len(arr) > 1:
        half = len(arr) // 2
        left = arr[:half]
        right = arr[half:]

        mergeSort(left)
        mergeSort(right)

        i = j = k = 0

        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                arr[k] = left[i]
                i += 1
            else:
                arr[k] = right[j]
                j += 1
            k += 1

        while i < len(left):
            arr[k] = left[i]
            i += 1
            k += 1
        
        while j < len(right):
            arr[k] = right[j]
            j += 1
            k += 1


def partition(arr, low, high):
    print("--------------------")
    pivot = arr[high]

    i = low - 1
    for j in range(low, high):
        print(arr)
        if arr[j] <= pivot:
            i = i + 1

            arr[i], arr[j] = arr[j], arr[i]
    import pdb; pdb.set_trace()
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    print(i + 1)
    return i + 1


def quickSort(arr, low, high):
    """
    Best	O(n*log n)
    Worst	O(n2)
    Space Complexity	O(log n)
    """
    if low < high:

        pi = partition(arr, low, high)

        quickSort(arr, low, pi - 1)
        quickSort(arr, pi + 1, high)



arr = [7, 8, 3, 0, 6]
quickSort(arr, 0, len(arr)-1 )
print(arr)
