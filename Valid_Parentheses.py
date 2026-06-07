class Solution:
    def isValid(self, s: str) -> bool:
        # Our stack will keep track of opening brackets
        stack = []
        
        # A dictionary to map closing brackets to their required opening bracket
        bracket_map = {")": "(", "}": "{", "]": "["}
        
        for char in s:
            # If the character is a closing bracket
            if char in bracket_map:
                # Get the top element of the stack. If stack is empty, use a dummy value '#'
                top_element = stack.pop() if stack else '#'
                
                # If the popped bracket doesn't match the corresponding opening bracket
                if bracket_map[char] != top_element:
                    return False
            # Otherwise, it's an opening bracket, so we push it onto the stack
            else:
                stack.append(char)
                
        # If the stack is completely empty at the end, all brackets were matched!
        # `not stack` returns True if the list is empty, False otherwise.
        return not stack

# --- Driver Code ---
if __name__ == "__main__":
    sol = Solution()
    
    # Test cases
    test_1 = "()"        # Valid
    test_2 = "()[]{}"    # Valid
    test_3 = "(]"        # Invalid
    test_4 = "([)]"      # Invalid (Wrong order)
    test_5 = "{[]}"      # Valid (Nested correctly)
    
    print(f"Test 1 '{test_1}': {sol.isValid(test_1)}")
    print(f"Test 2 '{test_2}': {sol.isValid(test_2)}")
    print(f"Test 3 '{test_3}': {sol.isValid(test_3)}")
    print(f"Test 4 '{test_4}': {sol.isValid(test_4)}")
    print(f"Test 5 '{test_5}': {sol.isValid(test_5)}")