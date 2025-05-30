// Edit Distance
/*
Given two strings word1 and word2, return the minimum number of operations required to convert word1 to word2.

You have the following three operations permitted on a word:

Insert a character
Delete a character
Replace a character
 
*/
#include <iostream>
#include <vector>
#include <string>
#include <algorithm>

using namespace std;

class Solution {
public:
    int minDistance(string word1, string word2) {
        int n = word1.size();
        int m = word2.size();
        vector<vector<int>> dp(n + 1, vector<int>(m + 1, 0));

        // Initialize base cases
        for (int i = 0; i <= n; ++i)
            dp[i][0] = i;
        for (int j = 0; j <= m; ++j)
            dp[0][j] = j;

        // Fill the dp table
        for (int i = 1; i <= n; ++i) {
            for (int j = 1; j <= m; ++j) {
                if (word1[i - 1] == word2[j - 1]) {
                    dp[i][j] = dp[i - 1][j - 1];
                } else {
                    dp[i][j] = 1 + min({dp[i - 1][j],    // Delete
                                        dp[i][j - 1],    // Insert
                                        dp[i - 1][j - 1] // Replace
                                       });
                }
            }
        }

        return dp[n][m];
    }
};

int main() {
    Solution sol;

    string word1 = "horse";
    string word2 = "ros";
    cout << "Edit Distance between \"" << word1 << "\" and \"" << word2 << "\": " 
         << sol.minDistance(word1, word2) << endl;

    word1 = "intention";
    word2 = "execution";
    cout << "Edit Distance between \"" << word1 << "\" and \"" << word2 << "\": " 
         << sol.minDistance(word1, word2) << endl;

    return 0;
}

/*
Example 1:

Input: word1 = "horse", word2 = "ros"
Output: 3
Explanation: 
horse -> rorse (replace 'h' with 'r')
rorse -> rose (remove 'r')
rose -> ros (remove 'e')
Example 2:

Input: word1 = "intention", word2 = "execution"
Output: 5
Explanation: 
intention -> inention (remove 't')
inention -> enention (replace 'i' with 'e')
enention -> exention (replace 'n' with 'x')
exention -> exection (replace 'n' with 'c')
exection -> execution (insert 'u')
 
*/