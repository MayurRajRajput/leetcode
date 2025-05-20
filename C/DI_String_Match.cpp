// DI String Match
/* 
A permutation perm of n + 1 integers of all the integers in the range [0, n] can be represented as a string s of length n where:

s[i] == 'I' if perm[i] < perm[i + 1], and
s[i] == 'D' if perm[i] > perm[i + 1].
Given a string s, reconstruct the permutation perm and return it. If there are multiple valid permutations perm, return any of them.

*/
#include<vector>
#include<iostream>
using namespace std;
class Solution {
public:
    vector<int> diStringMatch(string s) {
        vector<int> res;
        for (int l = 0, h = s.size(), i = 0; i <= s.size(); ++i)
        res.push_back(i == s.size() || s[i] == 'I' ? l++ : h--);
    return res;
    }
};
void printVector(const vector<int>& vec){
    for(int num:vec){
        cout << num <<" ";
    }
    cout << endl;
}
int main(){
    Solution sol;
    string s = "IDID";
     vector<int> res1 = sol.diStringMatch(s);
     cout << "Input: " << s << " -> Output: "; printVector(res1);
    return 0;
}
/*
Example 1:

Input: s = "IDID"
Output: [0,4,1,3,2]
Example 2:

Input: s = "III"
Output: [0,1,2,3]
Example 3:

Input: s = "DDI"
Output: [3,2,0,1]
*/