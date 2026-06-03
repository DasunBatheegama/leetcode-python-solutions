class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        # Create an empty set to store numbers we have seen
        seen = set()
        
        for num in nums:
            # If the number is already in the set, we found a duplicate!
            if num in seen:
                return True
            
            # Otherwise, add it to the set and keep checking
            seen.add(num)
            
        # If we finish the loop without finding duplicates, return False
        return False

# --- Driver Code ---
if __name__ == "__main__":
    # 1. Create an instance of your Solution class
    sol = Solution()
    
    # 2. Define test cases
    test_nums_1 = [1, 2, 3, 1]
    test_nums_2 = [1, 2, 3, 4]
    test_nums_3 = [1, 1, 1, 3, 3, 4, 3, 2, 4, 2]
    
    # 3. Call your method and print the results
    result_1 = sol.containsDuplicate(test_nums_1)
    print(f"Test case 1 {test_nums_1}: {result_1}")
    
    result_2 = sol.containsDuplicate(test_nums_2)
    print(f"Test case 2 {test_nums_2}: {result_2}")
    
    result_3 = sol.containsDuplicate(test_nums_3)
    print(f"Test case 3 {test_nums_3}: {result_3}")