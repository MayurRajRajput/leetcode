// Search a 2D Matrix
/*
You are given an m x n integer matrix matrix with the following two properties:

Each row is sorted in non-decreasing order.
The first integer of each row is greater than the last integer of the previous row.
Given an integer target, return true if target is in matrix or false otherwise.

You must write a solution in O(log(m * n)) time complexity.

*/
#include <iostream>
#include <vector>
using namespace std;

class Solution {
public:
    bool searchMatrix(vector<vector<int>>& matrix, int target) {
        int m = matrix.size(), n = matrix[0].size();
        int l = 0, r = m * n - 1;

        while (l <= r) {
            int mid = l + (r - l) / 2;
            int midVal = matrix[mid / n][mid % n];

            if (midVal == target) return true;
            else if (midVal < target) l = mid + 1;
            else r = mid - 1;
        }

        return false;
    }
};

int main() {
    Solution sol;

    vector<vector<int>> matrix = {
        {1, 3, 5, 7},
        {10, 11, 16, 20},
        {23, 30, 34, 60}
    };
    
    int target = 3;
    cout << "Is target " << target << " found? " 
         << (sol.searchMatrix(matrix, target) ? "true" : "false") << endl;

    target = 13;
    cout << "Is target " << target << " found? " 
         << (sol.searchMatrix(matrix, target) ? "true" : "false") << endl;

    return 0;
}

/*
Example 1:


Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3
Output: true
Example 2:


Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 13
Output: false
 
*/