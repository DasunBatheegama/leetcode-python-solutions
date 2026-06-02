class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        # Start by assuming the lowest price is the first day's price
        min_price = prices[0]
        max_profit = 0
        
        for price in prices:
            # If we find a lower price, update our min_price
            if price < min_price:
                min_price = price
            # Otherwise, check if selling at the current price gives us a better profit
            elif price - min_price > max_profit:
                max_profit = price - min_price
                
        return max_profit

# --- Driver Code ---
if __name__ == "__main__":
    # 1. Create an instance of your Solution class
    sol = Solution()
    
    # 2. Define test cases
    test_prices_1 = [7, 1, 5, 3, 6, 4]
    test_prices_2 = [7, 6, 4, 3, 1]
    
    # 3. Call your method and print the results
    result_1 = sol.maxProfit(test_prices_1)
    print(f"Profit for test case 1: {result_1}")
    
    result_2 = sol.maxProfit(test_prices_2)
    print(f"Profit for test case 2: {result_2}")