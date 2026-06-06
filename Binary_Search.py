class Solution:
    def search(self, nums: list[int], target: int) -> int:
        left = 0
        right = len(nums) - 1
        
        while left <= right:
            # Find the middle index
            # (In Python, // does integer division so we don't get decimals)
            mid = (left + right) // 2
            
            # Did we find it?
            if nums[mid] == target:
                return mid
            
            # If the middle number is too small, the target must be to the right
            elif nums[mid] < target:
                left = mid + 1
                
            # If the middle number is too big, the target must be to the left
            else:
                right = mid - 1
                
        # If the loop finishes and we haven't returned, it's not in the array
        return -1

# --- Driver Code ---
if __name__ == "__main__":
    sol = Solution()
    
    # Test cases
    nums_1 = [-1, 0, 3, 5, 9, 12]
    target_1 = 9
    
    nums_2 = [-1, 0, 3, 5, 9, 12]
    target_2 = 2
    
    result_1 = sol.search(nums_1, target_1)
    print(f"Index of target {target_1}: {result_1}")
    
    result_2 = sol.search(nums_2, target_2)
    print(f"Index of target {target_2}: {result_2}")