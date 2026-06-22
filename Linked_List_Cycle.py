# Define the Node
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        # Start both pointers at the head of the list
        slow = head
        fast = head
        
        # Fast pointer moves 2 steps, so we must ensure fast and fast.next exist
        while fast and fast.next:
            slow = slow.next          # Move 1 step
            fast = fast.next.next     # Move 2 steps
            
            # If they meet, they are caught in a loop!
            if slow == fast:
                return True
                
        # If the fast pointer reaches the end of the list, there is no loop
        return False

# --- Driver Code ---
if __name__ == "__main__":
    sol = Solution()
    
    # --- Test Case 1: A list with a cycle ---
    # 3 -> 2 -> 0 -> -4
    #      ^          |
    #      |__________|
    node1 = ListNode(3)
    node2 = ListNode(2)
    node3 = ListNode(0)
    node4 = ListNode(-4)
    
    node1.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = node2 # This creates the cycle!
    
    print(f"Test Case 1 (Has Cycle): {sol.hasCycle(node1)}") # Expected: True
    
    # --- Test Case 2: A list without a cycle ---
    # 1 -> 2 -> None
    node_a = ListNode(1)
    node_b = ListNode(2)
    node_a.next = node_b
    
    print(f"Test Case 2 (No Cycle): {sol.hasCycle(node_a)}") # Expected: False