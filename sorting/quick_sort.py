import unittest

# quick sort
# time: avg(o(nlog(n)), worst(o(n^2))
# https://www.khanacademy.org/computing/computer-science/algorithms/quick-sort/a/quick-sort
def quicksort(nums, start, end):
    # partition the list by choosing a pivot
    # different strategies can be used
    # - first element
    # - last element
    # - random element 
    # - medium element
    # recursively sort the left and right subarrays
    # return quicksort(nums)
    if start < end:
        partition_idx = partition(nums, start, end)
        quicksort(nums, start, partition_idx - 1)
        quicksort(nums, partition_idx + 1, end)
    
    return nums

def partition(nums, l, r):
    pivot_idx = l
    pivot = nums[pivot_idx]

    while l < r:
        while l < len(nums) and nums[l] <= pivot:
            l += 1

        while nums[r] > pivot:
            r -= 1

        if l < r:
            swap(nums, l, r)

    swap(nums, pivot_idx, r)
    return r

def swap(nums, i, j):
    nums[i], nums[j] = nums[j], nums[i]

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
            [4, 1, 5, 7, 2, 6, 1, 1, 6, 4, 10, 33, 5, 7, 23],
            [],
            [99, -4, 1, 2],
            [1, 2, 3, -3, 4, 10, 6, 7, 8, 9, 10],
        ]

        for nums in data:
            expected_nums = nums.copy()
            expected_nums.sort()

            sorted_nums = quicksort(nums, 0, len(nums) - 1)
            print(sorted_nums)
            self.lst_equal(sorted_nums, expected_nums)

if __name__ == "__main__":
    print("quick sort")
    unittest.main()