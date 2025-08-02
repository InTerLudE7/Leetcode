from typing import List

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        # Add one to the last digit
        digits[-1] += 1
        # Propagate carry from rightmost toward the front
        for i in range(len(digits) - 1, -1, -1):
            if digits[i] == 10:
                # Set current to 0 and carry over
                digits[i] = 0
                if i == 0:
                    # At most significant digit: insert the carry at front
                    digits.insert(0, 1)
                else:
                    # Otherwise, add carry to the next more significant digit
                    digits[i - 1] += 1
            else:
                # No further carry, we can stop early
                break
        return digits


if __name__ == "__main__":
    sol = Solution()
    tests = [
        ([1,2,3],   [1,2,4]),
        ([4,3,2,1], [4,3,2,2]),
        ([9],       [1,0]),
        ([9,9],     [1,0,0]),
        ([1,9,9],   [2,0,0]),
    ]

    for digits, expected in tests:
        arr = digits.copy()
        out = sol.plusOne(arr)
        status = "✅ PASS" if out == expected else f"❌ FAIL (got {out})"
        print(f"Input:    {digits}")
        print(f"Expected: {expected}")
        print(f"Output:   {out}  {status}")
        print("-" * 40)
