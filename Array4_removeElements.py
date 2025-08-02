from typing import List

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        # i is the position to write the next non-val element
        i = 0
        # j scans through the entire array
        for j in range(len(nums)):
            # whenever nums[j] != val, we copy it forward
            if nums[j] != val:
                nums[i] = nums[j]
                i += 1
        # i is now the count of elements ≠ val
        return i

if __name__ == "__main__":
    sol = Solution()
    tests = [
        # (input array, value to remove, expected remaining elements)
        ([3,2,2,3],         3, [2,2]),
        ([0,1,2,2,3,0,4,2], 2, [0,1,3,0,4]),
        ([],                1, []),         # empty array
        ([1,1,1,1],         1, []),         # all elements removed
        ([4,5,6,7],         8, [4,5,6,7]),  # nothing to remove
    ]

    for nums, val, expected in tests:
        arr = nums.copy()
        k = sol.removeElement(arr, val)
        result = arr[:k]
        status = "✅ PASS" if (k == len(expected) and result == expected) \
                 else f"❌ FAIL (got k={k}, arr[:k]={result})"
        # build the "don't care" tail as underscores for display
        tail = ["_"] * (len(nums) - k)

        print(f"Input: nums = {nums}, val = {val}")
        print(f"Expected: k = {len(expected)}, nums = {expected + ['_']*(len(nums)-len(expected))}")
        print(f"Output:   k = {k}, nums = {result + tail}  {status}")
        print("-" * 60)
