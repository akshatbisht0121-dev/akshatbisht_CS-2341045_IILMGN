from typing import List

"""class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        answer = [1] * n

        # Step 1: Prefix products
        prefix = 1
        for i in range(n):
            answer[i] = prefix
            prefix *= nums[i]

        # Step 2: Suffix products
        suffix = 1
        for i in range(n - 1, -1, -1):
            answer[i] *= suffix
            suffix *= nums[i]

        return answer"""
def prefix_array(arr):
    n = len(arr)
    prefix = [0] * n
    prefix[0] = arr[0]

    for i in range(1, n):
        prefix[i] = prefix[i - 1] + arr[i]

    return prefix


def suffix_array(arr):
    n = len(arr)
    suffix = [0] * n
    suffix[n - 1] = arr[n - 1]

    for i in range(n - 2, -1, -1):
        suffix[i] = suffix[i + 1] + arr[i]

    return suffix



arr = [2, 4, 6, 8]

print("Original Array:", arr)
print("Prefix Array:", prefix_array(arr))
print("Suffix Array:", suffix_array(arr))

