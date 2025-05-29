// Matrix Cells in Distance Order
/*
You are given four integers row, cols, rCenter, and cCenter. There is a rows x cols matrix and you are on the cell with the coordinates (rCenter, cCenter).

Return the coordinates of all cells in the matrix, sorted by their distance from (rCenter, cCenter) from the smallest distance to the largest distance. You may return the answer in any order that satisfies this condition.

The distance between two cells (r1, c1) and (r2, c2) is |r1 - r2| + |c1 - c2|.
*/
#include <iostream>
#include <vector>
#include <algorithm>
#include <cmath>

using namespace std;

class Solution {
public:
    vector<vector<int>> allCellsDistOrder(int rows, int cols, int rCenter, int cCenter) {
        vector<vector<int>> ans;
        vector<pair<int, pair<int, int>>> v;

        for (int i = 0; i < rows; ++i) {
            for (int j = 0; j < cols; ++j) {
                int distance = abs(i - rCenter) + abs(j - cCenter);
                v.push_back({distance, {i, j}});
            }
        }

        sort(v.begin(), v.end());

        for (auto& item : v) {
            ans.push_back({item.second.first, item.second.second});
        }

        return ans;
    }
};

// Helper function to print the result
void printMatrix(const vector<vector<int>>& matrix) {
    for (const auto& row : matrix) {
        cout << "[" << row[0] << "," << row[1] << "] ";
    }
    cout << endl;
}

int main() {
    Solution sol;

    vector<vector<int>> result;

    // Example 1
    result = sol.allCellsDistOrder(1, 2, 0, 0);
    cout << "Example 1 Output: ";
    printMatrix(result);

    // Example 2
    result = sol.allCellsDistOrder(2, 2, 0, 1);
    cout << "Example 2 Output: ";
    printMatrix(result);

    // Example 3
    result = sol.allCellsDistOrder(2, 3, 1, 2);
    cout << "Example 3 Output: ";
    printMatrix(result);

    return 0;
}

/*
Example 1:

Input: rows = 1, cols = 2, rCenter = 0, cCenter = 0
Output: [[0,0],[0,1]]
Explanation: The distances from (0, 0) to other cells are: [0,1]
Example 2:

Input: rows = 2, cols = 2, rCenter = 0, cCenter = 1
Output: [[0,1],[0,0],[1,1],[1,0]]
Explanation: The distances from (0, 1) to other cells are: [0,1,1,2]
The answer [[0,1],[1,1],[0,0],[1,0]] would also be accepted as correct.
Example 3:

Input: rows = 2, cols = 3, rCenter = 1, cCenter = 2
Output: [[1,2],[0,2],[1,1],[0,1],[1,0],[0,0]]
Explanation: The distances from (1, 2) to other cells are: [0,1,1,2,2,3]
There are other answers that would also be accepted as correct, such as [[1,2],[1,1],[0,2],[1,0],[0,1],[0,0]].
 
*/