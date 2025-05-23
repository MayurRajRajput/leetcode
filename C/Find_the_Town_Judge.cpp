// Find the Town Judge
/*
In a town, there are n people labeled from 1 to n. There is a rumor that one of these people is secretly the town judge.

If the town judge exists, then:

The town judge trusts nobody.
Everybody (except for the town judge) trusts the town judge.
There is exactly one person that satisfies properties 1 and 2.
You are given an array trust where trust[i] = [ai, bi] representing that the person labeled ai trusts the person labeled bi. If a trust relationship does not exist in trust array, then such a trust relationship does not exist.

Return the label of the town judge if the town judge exists and can be identified, or return -1 otherwise. 
 */
#include<vector>
#include<iostream>
using namespace std;
class Solution {
public:
    int findJudge(int n, vector<vector<int>>& trust) {
        int m = trust.size();
        if(m < n - 1) return -1;
        vector<int> score(n + 1, 0);
        for (int i = 0; i < m; ++i) {
            --score[trust[i][0]];
            ++score[trust[i][1]];
        }
        for (int i = 1; i <= n; ++i) {
            if (score[i] == n - 1) return i;
        }
        return -1;
    }
};
int main() {
    Solution sol;

    // Example 1
    int n1 = 2;
    vector<vector<int>> trust1 = {{1, 2}};
    cout << "Example 1 Output: " << sol.findJudge(n1, trust1) << endl; // Expected: 2

    // Example 2
    int n2 = 3;
    vector<vector<int>> trust2 = {{1, 3}, {2, 3}};
    cout << "Example 2 Output: " << sol.findJudge(n2, trust2) << endl; // Expected: 3

    // Example 3
    int n3 = 3;
    vector<vector<int>> trust3 = {{1, 3}, {2, 3}, {3, 1}};
    cout << "Example 3 Output: " << sol.findJudge(n3, trust3) << endl; // Expected: -1

    return 0;
}

/*
Example 1:

Input: n = 2, trust = [[1,2]]
Output: 2
Example 2:

Input: n = 3, trust = [[1,3],[2,3]]
Output: 3
Example 3:

Input: n = 3, trust = [[1,3],[2,3],[3,1]]
Output: -1
*/