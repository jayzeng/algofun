import unittest

# merge sort
# time: O(nlog(n))
# https://www.khanacademy.org/computing/computer-science/algorithms/merge-sort/a/analysis-of-merge-sort
def mergesort(nums):
    # keep breaking the list into smaller lists
    # until the list is only one element
    if len(nums) <= 1:
        return nums

    mid = len(nums) // 2
    left = mergesort(nums[:mid])
    right = mergesort(nums[mid:])

    # merge the two lists
    return merge(left, right)

def merge(left, right):
    i, j = 0, 0
    output = []

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            output.append(left[i])
            i += 1
        else:
            output.append(right[j])
            j += 1

    # merge left over elements
    output.extend(left[i:])
    output.extend(right[j:])
    return output

class TestSort(unittest.TestCase):
    def test_sort(self):
        nums = [4, 1, 5, 7, 2, 6, 1, 1, 6, 4, 10, 33, 5, 7, 23]
        sorted_nums = mergesort(nums)
        # use tim sort to yield expected output
        nums.sort()
        self.assertEqual(sorted_nums, nums)

if __name__ == "__main__":
    print("merge sort")
    unittest.main()