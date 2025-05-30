// Combinations
/*
Given two integers n and k, return all possible combinations of k numbers chosen from the range [1, n].

You may return the answer in any order.
*/
#include <iostream>
#include <vector>
using namespace std;

class Solution {
public:
    vector<vector<int>> combine(int n, int k) {
        vector<vector<int>> result;
        vector<int> combination(k);
        generateCombinations(1, n, k, combination, result);
        return result;
    }

private:
    void generateCombinations(int start, int n, int k, vector<int> &combination, vector<vector<int>> &result) {
        if (k == 0) {
            result.push_back(combination);
            return;
        }
        for (int i = start; i <= n; ++i) {
            combination[combination.size() - k] = i;
            generateCombinations(i + 1, n, k - 1, combination, result);
        }
    }
};

int main() {
    Solution sol;

    int n = 4, k = 2;
    vector<vector<int>> combinations = sol.combine(n, k);

    cout << "Combinations of " << n << " choose " << k << ":\n";
    for (const auto& combo : combinations) {
        cout << "[";
        for (int i = 0; i < combo.size(); ++i) {
            cout << combo[i];
            if (i < combo.size() - 1) cout << ", ";
        }
        cout << "]\n";
    }

    return 0;
}

/*
Example 1:

Input: n = 4, k = 2
Output: [[1,2],[1,3],[1,4],[2,3],[2,4],[3,4]]
Explanation: There are 4 choose 2 = 6 total combinations.
Note that combinations are unordered, i.e., [1,2] and [2,1] are considered to be the same combination.
Example 2:

Input: n = 1, k = 1
Output: [[1]]
Explanation: There is 1 choose 1 = 1 total combination.
 
*/