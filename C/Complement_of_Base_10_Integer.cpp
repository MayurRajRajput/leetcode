// Complement of Base 10 Integer
/*
The complement of an integer is the integer you get when you flip all the 0's to 1's and all the 1's to 0's in its binary representation.

For example, The integer 5 is "101" in binary and its complement is "010" which is the integer 2.
Given an integer n, return its complement.
*/
#include <iostream>
using namespace std;

class Solution {
public:
    int bitwiseComplement(int n) {
        if (n == 0) {
            return 1;
        }
        int rem, ans = 0, mul = 1;
        while (n) {
            rem = n % 2;
            rem = rem ^ 1;  // Flip the bit
            n /= 2;
            ans = ans + rem * mul;
            mul *= 2;
        }
        return ans;
    }
};

int main() {
    Solution sol;

    cout << "Complement of 5: " << sol.bitwiseComplement(5) << endl;   // Output: 2
    cout << "Complement of 7: " << sol.bitwiseComplement(7) << endl;   // Output: 0
    cout << "Complement of 10: " << sol.bitwiseComplement(10) << endl; // Output: 5
    cout << "Complement of 0: " << sol.bitwiseComplement(0) << endl;   // Output: 1

    return 0;
}

/*
Example 1:

Input: n = 5
Output: 2
Explanation: 5 is "101" in binary, with complement "010" in binary, which is 2 in base-10.
Example 2:

Input: n = 7
Output: 0
Explanation: 7 is "111" in binary, with complement "000" in binary, which is 0 in base-10.
Example 3:

Input: n = 10
Output: 5
Explanation: 10 is "1010" in binary, with complement "0101" in binary, which is 5 in base-10.
 
*/