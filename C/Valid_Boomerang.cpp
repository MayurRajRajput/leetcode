// Valid Boomerang
/*
Given an array points where points[i] = [xi, yi] represents a point on the X-Y plane, return true if these points are a boomerang.

A boomerang is a set of three points that are all distinct and not in a straight line.

*/
#include <iostream>
#include <vector>
#include <string>
#include <algorithm>

using namespace std;

class Solution {
public:
    // Check if points form a boomerang (not in a straight line)
    bool isBoomerang(vector<vector<int>>& points) {
        int x1 = points[0][0], y1 = points[0][1];
        int x2 = points[1][0], y2 = points[1][1];
        int x3 = points[2][0], y3 = points[2][1];

        // Check if all points are distinct
        if ((x1 == x2 && y1 == y2) ||
            (x1 == x3 && y1 == y3) ||
            (x2 == x3 && y2 == y3)) {
            return false;
        }

        // Check if points are in a straight line using cross product
        return (x2 - x1) * (y3 - y1) != (y2 - y1) * (x3 - x1);
    }

    // Edit distance (Levenshtein Distance)
    int minDistance(string word1, string word2) {
        int m = word1.size(), n = word2.size();
        vector<vector<int>> dp(m + 1, vector<int>(n + 1));

        for (int i = 0; i <= m; ++i) dp[i][0] = i;
        for (int j = 0; j <= n; ++j) dp[0][j] = j;

        for (int i = 1; i <= m; ++i) {
            for (int j = 1; j <= n; ++j) {
                if (word1[i - 1] == word2[j - 1])
                    dp[i][j] = dp[i - 1][j - 1];
                else
                    dp[i][j] = 1 + min({dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1]});
            }
        }
        return dp[m][n];
    }
};

int main() {
    Solution sol;

    // Test Edit Distance
    string word1 = "horse";
    string word2 = "ros";
    cout << "Edit Distance between \"" << word1 << "\" and \"" << word2 << "\": "
         << sol.minDistance(word1, word2) << endl;

    word1 = "intention";
    word2 = "execution";
    cout << "Edit Distance between \"" << word1 << "\" and \"" << word2 << "\": "
         << sol.minDistance(word1, word2) << endl;

    // Test Boomerang
    vector<vector<int>> points1 = {{1, 1}, {2, 3}, {3, 2}};
    vector<vector<int>> points2 = {{1, 1}, {2, 2}, {3, 3}};

    cout << "Is Boomerang 1: " << (sol.isBoomerang(points1) ? "true" : "false") << endl;
    cout << "Is Boomerang 2: " << (sol.isBoomerang(points2) ? "true" : "false") << endl;

    return 0;
}

/*
Example 1:

Input: points = [[1,1],[2,3],[3,2]]
Output: true
Example 2:

Input: points = [[1,1],[2,2],[3,3]]
Output: false
*/