from typing import List


def binarySearch(nums: List[int], target: int) -> int:
    left, right = 0, len(nums) - 1

    while left <= right: 
        mid = left + ((right - left) // 2)

        if nums[mid] > target:
            right = mid - 1
        elif nums[mid] < target:
            left = mid + 1
        else:
            return mid
        
    return -1


def binarySearchRecursive(nums: List[int], target: int) -> int:

    def helper(nums, target, left, right):
        if left > right:
            return -1
        mid = left + ((right - left) // 2)

        if nums[mid] > target:
            return helper(nums, target, left, mid - 1)
        elif nums[mid] < target:
            return helper(nums, target, mid + 1, right)
        else:
            return mid

    return helper(nums, target, 0, len(nums) - 1)


# lower_bound:
# Returns the first index i where nums[i] >= target.
# If no such element exists, returns len(nums) (insertion position).

# upper_bound:
# Returns the first index i where nums[i] > target.
# If no such element exists, returns len(nums).

# Common usage:
# lower_bound(target)      -> first >= target
# upper_bound(target)      -> first > target
# lower_bound(target) - 1  -> last < target
# upper_bound(target) - 1  -> last <= target


def lower_bound(nums, target):
    left, right = 0, len(nums)

    while left < right:
        mid = left + (right - left) // 2

        if nums[mid] < target:
            left = mid + 1
        else:
            right = mid

    return left


def upper_bound(nums, target):
    left, right = 0, len(nums)

    while left < right:
        mid = left + (right - left) // 2

        if nums[mid] <= target:
            left = mid + 1
        else:
            right = mid

    return left


if __name__ == "__main__":

    # index: 0  1  2  3  4  5
    test1 = [1, 2, 3, 4, 5, 6]

    # index:  0   1   2  3  4  5   6   7  8   9   10
    test2 = [-20, -1, 0, 1, 2, 8, 10, 11, 26, 37, 108]

    print(binarySearch(test1, 1))
    print(binarySearch(test1, 2))
    print(binarySearch(test1, 6))

    print(binarySearchRecursive(test2, 2))
    print(binarySearchRecursive(test2, 8))