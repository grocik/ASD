import random
import sys
from datetime import datetime

sys.setrecursionlimit(9999999)

#>>>>>>>>quickSort>>>>>>>>>
def partition(arr, p, r):
    x = arr[r]
    i = (p - 1)
    for j in range(p, r):
        if (arr[j] <= x):
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[r] = arr[r], arr[i + 1]
    return (i + 1)
def quickSort(arr, p, r):
    if (p < r):
        pi = partition(arr, p, r)

        quickSort(arr, p, pi - 1)
        quickSort(arr, pi + 1, r)
#<<<<<<<quickSort<<<<<<<<

#>>>>>>>>>>heapSort>>>>>>
def heapify(arr, n, i):
    largest = i
    l = 2 * i + 1
    r = 2 * i + 2

    if l < n and arr[largest] < arr[l]:
        largest = l
    if r < n and arr[largest] < arr[r]:
        largest = r
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)
def heapSort(arr):
    n = len(arr)
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0)
#<<<<<<heapSort<<<<<<<<<

#>>>>>>bubbleSort>>>>>>>

def bubbleSort(A):
    n = len(A)
    for i in range(n - 1):
        for j in range(0, n - i - 1):
            if A[j] > A[j + 1]:
                A[j], A[j + 1] = A[j + 1], A[j]


#<<<<<<bubbleSort<<<<<<

#>>>>>>MergeSort>>>>>>>
def mergeSort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        L = arr[:mid]
        R = arr[mid:]
        mergeSort(L)
        mergeSort(R)
        i = j = k = 0
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1
        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1
        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1
#<<<<<<MergeSort<<<<<<<

#>>>>>>ArrayPrinting>>>>>>>>>
''' Function to print array '''
def printArray(arr, size):
    for i in range(size):
        print(arr[i], end=" ")
    print()
#<<<<<<ArrayPrinting<<<<<<<<<

def inputFileReader(file, array):
    for line in file:
        line = line.strip(" ")
        line = line.strip("ď»ż")
        line = line.strip(")")
        line = line.strip("(")
        values = line.split(",")
        for v in values:
            array.append(int(v))



if __name__ == '__main__':

    randomArr = []
    reversedArr = []
    sortedArr = []

    quickRandom = []
    quicReversed = []
    quickSorted = []

    heapRandom = []
    heapReversed = []
    heapSorted = []

    bubbleRandom = []
    bubbleReversed = []
    bubbleSorted = []

    mergeRandom = []
    mergeReversed = []
    mergeSorted = []

    inputFileReader(open("100kRandom-array.txt", "r"), randomArr)
    inputFileReader(open("100kReversed-array.txt", "r"), reversedArr)
    inputFileReader(open("100kSorted-array.txt", "r"), sortedArr)

    inputFileReader(open("100kRandom-array.txt", "r"), heapRandom)
    inputFileReader(open("100kReversed-array.txt", "r"), heapReversed)
    inputFileReader(open("100kSorted-array.txt", "r"), heapSorted)

    inputFileReader(open("100kRandom-array.txt", "r"), bubbleRandom)
    inputFileReader(open("100kReversed-array.txt", "r"), bubbleReversed)
    inputFileReader(open("100kSorted-array.txt", "r"), bubbleSorted)

    inputFileReader(open("100kRandom-array.txt", "r"), mergeRandom)
    inputFileReader(open("100kReversed-array.txt", "r"), mergeReversed)
    inputFileReader(open("100kSorted-array.txt", "r"), mergeSorted)

    nsorted = len(sortedArr)
    nrandom = len(randomArr)
    nreversed = len(reversedArr)
#-----------QuickSort-------------
    #commented because of out of memory error
    #startTime = datetime.now()
    #quickSort(sortedArr, 0, nsorted - 1)
    #time = datetime.now() - startTime
    #print("QuickSort ", "sorted ", time)

    startTime = datetime.now()
    quickSort(randomArr, 0, nrandom - 1)
    time = datetime.now() - startTime
    print("QuickSort ", "random ", time)

    # commented because of out of memory error
   # startTime = datetime.now()
   # quickSort(reversedArr, 0, nreversed - 1)
   # time = datetime.now() - startTime
   # print("QuickSort ", "reversed ", time)
# -----------heapSort-------------
    startTime = datetime.now()
    heapSort(heapSorted)
    time = datetime.now() - startTime
    print("heapSort ", "sorted ", time)

    startTime = datetime.now()
    heapSort(heapRandom)
    time = datetime.now() - startTime
    print("heapSort ", "random ", time)

    startTime = datetime.now()
    heapSort(heapReversed)
    time =datetime.now() - startTime
    print("heapSort ","reversed ",time)

#---------------MergeSort---------------
    startTime = datetime.now()
    mergeSort(mergeSorted)
    time = datetime.now() - startTime
    print("merge ", "sorted ", time)

    startTime = datetime.now()
    mergeSort(mergeRandom)
    time = datetime.now() - startTime
    print("merge ", "random ", time)

    startTime = datetime.now()
    mergeSort(mergeReversed)
    time = datetime.now() - startTime
    print("merge ", "reversed ", time)

#-------------BubbleSort--------------
    startTime = datetime.now()
    bubbleSort(bubbleSorted)
    time = datetime.now() - startTime
    print("bubbleSort ", "sorted ", time)

    startTime = datetime.now()
    bubbleSort(bubbleRandom)
    time = datetime.now() - startTime
    print("bubbleSort ", "random ", time)

    startTime = datetime.now()
    bubbleSort(bubbleReversed)
    time = datetime.now() - startTime
    print("bubbleSort ", "reversed ", time)