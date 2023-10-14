from typing import List


def two_sum_hash(self, nums: List[int], target: int) -> List[int]:
    target_dict = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in target_dict:
            return [target_dict[complement], i]
        target_dict[num] = i
    return []


def two_sum_brute_force(self, nums: List[int], target: int) -> List[int]:
    for i in range(0,len(nums)):
        for j in range(i+1, len(nums)):
            if not j == len(nums):
                temp_sum = nums[i] + nums[j]
                if temp_sum == target:
                    return [i,j]