"""
Math 590
Project 1
Fall 2019

Partner 1: Xichen Tan
Partner 2: Jianfei Bi
Date: 10/26/2019
"""

"""
SelectionSort
This is a in-place sorting function.
This function takes a list, and output it in ascending sorted order. 
"""


def SelectionSort(listToSort):
    # Seperate the array onto a sorted component and an unsorted component
    # with index i, i will start as 0 and increase by 1 every time
    n = len(listToSort)
    for i in range(n):
        index_min = i

        # At each iteration, traverse the whole unsorted component to find
        # the index with smallest value
        for j in range(i + 1, n):
            if listToSort[j] < listToSort[index_min]:
                index_min = j

        # Place the smallest value at the end of the sorted component
        listToSort[i], listToSort[index_min] = \
            listToSort[index_min], listToSort[i]

    return listToSort


"""
InsertionSort
This is a in-place sorting function.
This function takes a list, and output it in ascending sorted order. 
"""


def InsertionSort(listToSort):
    n = len(listToSort)
    # i is the index that separates the sorted and unsorted components.
    for i in range(1, n):
        index_to_sort = listToSort[i]
        j = i - 1

        # Search backwards to find the proper location for the element.
        # Shift the remaining sorted elements 1 index to the right.
        while j >= 0 and index_to_sort < listToSort[j]:
            listToSort[j + 1] = listToSort[j]
            j = j - 1

        # Insert the element in the proper location.
        listToSort[j + 1] = index_to_sort

    return listToSort

"""
BubbleSort
"""


def BubbleSort(listToSort):
    n = len(listToSort)
    # Set a flag variable update to record whether any swap happens at one
    # iteration.
    update = True

    # If in one iteration, no swap happened,
    # then the first n - k elements are already sorted.
    while n > 1 and update is True:
        update = False
        # At each pass, iterate through first n - k elements for comparison.
        for j in range(n - 1):
            # Compare every two adjacent elements, swap if needed.
            if listToSort[j] >= listToSort[j + 1]:
                listToSort[j], listToSort[j + 1] = \
                    listToSort[j + 1], listToSort[j]
                update = True
        n = n - 1

    return listToSort

# def optimizedBubbleSort(a):
# 	update=True
# 	n=len(a)
# 	while(update==True and n>1):
# 		update = False
# 		for i in range(len(a)-1):
# 			if a[i]>a[i+1]:
# 				a[i],a[i+1]=a[i+1],a[i]
# 				update = True
# 		n-=1
# 	return a
"""
MergeSort
"""


def MergeSort(listToSort):
    n = len(listToSort)
    # use helper function to support more input
    helper(listToSort, 0, n-1)
    return listToSort

# recursively divide array into two halves


def helper(listToSort, left, right):
    if(left >= right):
        return
    mid = left + (right - left) // 2
    helper(listToSort, left, mid)
    helper(listToSort, mid+1, right)
    # merge two halves into one sorted array
    merge(listToSort, left, mid, right)

# merge two halves into one sorted array


def merge(listToSort, left, mid, right):
    # use a extra array to store the sorted results
    helper = listToSort.copy()
    leftIndex = left
    rightIndex = mid + 1
    # put the smaller element of two halves into one extra array
    while leftIndex <= mid and rightIndex <= right:
        if helper[leftIndex] <= helper[rightIndex]:
            listToSort[left] = helper[leftIndex]
            left = left+1
            leftIndex = leftIndex+1
        else:
            listToSort[left] = helper[rightIndex]
            left = left + 1
            rightIndex = rightIndex + 1
    # handle the left elements

    while leftIndex <= mid :
        listToSort[left] = helper[leftIndex]
        left = left + 1
        leftIndex = leftIndex + 1

"""
QuickSort

Sort a list with the call QuickSort(listToSort),
or additionally specify i and j.
"""

# find the position of pivot


def partition(listToSort, left, right):
    # set the last element as pivot
    pivot = right
    # use two pointers, one start from left, one start from right
    i = left
    j = right - 1
    # swap i and j only element i is smaller than pivot
    # and element j is larger than pivot.
    while i <= j:
        if listToSort[i] < listToSort[pivot]:
            i += 1
        elif listToSort[j] >= listToSort[pivot]:
            j -= 1
        else:
            listToSort[i], listToSort[j] = \
                listToSort[j], listToSort[i]
            i += 1
            j -= 1
    # Swap the pivot to the right position
    listToSort[i], listToSort[pivot] = \
        listToSort[pivot], listToSort[i]
    # return position of pivot
    return i


def QuickSort(listToSort, i=0, j=None):
    # Set default value for j if None.
    if j == None:
        j = len(listToSort)
    # stop condition
    if i < j - 1:
        # find the position of pivot for current array
        pivot = partition(listToSort, i, j - 1)
        # recursively call QuickSort on each half
        QuickSort(listToSort, i, pivot)
        QuickSort(listToSort, pivot + 1, j)
    return listToSort

"""
Importing the testing code after function defs to ensure same references.
"""
from project1tests_updated import *

"""
Main function.
"""
if __name__ == "__main__":
    print('Testing Selection Sort')
    print()
    testingSuite(SelectionSort)
    print()
    print('Testing Insertion Sort')
    print()
    testingSuite(InsertionSort)
    print()
    print('Testing Bubble Sort')
    print()
    testingSuite(BubbleSort)
    print()
    print('Testing Merge Sort')
    print()
    testingSuite(MergeSort)
    print()
    print('Testing Quick Sort')
    print()
    testingSuite(QuickSort)
    print()
    print('DEFAULT measureTime')
    print()
    measureTime(numTrials=100)
    #measureTime(preSorted=True)
