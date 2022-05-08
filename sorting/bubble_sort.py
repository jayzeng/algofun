import unittest

# bubble sort
# one of the worst-performing sorting algorithms
# time: O(n^2)
# space: O(1)
def bubble_sort(nums):
    for _ in range(len(nums)):
        for j in range(len(nums) - 1):
            if nums[j] > nums[j + 1]:
                nums[j], nums[j + 1] = nums[j + 1], nums[j]
    
    return nums

# time: O(n^2)
# space: O(1)
def bubble_sort_optimized(nums):
    # when no swap is made, the list is sorted
    # introduce a counter to stop the loop if no swap is made
    # reduce from n to n - k 

    swapped = True
    num_iterations = 0

    while swapped:
        swapped = False
        for i in range(len(nums) - num_iterations - 1):
            if nums[i] > nums[i + 1]:
                nums[i], nums[i + 1] = nums[i + 1], nums[i]
                swapped = True
        # increment by 1 because it is guaranteed that at least element is swapped
        num_iterations += 1
    
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
            # [9, -1, 2],
            [8, 1, 3, 5, 2, 0, 10, 2, 5],
            [3, 2, 1],
            [4, 1, 5, 7, 2, 6, 1, 1, 6, 4, 10, 33, 5, 7, 23],
            [],
            [99, -4, 1, 2],
            [1, 2, 3, 4, 10, 6, 7, 8, 9, 10],
        ]

        for nums in data:
            expected_nums = nums.copy()
            expected_nums.sort()

            sorted_nums = bubble_sort(nums.copy())

            print(sorted_nums)
            self.lst_equal(sorted_nums, expected_nums)

            optimized_sorted_nums = bubble_sort_optimized(nums.copy())
            print(optimized_sorted_nums)
            self.lst_equal(optimized_sorted_nums, expected_nums)

if __name__ == "__main__":
    print("bubble sort")
    unittest.main()