import unittest

# heap sort
# time: O(nlog(n))
# space: O(1)
def max_heapify(lst, n, i):
    l = 2 * i + 1
    r = 2 * i + 2

    if l < n and lst[l] > lst[i]:
        largest = l
    else:
        largest = i

    if r < n and lst[r] > lst[largest]:
        largest = r

    if largest != i:
        lst[i], lst[largest] = lst[largest], lst[i]
        max_heapify(lst, n, largest)

def heapsort(nums):
    n = len(nums)

    for i in range(n, -1, -1):
        max_heapify(nums, n, i)

    for i in range(n - 1, 0, -1):
        nums[0], nums[i] = nums[i], nums[0]
        max_heapify(nums, i, 0)

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
            [4, 1, 5, 7, 2, 6, 1, 1, 6, 4, 10, 33, 5, 7, 23],
            [],
            [99, -4, 1, 2],
            [1, 2, 3, -3, 4, 10, 6, 7, 8, 9, 10],
        ]

        for nums in data:
            expected_nums = nums.copy()
            expected_nums.sort()

            sorted_nums = heapsort(nums)
            print(sorted_nums)
            self.lst_equal(sorted_nums, expected_nums)

if __name__ == "__main__":
    print("heap sort")
    unittest.main()