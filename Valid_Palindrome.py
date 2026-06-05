class Solution:
    def isPalindrome(self, s: str) -> bool:
        # Initialize two pointers: one at the start, one at the end
        left = 0
        right = len(s) - 1
        
        while left < right:
            # Move the left pointer forward if the current character is a space or symbol
            while left < right and not s[left].isalnum():
                left += 1
                
            # Move the right pointer backward if the current character is a space or symbol
            while left < right and not s[right].isalnum():
                right -= 1
                
            # Compare the two characters (converted to lowercase to ignore case differences)
            if s[left].lower() != s[right].lower():
                return False
            
            # If they match, move both pointers inward to check the next set of characters
            left += 1
            right -= 1
            
        return True

# --- Driver Code ---
if __name__ == "__main__":
    # 1. Create an instance of your Solution class
    sol = Solution()
    
    # 2. Define test cases
    test_1 = "A man, a plan, a canal: Panama"
    test_2 = "race a car"
    test_3 = " "
    
    # 3. Call your method and print the results
    result_1 = sol.isPalindrome(test_1)
    print(f"Test case 1: {result_1}")
    
    result_2 = sol.isPalindrome(test_2)
    print(f"Test case 2: {result_2}")
    
    result_3 = sol.isPalindrome(test_3)
    print(f"Test case 3: {result_3}")