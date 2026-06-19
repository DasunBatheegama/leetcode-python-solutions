# Define the Tree Node
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        # Base Case 1: Both are empty (we reached the bottom safely)
        if not p and not q:
            return True
            
        # Base Case 2: One is empty but the other is not (structural mismatch)
        if not p or not q:
            return False
            
        # Base Case 3: Both have values, but the values are different
        if p.val != q.val:
            return False
            
        # If we made it here, the current nodes match!
        # Now, recursively check if the left sides match AND the right sides match.
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)

# --- Driver Code ---
if __name__ == "__main__":
    sol = Solution()
    
    # Test Case 1: Identical Trees
    # Tree P:     1         Tree Q:     1
    #            / \                   / \
    #           2   3                 2   3
    p1 = TreeNode(1, TreeNode(2), TreeNode(3))
    q1 = TreeNode(1, TreeNode(2), TreeNode(3))
    
    # Test Case 2: Structurally Different
    # Tree P:     1         Tree Q:     1
    #            /                       \
    #           2                         2
    p2 = TreeNode(1, TreeNode(2), None)
    q2 = TreeNode(1, None, TreeNode(2))
    
    # Test Case 3: Same Structure, Different Values
    # Tree P:     1         Tree Q:     1
    #            / \                   / \
    #           2   1                 1   2
    p3 = TreeNode(1, TreeNode(2), TreeNode(1))
    q3 = TreeNode(1, TreeNode(1), TreeNode(2))
    
    print(f"Test Case 1 (Identical): {sol.isSameTree(p1, q1)}")
    print(f"Test Case 2 (Different Structure): {sol.isSameTree(p2, q2)}")
    print(f"Test Case 3 (Different Values): {sol.isSameTree(p3, q3)}")