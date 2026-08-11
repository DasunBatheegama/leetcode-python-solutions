class Solution:
    def climbStairs(self, n: int) -> int:
        # Base cases: If there are 1 or 2 steps, the answer is just n.
        if n <= 2:
            return n
            
        # We only need to remember the results of the two previous steps
        # one_step_before represents (n-1)
        # two_steps_before represents (n-2)
        two_steps_before = 1
        one_step_before = 2
        
        # Start calculating from step 3 up to n
        for i in range(3, n + 1):
            # The current step is the sum of the two previous steps
            current = one_step_before + two_steps_before
            
            # Shift our variables forward for the next loop iteration
            two_steps_before = one_step_before
            one_step_before = current
            
        return one_step_before

# --- Driver Code ---
if __name__ == "__main__":
    sol = Solution()
    
    # Test cases
    test_1 = 2
    test_2 = 3
    test_3 = 5
    test_4 = 10
    
    print(f"Ways to climb {test_1} steps: {sol.climbStairs(test_1)}") # Expected: 2
    print(f"Ways to climb {test_2} steps: {sol.climbStairs(test_2)}") # Expected: 3
    print(f"Ways to climb {test_3} steps: {sol.climbStairs(test_3)}") # Expected: 8
    print(f"Ways to climb {test_4} steps: {sol.climbStairs(test_4)}") # Expected: 89