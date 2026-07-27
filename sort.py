import random
from typing import List


# | Algorithm      | Best       | Average    | Worst      | Stable |
# | -------------- | ---------- | ---------- | ---------- | ------ |
#
# | Bubble Sort    | O(n)       | O(n²)      | O(n²)      | Y      |
# | Selection Sort | O(n²)      | O(n²)      | O(n²)      | N      |
# | Insertion Sort | O(n)       | O(n²)      | O(n²)      | Y      |
#
# | Merge Sort     | O(n log n) | O(n log n) | O(n log n) | Y      |
# | Quick Sort     | O(n log n) | O(n log n) | O(n²)      | N      |
# | Heap Sort      | O(n log n) | O(n log n) | O(n log n) | N      |


# Bubble Sort
def bubbleSort(nums: List[int]) -> None:
    n = len(nums)
    for i in range(n):
        swapped = False
        for j in range(n - i - 1):
            if nums[j] > nums[j + 1]:
                nums[j], nums[j + 1] = nums[j + 1], nums[j]
                swapped = True
        if not swapped:  # already sorted, stop early
            break
    
    print(nums)


# Selection Sort
# Find the minimum element, then put it in the correct position.
def selectionSort(nums: List[int]) -> None:
    n = len(nums)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if nums[j] < nums[min_idx]:
                min_idx = j
        nums[i], nums[min_idx] = nums[min_idx], nums[i]
    print(nums)


# Insertion Sort
# Keep the left part sorted, and insert the next element into the correct position.
def insertionSort(nums: List[int]) -> None:
    n = len(nums)
    for i in range(1, n):
        key = nums[i]
        j = i - 1
        while j >= 0 and nums[j] > key:
            nums[j + 1] = nums[j]
            j -= 1
        nums[j + 1] = key
    print(nums)


# Merge Sort
def mergeSort(nums):
    if len(nums) <= 1:
        return nums

    mid = len(nums) // 2

    left = mergeSort(nums[:mid])
    right = mergeSort(nums[mid:])

    return merge(left, right)


def merge(left, right):
    res = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            res.append(left[i])
            i += 1
        else:
            res.append(right[j])
            j += 1

    res.extend(left[i:])
    res.extend(right[j:])

    return res


# Quick Sort
def quickSort(nums):
    def partition(left, right):
        pivot = nums[right]
        i = left

        for j in range(left, right):
            if nums[j] < pivot:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1

        nums[i], nums[right] = nums[right], nums[i]
        return i

    def sort(left, right):
        if left >= right:
            return

        pivot = partition(left, right)

        sort(left, pivot - 1)
        sort(pivot + 1, right)

    sort(0, len(nums) - 1)


def _randomNums(length: int) -> None:
    if length <= 0:
        return []

    nums = list(range(length))
    random.shuffle(nums)

    return nums


if __name__ == "__main__":
    nums = _randomNums(20)

    bubbleSort(nums.copy())
    selectionSort(nums.copy())
    insertionSort(nums.copy())

    mergeSort(nums.copy())
    quickSort(nums.copy())