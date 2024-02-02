'''
DFS - Question can be like "FIND TOTAL NO OF PATHS"
Count the unique paths from the top to the left to the bottom right. 
A single path may only move along 0's and can't visit the same cell more than once.

Time complexity of this algorithm is O(4^(R.C)) or 0(4^(n.m))
From binary tree analysis, the time complexity is the no of branches raised to the power of heights.
  Branches: There is 4 ways to for each position. 
  Height: N rows and M columns, so, it's (n x m) or (r x c)
'''

grid = [[0,0,0,0],
        [1,1,0,0],
        [0,0,0,1],
        [0,1,0,0]]

def dfs(grid, r, c, visit):
    ROWS, COLS = len(grid), len(grid[0])
    if (min(r,c) < 0 or ROWS == r or COLS == c or
        (r,c) in visit or grid[r][c] == 1):
            return 0

    if ROWS-1 == r and COLS-1 == c:
        return 1

    visit.add((r,c))

    count = 0
    count += dfs(grid, r+1, c, visit)
    count += dfs(grid, r-1, c, visit)
    count += dfs(grid, r, c+1, visit)
    count += dfs(grid, r, c-1, visit)

    visit.remove((r,c))
    return count

print("Total paths:",dfs(grid, 0, 0, set()))

Find peak of an element
