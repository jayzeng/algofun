import unittest

# counting sort
# typically used to sort a list of integers
# stable (preserving the original array order), non-comparative sort
# time: O(n+k) (n is the number of elements, k is the range of the elements)
# space: O(n+k)
# https://www.khanacademy.org/computing/computer-science/algorithms/counting-sort/a/counting-sort
# it is also possible to map strings to integers to perform counting sort
def counting_sort(arr):
    n = len(arr)
    if n <= 1:
        return arr

    # to account for negative numbers, we need to find the minimum and maximum
    # which will create the range of the output array (and potentially more elements than the input array)
    max_ele, min_ele = max(arr), min(arr)
    nums_range = max_ele - min_ele + 1

    buckets = [0] * nums_range
    output = [0] * n

    # store freqnu of each element in buckets
    for num in arr:
        buckets[num - min_ele] += 1

    # calculate the running-sum of the buckets (by using the left-most val)
    # e.g:
    # buckets:
    #          [1, 1, 1, 1, 0, 1]
    # becomes: [1, 2, 3, 4, 4, 5]
    for i in range(1, len(buckets)):
        buckets[i] += buckets[i - 1]

    # sort the elements in the buckets
    for num in arr:
        idx = buckets[num - min_ele] - 1
        output[idx] = num
        buckets[num - min_ele] -= 1

    return output

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

            sorted_nums = counting_sort(nums)
            print(sorted_nums)
            self.lst_equal(sorted_nums, expected_nums)

if __name__ == "__main__":
    print("counting sort")
    unittest.main()