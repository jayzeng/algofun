from typing import (
    List,
)

# binary search
# assuming the list is sorted, if the target is less than the middle element, then the remaining elements are on the left side of the middle element.
def binary_search(nums, target):
    """
    Binary search
    :param nums: sorted list
    :param target: target value
    :return: index of target value
    """
    left = 0
    right = len(nums) - 1

    while left < right:
        mid = (left + right) >> 1
        if nums[mid] >= target:
            right = mid
        else:
            left = mid + 1

    return -1

def findMin(nums):
    if not nums or len(nums) == 0:
        return -9999
    start = 0
    end = len(nums) - 1
    while start + 1 < end:
        mid = start + (end - start) // 2
        if nums[mid] < nums[end]:
            end = mid
        else:
            start = mid
    if nums[start] < nums[end]:
        return nums[start]
    return nums[end]

def search_matrix(matrix: List[List[int]], target: int) -> bool:
    M, N = len(matrix), len(matrix[0])
    left, right = 0, M * N - 1
    while left <= right:
        mid = left + (right - left) // 2
        cur = matrix[mid // N][mid % N]
        if cur == target:
            return True
        elif cur < target:
            left = mid + 1
        else:
            right = mid - 1
    return False

def sqrt(x):
    if x < 1:
        return 0

    if x == 1:
        return 1

    left, right = 1, x
    while left + 1 < right:
        mid = (left + right) // 2
        if mid * mid <= x and (mid + 1) * (mid + 1) >= x:
            return mid
        elif mid * mid > x:
            right = mid
        else:
            left = mid

    return 0

if __name__ == "__main__":
    # print(binary_search([5,5,5,5,5,5,5,5,5,5], 5))
    # print(binary_search([1, 2, 5, 10, 100, 100], 100))
    # print(binary_search([], 100))
    # print(findMin([4, 5, 6, 7, 0, 1, 2]))

    # print(search_matrix([[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 50]], 3))
    print(sqrt(17))