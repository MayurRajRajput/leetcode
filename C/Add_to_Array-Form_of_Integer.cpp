// Add to Array-Form of Integer
/*
The array-form of an integer num is an array representing its digits in left to right order.

For example, for num = 1321, the array form is [1,3,2,1].
Given num, the array-form of an integer, and an integer k, return the array-form of the integer num + k.

*/
#include <iostream>
#include <vector>
using namespace std;

class Solution {
public:
    vector<int> addToArrayForm(vector<int>& num, int k) {
        for (int i = num.size() - 1; i >= 0; --i) {
            num[i] += k;
            k = num[i] / 10;
            num[i] %= 10;
        }
        while (k > 0) {
            num.insert(num.begin(), k % 10);
            k /= 10;
        }
        return num;
    }
};

// Helper function to print vector contents
void printVector(const vector<int>& vec) {
    for (int val : vec) {
        cout << val << " ";
    }
    cout << endl;
}

int main() {
    Solution sol;

    // Example 1
    vector<int> num1 = {1, 2, 0, 0};
    int k1 = 34;
    cout << "Example 1 Output: ";
    printVector(sol.addToArrayForm(num1, k1));  // [1, 2, 3, 4]

    // Example 2
    vector<int> num2 = {2, 7, 4};
    int k2 = 181;
    cout << "Example 2 Output: ";
    printVector(sol.addToArrayForm(num2, k2));  // [4, 5, 5]

    // Example 3
    vector<int> num3 = {2, 1, 5};
    int k3 = 806;
    cout << "Example 3 Output: ";
    printVector(sol.addToArrayForm(num3, k3));  // [1, 0, 2, 1]

    return 0;
}

/*
Example 1:

Input: num = [1,2,0,0], k = 34
Output: [1,2,3,4]
Explanation: 1200 + 34 = 1234
Example 2:

Input: num = [2,7,4], k = 181
Output: [4,5,5]
Explanation: 274 + 181 = 455
Example 3:

Input: num = [2,1,5], k = 806
Output: [1,0,2,1]
Explanation: 215 + 806 = 1021
 
*/