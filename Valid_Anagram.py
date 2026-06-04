class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # If the strings are different lengths, they cannot be anagrams
        if len(s) != len(t):
            return False
            
        # Create a dictionary to count letter frequencies
        letter_counts = {}
        
        # Count the letters in string 's'
        for letter in s:
            if letter in letter_counts:
                letter_counts[letter] += 1
            else:
                letter_counts[letter] = 1
                
        # Subtract the counts using string 't'
        for letter in t:
            if letter in letter_counts:
                letter_counts[letter] -= 1
            else:
                # If we see a letter in 't' that wasn't in 's', it's not an anagram
                return False
                
        # If any count is not exactly 0, they are not anagrams
        for count in letter_counts.values():
            if count != 0:
                return False
                
        return True

# --- Driver Code ---
if __name__ == "__main__":
    # 1. Create an instance of your Solution class
    sol = Solution()
    
    # 2. Define test cases
    s1, t1 = "anagram", "nagaram"
    s2, t2 = "rat", "car"
    s3, t3 = "listen", "silent"
    
    # 3. Call your method and print the results
    result_1 = sol.isAnagram(s1, t1)
    print(f"Test case 1 ('{s1}', '{t1}'): {result_1}")
    
    result_2 = sol.isAnagram(s2, t2)
    print(f"Test case 2 ('{s2}', '{t2}'): {result_2}")
    
    result_3 = sol.isAnagram(s3, t3)
    print(f"Test case 3 ('{s3}', '{t3}'): {result_3}")