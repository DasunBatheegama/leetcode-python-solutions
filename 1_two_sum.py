"""
1. Two Sum

Given an array of integers `nums` and an integer `target`, return indices of the two numbers such that they add up to `target`.
You may assume that each input would have exactly one solution, and you may not use the same element twice.
You can return the answer in any order.

Example 1:
Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

Example 2:
Input: nums = [3,2,4], target = 6
Output: [1,2]

Example 3:
Input: nums = [3,3], target = 6
Output: [0,1]
"""
from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for i, num in enumerate(nums):
            comp = target - num
            if comp in seen:
                return [seen[comp], i]
            seen[num] = i
        raise ValueError("No two sum solution")

# Optional: You can add tests down here to check your work
if __name__ == "__main__":
    solution = Solution()
    print("Test 1:", solution.twoSum([2, 7, 11, 15], 9) == [0, 1])
    print("Test 2:", solution.twoSum([3, 2, 4], 6) == [1, 2])
    print("Test 3:", solution.twoSum([3, 3], 6) == [0, 1])
