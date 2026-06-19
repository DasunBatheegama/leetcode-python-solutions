# Define the Tree Node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        current = root
        
        while current:
            # If both p and q are greater than parent, go right
            if p.val > current.val and q.val > current.val:
                current = current.right
            
            # If both p and q are lesser than parent, go left
            elif p.val < current.val and q.val < current.val:
                current = current.left
                
            # We found the split point (or one of the nodes is the current node)
            else:
                return current

# --- Driver Code ---
if __name__ == "__main__":
    sol = Solution()
    
    # Let's build a Binary Search Tree:
    #             6
    #           /   \
    #          2     8
    #         / \   / \
    #        0   4 7   9
    #           / \
    #          3   5
    
    root = TreeNode(6)
    root.left = TreeNode(2)
    root.right = TreeNode(8)
    root.left.left = TreeNode(0)
    root.left.right = TreeNode(4)
    root.right.left = TreeNode(7)
    root.right.right = TreeNode(9)
    root.left.right.left = TreeNode(3)
    root.left.right.right = TreeNode(5)
    
    # Test Case 1: LCA of 2 and 8
    p1, q1 = root.left, root.right
    lca1 = sol.lowestCommonAncestor(root, p1, q1)
    print(f"LCA of {p1.val} and {q1.val} is: {lca1.val}") # Expected: 6
    
    # Test Case 2: LCA of 2 and 4
    p2, q2 = root.left, root.left.right
    lca2 = sol.lowestCommonAncestor(root, p2, q2)
    print(f"LCA of {p2.val} and {q2.val} is: {lca2.val}") # Expected: 2 (A node can be its own ancestor)