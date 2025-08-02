from typing import List

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Merge nums2 into nums1 in-place. nums1 has length m+n,
        with its last n slots set to 0 and to be ignored.
        After merging, nums1[:m+n] is sorted.
        """
        # Pointers for nums1, nums2, and write position
        i = m - 1          # last valid element in nums1
        j = n - 1          # last element in nums2
        k = m + n - 1      # last position in nums1 buffer

        # While there are still elements in nums2 to merge
        while j >= 0:
            # If nums1 has elements left and its current element is bigger,
            # take that; otherwise take from nums2.
            if i >= 0 and nums1[i] > nums2[j]:
                nums1[k] = nums1[i]
                i -= 1
            else:
                nums1[k] = nums2[j]
                j -= 1
            k -= 1
        # No return needed — nums1 is modified in-place


if __name__ == "__main__":
    sol = Solution()
    tests = [
        # (nums1 initial, m, nums2, n, expected merged nums1[:m+n])
        ([1,2,3,0,0,0], 3, [2,5,6], 3, [1,2,2,3,5,6]),
        ([1],           1, [],        0, [1]),
        ([0],           0, [1],       1, [1]),
        ([2,0],         1, [1],       1, [1,2]),
        ([4,5,6,0,0,0], 3, [1,2,3],   3, [1,2,3,4,5,6]),
    ]

    for nums1, m, nums2, n, expected in tests:
        arr1 = nums1.copy()
        sol.merge(arr1, m, nums2, n)
        result = arr1[:m+n]
        status = "✅ PASS" if result == expected else f"❌ FAIL (got {result})"

        print(f"Input:    nums1={nums1}, m={m}, nums2={nums2}, n={n}")
        print(f"Expected: {expected}")
        print(f"Result:   {result}  {status}")
        print("-" * 60)
