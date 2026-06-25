class Solution:
    def numIslands(self, grid: list[list[str]]) -> int:
        if not grid:
            return 0
            
        rows = len(grid)
        cols = len(grid[0])
        island_count = 0
        
        # A helper function to explore and "sink" connected land
        def dfs(r, c):
            # Base cases: if we go out of bounds, or hit water, stop!
            if r < 0 or c < 0 or r >= rows or c >= cols or grid[r][c] == '0':
                return
            
            # "Sink" the current land by turning it into water
            grid[r][c] = '0'
            
            # Recursively explore all 4 directions (up, down, left, right)
            dfs(r - 1, c) # Up
            dfs(r + 1, c) # Down
            dfs(r, c - 1) # Left
            dfs(r, c + 1) # Right

        # Iterate through every cell in the grid
        for r in range(rows):
            for c in range(cols):
                # When we find unvisited land, it's a new island!
                if grid[r][c] == '1':
                    island_count += 1
                    # Trigger DFS to sink the entire connected island
                    dfs(r, c)
                    
        return island_count

# --- Driver Code ---
if __name__ == "__main__":
    sol = Solution()
    
    # Test Case 1
    # 1 1 0 0 0
    # 1 1 0 0 0
    # 0 0 1 0 0
    # 0 0 0 1 1
    grid_1 = [
      ["1","1","0","0","0"],
      ["1","1","0","0","0"],
      ["0","0","1","0","0"],
      ["0","0","0","1","1"]
    ]
    
    print(f"Number of islands in grid 1: {sol.numIslands(grid_1)}") # Expected: 3