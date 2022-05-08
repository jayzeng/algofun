from operator import le
import unittest

# selection sort
# time: O(n^2)
# space: 
def selection_sort(nums):
    # 1. finds the smallest element in the list
    # 2. swaps it with the first unsorted element
    n = len(nums)
    for i in range(n - 1):
        min_idx = i

        for j in range(i + 1, n):
            if nums[j] < nums[min_idx]:
                min_idx = j

        nums[i], nums[min_idx] = nums[min_idx], nums[i]

    return nums

class TestSort(unittest.TestCase):
    def lst_equal(self, l1, l2):
        from functools import reduce
        is_same = None

        if not l1 and not l2:
            is_same = True
        else:
            is_same = reduce(lambda x, y: x and y, map(lambda x, y: x == y, l1, l2))

        self.assertTrue(is_same)

    def test_sort(self):
        data = [
            [9, -1, 2],
            [8, 1, 3, 5, 2, 0, 10, 2, 5],
            [3, 2, 1],
            [4, 1, 5, 7, 2, 6, 1, 1, 6, 4, 10, 33, 5, 7, 23],
            [],
            [99, -4, 1, 2],
            [1, 2, 3, 4, 10, 6, 7, 8, 9, 10],
        ]

        for nums in data:
            sorted_nums = selection_sort(nums.copy())
            print(sorted_nums)

            nums.sort()
            self.lst_equal(sorted_nums, nums)

if __name__ == "__main__":
    print("selection sort")
    unittest.main()