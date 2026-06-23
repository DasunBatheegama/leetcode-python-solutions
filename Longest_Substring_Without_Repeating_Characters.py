class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # A set to keep track of characters in our current window
        char_set = set()
        left = 0
        max_length = 0
        
        # 'right' is our expanding pointer moving through the string
        for right in range(len(s)):
            
            # If we find a duplicate, shrink the window from the left 
            # until the duplicate is completely removed from our set
            while s[right] in char_set:
                char_set.remove(s[left])
                left += 1
                
            # Add the new character to our window's set
            char_set.add(s[right])
            
            # Check if this new valid window is the longest one we've seen
            # The current window size is (right - left + 1)
            if (right - left + 1) > max_length:
                max_length = right - left + 1
                
        return max_length

# --- Driver Code ---
if __name__ == "__main__":
    sol = Solution()
    
    # Test cases
    test_1 = "abcabcbb" # Expected: 3 ("abc")
    test_2 = "bbbbb"    # Expected: 1 ("b")
    test_3 = "pwwkew"   # Expected: 3 ("wke")
    
    print(f"Test Case 1 '{test_1}': {sol.lengthOfLongestSubstring(test_1)}")
    print(f"Test Case 2 '{test_2}': {sol.lengthOfLongestSubstring(test_2)}")
    print(f"Test Case 3 '{test_3}': {sol.lengthOfLongestSubstring(test_3)}")