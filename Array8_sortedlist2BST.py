from typing import List, Optional
from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val: int=0, left: 'TreeNode'=None, right: 'TreeNode'=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        """
        Convert a sorted (ascending) array to a height-balanced BST.
        We pick the middle element as root, recursively build left/right.
        """
        def build(l: int, r: int) -> Optional[TreeNode]:
            if l > r:
                return None
            mid = (l + r) // 2
            node = TreeNode(nums[mid])
            node.left  = build(l, mid - 1)
            node.right = build(mid + 1, r)
            return node
        
        return build(0, len(nums) - 1)

# Helper: inorder traversal — should reproduce the original sorted array
def inorder(root: Optional[TreeNode]) -> List[int]:
    if not root:
        return []
    return inorder(root.left) + [root.val] + inorder(root.right)

# Helper: check if a tree is height-balanced (difference ≤ 1 at every node)
def check_balanced(root: Optional[TreeNode]) -> tuple[int, bool]:
    """
    Returns (height, is_balanced) for the subtree rooted at `root`.
    """
    if not root:
        return 0, True
    lh, lb = check_balanced(root.left)
    rh, rb = check_balanced(root.right)
    height = max(lh, rh) + 1
    return height, (lb and rb and abs(lh - rh) <= 1)

if __name__ == "__main__":
    tests = [
        # Each test is (input_sorted_array)
        [-10, -3, 0, 5, 9],
        [],
        [1],
        [1, 2, 3],
        [1, 2],
    ]

    for nums in tests:
        root = Solution().sortedArrayToBST(nums)
        # Validate by inorder and balanced property
        out_inorder = inorder(root)
        _, is_bal = check_balanced(root)
        passed = (out_inorder == nums) and is_bal

        status = "✅ PASS" if passed else "❌ FAIL"
        print(f"Input:  {nums}")
        print(f"In-order traversal: {out_inorder}")
        print(f"Height-balanced:    {is_bal}")
        print(f"Result:  {status}")
        print("-" * 60)
