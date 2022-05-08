import unittest

# insertion sort
# efficient for small lists and mostly sorted lists
# in-place, stable sorting
# time: O(n^2)
# space: O(1)
def insertion_sort(arr):
    n = len(arr)
    if n <= 1:
        return arr

    for i in range(1, n):
        cur_val = arr[i]
        cur_pos = i

        while cur_pos > 0 and arr[cur_pos - 1] > cur_val:
            arr[cur_pos] = arr[cur_pos - 1]
            cur_pos = cur_pos - 1
        
        arr[cur_pos] = cur_val

    return arr

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
            expected_nums = nums.copy()
            expected_nums.sort()

            sorted_nums = insertion_sort(nums)
            print(sorted_nums)
            self.lst_equal(sorted_nums, expected_nums)

if __name__ == "__main__":
    print("insertion sort")
    unittest.main()