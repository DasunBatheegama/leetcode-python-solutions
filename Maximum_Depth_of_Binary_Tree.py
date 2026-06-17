# Define the Tree Node
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        # Base case: if the tree is empty, the depth is 0
        if not root:
            return 0
        
        # 1. Ask the left child for its maximum depth
        left_depth = self.maxDepth(root.left)
        
        # 2. Ask the right child for its maximum depth
        right_depth = self.maxDepth(root.right)
        
        # 3. The depth of the current node is 1 + whichever child is deeper
        return 1 + max(left_depth, right_depth)

# --- Driver Code ---
if __name__ == "__main__":
    sol = Solution()
    
    # Let's build the example tree from LeetCode:
    #      3
    #    /   \
    #   9    20
    #       /  \
    #      15   7
    
    root = TreeNode(3)
    root.left = TreeNode(9)
    root.right = TreeNode(20, TreeNode(15), TreeNode(7))
    
    # Calculate the depth
    depth = sol.maxDepth(root)
    
    # Expected output: 3 (The path 3 -> 20 -> 15 or 3 -> 20 -> 7)
    print(f"The maximum depth of the tree is: {depth}")