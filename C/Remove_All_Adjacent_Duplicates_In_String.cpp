// Remove All Adjacent Duplicates In String
/*
You are given a string s consisting of lowercase English letters. A duplicate removal consists of choosing two adjacent and equal letters and removing them.

We repeatedly make duplicate removals on s until we no longer can.

Return the final string after all such duplicate removals have been made. It can be proven that the answer is unique.
*/
#include <iostream>
#include <string>
using namespace std;

class Solution {
public:
    string removeDuplicates(string s) {
        string temp = "";
        int i = 0;
        
        while (i < s.length()) {
            if (temp.empty() || s[i] != temp.back()) {
                temp.push_back(s[i]);
            } else {
                temp.pop_back();
            }
            i++;
        }
        
        return temp;
    }
};

int main() {
    Solution sol;

    string s1 = "abbaca";
    cout << "Input: " << s1 << "\nOutput: " << sol.removeDuplicates(s1) << endl;

    string s2 = "azxxzy";
    cout << "Input: " << s2 << "\nOutput: " << sol.removeDuplicates(s2) << endl;

    string s3 = "aabbccddeeffgghhii";
    cout << "Input: " << s3 << "\nOutput: " << sol.removeDuplicates(s3) << endl;

    return 0;
}

/*
Example 1:

Input: s = "abbaca"
Output: "ca"
Explanation: 
For example, in "abbaca" we could remove "bb" since the letters are adjacent and equal, and this is the only possible move.  The result of this move is that the string is "aaca", of which only "aa" is possible, so the final string is "ca".
Example 2:

Input: s = "azxxzy"
Output: "ay"
 
*/