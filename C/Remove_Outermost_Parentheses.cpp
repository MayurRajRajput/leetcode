// Remove Outermost Parentheses
/*
A valid parentheses string is either empty "", "(" + A + ")", or A + B, where A and B are valid parentheses strings, and + represents string concatenation.

For example, "", "()", "(())()", and "(()(()))" are all valid parentheses strings.
A valid parentheses string s is primitive if it is nonempty, and there does not exist a way to split it into s = A + B, with A and B nonempty valid parentheses strings.

Given a valid parentheses string s, consider its primitive decomposition: s = P1 + P2 + ... + Pk, where Pi are primitive valid parentheses strings.

Return s after removing the outermost parentheses of every primitive string in the primitive decomposition of s.

*/
#include <iostream>
#include <string>
using namespace std;

class Solution {
public:
    string removeOuterParentheses(string s) {
        int count = 0;
        string result = "";
        for (char c : s) {
            if (c == '(') {
                if (count > 0) result += c;
                count++;
            } else { // c == ')'
                count--;
                if (count > 0) result += c;
            }
        }
        return result;
    }
};

int main() {
    Solution sol;

    // Example 1
    string s1 = "(()())(())";
    cout << "Example 1 Output: " << sol.removeOuterParentheses(s1) << endl;  // Output: "()()()"

    // Example 2
    string s2 = "(()())(())(()(()))";
    cout << "Example 2 Output: " << sol.removeOuterParentheses(s2) << endl;  // Output: "()()()()(())"

    // Example 3
    string s3 = "()()";
    cout << "Example 3 Output: " << sol.removeOuterParentheses(s3) << endl;  // Output: ""

    return 0;
}

/*
Example 1:

Input: s = "(()())(())"
Output: "()()()"
Explanation: 
The input string is "(()())(())", with primitive decomposition "(()())" + "(())".
After removing outer parentheses of each part, this is "()()" + "()" = "()()()".
Example 2:

Input: s = "(()())(())(()(()))"
Output: "()()()()(())"
Explanation: 
The input string is "(()())(())(()(()))", with primitive decomposition "(()())" + "(())" + "(()(()))".
After removing outer parentheses of each part, this is "()()" + "()" + "()(())" = "()()()()(())".
Example 3:

Input: s = "()()"
Output: ""
Explanation: 
The input string is "()()", with primitive decomposition "()" + "()".
After removing outer parentheses of each part, this is "" + "" = "".
 
*/