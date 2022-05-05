import random

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
    
    # left over
    output.extend(left[i:])
    output.extend(right[j:])
    return output

def main():
    # build up random, unsorted list
    nums = [random.randint(1, 1000000) for _ in range(1000)]
    print(f'before: {nums}')
    sorted_nums = mergesort(nums)
    print(f'after: {sorted_nums}')

if __name__ == "__main__":
    main()