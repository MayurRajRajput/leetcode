// Minimum Path Sum
/*
Given a m x n grid filled with non-negative numbers, find a path from top left to bottom right, which minimizes the sum of all numbers along its path.

Note: You can only move either down or right at any point in time.
*/
#include <iostream>
#include <vector>
#include <climits>
using namespace std;
class Solution {
public:

int solve(int m,int n,vector<vector<int>>& grid) {    
   for(int i=0;i<=m;i++){
    for(int j=0;j<=n;j++){
        if(i==0 && j==0) continue;
            int left = (j > 0) ? grid[i][j - 1] : INT_MAX;
            int up   = (i > 0) ? grid[i - 1][j] : INT_MAX;
     grid[i][j] += min(left,up);
    }
   }
   return grid[m][n];
}
    int minPathSum(vector<vector<int>>& grid) {
        int m = grid.size();
        int n = grid[0].size();
        int ans = solve(m-1,n-1,grid);
        return ans;
    }
};
int main() {
    Solution sol;

    vector<vector<int>> grid1 = {{1,3,1},{1,5,1},{4,2,1}};
    cout << "Minimum Path Sum (Example 1): " << sol.minPathSum(grid1) << endl; // Output: 7

    vector<vector<int>> grid2 = {{1,2,3},{4,5,6}};
    cout << "Minimum Path Sum (Example 2): " << sol.minPathSum(grid2) << endl; // Output: 12

    return 0;
}

/*
Example 1:


Input: grid = [[1,3,1],[1,5,1],[4,2,1]]
Output: 7
Explanation: Because the path 1 → 3 → 1 → 1 → 1 minimizes the sum.
Example 2:

Input: grid = [[1,2,3],[4,5,6]]
Output: 12
 
*/