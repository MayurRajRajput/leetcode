// Unique Paths II
/*
You are given an m x n integer array grid. There is a robot initially located at the top-left corner (i.e., grid[0][0]). The robot tries to move to the bottom-right corner (i.e., grid[m - 1][n - 1]). The robot can only move either down or right at any point in time.

An obstacle and space are marked as 1 or 0 respectively in grid. A path that the robot takes cannot include any square that is an obstacle.

Return the number of possible unique paths that the robot can take to reach the bottom-right corner.

The testcases are generated so that the answer will be less than or equal to 2 * 109.
*/
#include <iostream>
#include <vector>
using namespace std;

class Solution {
public:
    int uniquePathsWithObstacles(vector<vector<int>>& obstacleGrid) {
        if (obstacleGrid.empty() || obstacleGrid[0][0] == 1) {
            return 0;
        }

        int rows = obstacleGrid.size();
        int cols = obstacleGrid[0].size();
        vector<int> dp(cols, 0);
        dp[0] = 1;

        for (int r = 0; r < rows; r++) {
            for (int c = 0; c < cols; c++) {
                if (obstacleGrid[r][c] == 1) {
                    dp[c] = 0;
                } else if (c > 0) {
                    dp[c] += dp[c - 1];
                }
            }
        }

        return dp[cols - 1];
    }
};

int main() {
    Solution sol;

    // Example 1
    vector<vector<int>> grid1 = {{0,0,0}, {0,1,0}, {0,0,0}};
    cout << "Unique Paths (Example 1): " << sol.uniquePathsWithObstacles(grid1) << endl; // Output: 2

    // Example 2
    vector<vector<int>> grid2 = {{0,1}, {0,0}};
    cout << "Unique Paths (Example 2): " << sol.uniquePathsWithObstacles(grid2) << endl; // Output: 1

    return 0;
}

/*
Example 1:


Input: obstacleGrid = [[0,0,0],[0,1,0],[0,0,0]]
Output: 2
Explanation: There is one obstacle in the middle of the 3x3 grid above.
There are two ways to reach the bottom-right corner:
1. Right -> Right -> Down -> Down
2. Down -> Down -> Right -> Right
Example 2:


Input: obstacleGrid = [[0,1],[0,0]]
Output: 1
 
*/