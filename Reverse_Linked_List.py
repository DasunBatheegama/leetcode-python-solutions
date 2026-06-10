# First, we define what a "Node" looks like
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        prev = None
        curr = head
        
        while curr:
            # 1. Save the next node so we don't lose the rest of the list
            next_temp = curr.next
            
            # 2. Reverse the pointer of the current node to point backward
            curr.next = prev
            
            # 3. Move the 'prev' and 'curr' pointers one step forward for the next loop
            prev = curr
            curr = next_temp
            
        # At the end, 'curr' is None, and 'prev' is the new head of the reversed list
        return prev

# --- Driver Code ---
if __name__ == "__main__":
    sol = Solution()
    
    # Helper function to easily create a linked list from a Python list
    def create_linked_list(arr):
        if not arr: return None
        head = ListNode(arr[0])
        current = head
        for val in arr[1:]:
            current.next = ListNode(val)
            current = current.next
        return head

    # Helper function to print a linked list so we can see the results
    def print_linked_list(head):
        values = []
        current = head
        while current:
            values.append(str(current.val))
            current = current.next
        values.append("None")
        print(" -> ".join(values))

    # Test case 1
    original_list = create_linked_list([1, 2, 3, 4, 5])
    print("Original List: ")
    print_linked_list(original_list)
    
    reversed_list = sol.reverseList(original_list)
    print("Reversed List: ")
    print_linked_list(reversed_list)