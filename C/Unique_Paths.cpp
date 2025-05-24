// Unique Paths
/*
There is a robot on an m x n grid. The robot is initially located at the top-left corner (i.e., grid[0][0]). The robot tries to move to the bottom-right corner (i.e., grid[m - 1][n - 1]). The robot can only move either down or right at any point in time.

Given the two integers m and n, return the number of possible unique paths that the robot can take to reach the bottom-right corner.

The test cases are generated so that the answer will be less than or equal to 2 * 109.

*/
#include <iostream>
#include <vector>
using namespace std;

class Solution {
public:
    int uniquePaths(int m, int n) {
        vector<int> aboveRow(n, 1);
        for (int row = 1; row < m; row++) {
            vector<int> currentRow(n, 1);
            for (int col = 1; col < n; col++) {
                currentRow[col] = currentRow[col - 1] + aboveRow[col];
            }
            aboveRow = currentRow;
        }
        return aboveRow[n - 1];        
    }
};

int main() {
    Solution sol;

    // Test Case 1
    int m1 = 3, n1 = 7;
    cout << "Unique Paths for (3, 7): " << sol.uniquePaths(m1, n1) << endl; // Output: 28

    // Test Case 2
    int m2 = 3, n2 = 2;
    cout << "Unique Paths for (3, 2): " << sol.uniquePaths(m2, n2) << endl; // Output: 3

    return 0;
}


/*
Example 1:


Input: m = 3, n = 7
Output: 28
Example 2:

Input: m = 3, n = 2
Output: 3
Explanation: From the top-left corner, there are a total of 3 ways to reach the bottom-right corner:
1. Right -> Down -> Down
2. Down -> Down -> Right
3. Down -> Right -> Down
 
*/