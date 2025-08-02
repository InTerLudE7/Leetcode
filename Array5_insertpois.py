from typing import List

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        # Scan through the list: as soon as we find a number ≥ target, return its index
        for i, num in enumerate(nums):
            if num >= target:
                return i
        # If target is larger than all elements, it goes at the end
        return len(nums)

if __name__ == "__main__":
    sol = Solution()
    tests = [
        # (nums, target, expected_index)
        ([1, 3, 5, 6], 5, 2),
        ([1, 3, 5, 6], 2, 1),
        ([1, 3, 5, 6], 7, 4),
        ([1, 3, 5, 6], 0, 0),
        ([],           10, 0),  # empty array → insert at 0
    ]

    for nums, target, expected in tests:
        out = sol.searchInsert(nums.copy(), target)
        status = "✅ PASS" if out == expected else f"❌ FAIL (got {out})"
        print(f"Input:    nums = {nums}, target = {target}")
        print(f"Expected: {expected}")
        print(f"Output:   {out}  {status}")
        print("-" * 50)
