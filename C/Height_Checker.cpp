// Height Checker
/*
A school is trying to take an annual photo of all the students. The students are asked to stand in a single file line in non-decreasing order by height. Let this ordering be represented by the integer array expected where expected[i] is the expected height of the ith student in line.

You are given an integer array heights representing the current order that the students are standing in. Each heights[i] is the height of the ith student in line (0-indexed).

Return the number of indices where heights[i] != expected[i].
*/
#include <iostream>
#include <vector>
using namespace std;

class Solution {
public:
    int heightChecker(vector<int>& heights) {
        int count[101] = {0};
        int n = heights.size();
        for (int i = 0; i < n; ++i) ++count[heights[i]];
        int res = 0, idx = 0;
        for (int h = 1; h <= 100; ++h) {
            while (count[h]-- > 0) {
                if (heights[idx++] != h) ++res;
            }
        }
        return res;
    }
};

int main() {
    Solution sol;

    vector<int> heights1 = {1, 1, 4, 2, 1, 3};
    cout << "Output for heights1: " << sol.heightChecker(heights1) << endl; // Output: 3

    vector<int> heights2 = {5, 1, 2, 3, 4};
    cout << "Output for heights2: " << sol.heightChecker(heights2) << endl; // Output: 5

    vector<int> heights3 = {1, 2, 3, 4, 5};
    cout << "Output for heights3: " << sol.heightChecker(heights3) << endl; // Output: 0

    return 0;
}

/*
Example 1:

Input: heights = [1,1,4,2,1,3]
Output: 3
Explanation: 
heights:  [1,1,4,2,1,3]
expected: [1,1,1,2,3,4]
Indices 2, 4, and 5 do not match.
Example 2:

Input: heights = [5,1,2,3,4]
Output: 5
Explanation:
heights:  [5,1,2,3,4]
expected: [1,2,3,4,5]
All indices do not match.
Example 3:

Input: heights = [1,2,3,4,5]
Output: 0
Explanation:
heights:  [1,2,3,4,5]
expected: [1,2,3,4,5]
All indices match.
 
*/