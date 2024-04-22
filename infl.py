from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_dict={}
        for idx, num in enumerate(nums):
            complement = target - num
            if complement in num_dict:
                return [num_dict[complement], idx]
            num_dict[num] = idx
        return []

sol = Solution()

# Приклади
nums1 = [2, 7, 11, 15]
target1 = 9
print(sol.twoSum(nums1, target1))  # Виведе: [0, 1]

nums2 = [3, 2, 4]
target2 = 6
print(sol.twoSum(nums2, target2))  # Виведе: [1, 2]

nums3 = [3, 3]
target3 = 6
print(sol.twoSum(nums3, target3))  # Виведе: [0, 1]
