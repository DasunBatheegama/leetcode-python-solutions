# First, we define what a "Tree Node" looks like
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        # Base case: if the node is empty, just return None
        if not root:
            return None
        
        # 1. Swap the left and right children
        root.left, root.right = root.right, root.left
        
        # 2. Recursively call this same function on the new left and right children
        self.invertTree(root.left)
        self.invertTree(root.right)
        
        # 3. Return the root of the now-inverted tree
        return root

# --- Driver Code ---
if __name__ == "__main__":
    sol = Solution()
    
    # Helper function to easily print a tree level by level
    def print_tree(root):
        if not root:
            return "[]"
        result, queue = [], [root]
        while queue:
            node = queue.pop(0)
            if node:
                result.append(node.val)
                queue.append(node.left)
                queue.append(node.right)
            else:
                result.append(None)
        # Clean up trailing None values for readability
        while result and result[-1] is None:
            result.pop()
        return str(result)

    # 1. Manually build a tree: 
    #      4
    #    /   \
    #   2     7
    #  / \   / \
    # 1   3 6   9
    root = TreeNode(4)
    root.left = TreeNode(2, TreeNode(1), TreeNode(3))
    root.right = TreeNode(7, TreeNode(6), TreeNode(9))
    
    print(f"Original Tree: {print_tree(root)}")
    
    # 2. Invert the tree
    inverted_root = sol.invertTree(root)
    
    # 3. Print the result
    # Expected: [4, 7, 2, 9, 6, 3, 1]
    print(f"Inverted Tree: {print_tree(inverted_root)}")