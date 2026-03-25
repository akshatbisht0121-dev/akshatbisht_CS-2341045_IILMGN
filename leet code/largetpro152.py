#Input: nums = [2,3,-2,4]
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        max_prod = nums[0]
        min_prod = nums[0]
        result = nums[0]

        for i in range(1, len(nums)):
            if nums[i] < 0:
                max_prod, min_prod = min_prod, max_prod

            max_prod = max(nums[i], nums[i] * max_prod)
            min_prod = min(nums[i], nums[i] * min_prod)

            result = max(result, max_prod)

        return result
