from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int: 
        nums[:] = list(dict.fromkeys(nums))
        return len(nums) 
        # # If the list is empty, return 0
        # if not nums:
        #     return 0
        # # i = index of last unique element
        # i = 0
        # # j scans through the array
        # for j in range(1, len(nums)):
        #     if nums[j] != nums[i]:
        #         i += 1
        #         nums[i] = nums[j]
        # # number of uniques = i+1
        # return i + 1

if __name__ == "__main__":
    sol = Solution()
    tests = [
        [1,1,2],
        [0,0,1,1,1,2,2,3,3,4],
        [],
        [1,2,3],
        [1,1,1,1],
    ]

    for nums in tests:
        orig = nums.copy()
        k = sol.removeDuplicates(orig)
        # build the “don’t care” tail as underscores
        tail = ["_"] * (len(nums) - k)
        # print in LeetCode Example format
        print(f"Input: nums = {nums}")
        print(f"Output: {k}, nums = {orig[:k] + tail}")
        print("-" * 50)
