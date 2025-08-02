from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numsList = {}
        for i,n in enumerate(nums):
            diff = target-n
            if diff in numsList:
                return [numsList[diff], i]
            else:
                numsList[n] = i

if __name__ == "__main__":
    sol = Solution()

    tests = [
        # (输入 nums, target, 期望输出)
        ([2,7,11,15], 9, [0,1]),
        ([3,2,4],    6, [1,2]),
        ([3,3],      6, [0,1]),
    ]

    for i, (nums, tgt, expect) in enumerate(tests, 1):
        out = sol.twoSum(nums, tgt)
        ok = "✅" if out == expect else f"❌  expected {expect}"
        print(f"Case {i}: nums={nums}, target={tgt} → out={out} {ok}")