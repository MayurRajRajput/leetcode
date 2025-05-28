// Partition Array Into Three Parts With Equal Sum
/*
Given an array of integers arr, return true if we can partition the array into three non-empty parts with equal sums.

Formally, we can partition the array if we can find indexes i + 1 < j with (arr[0] + arr[1] + ... + arr[i] == arr[i + 1] + arr[i + 2] + ... + arr[j - 1] == arr[j] + arr[j + 1] + ... + arr[arr.length - 1])
*/
#include <iostream>
#include <vector>
using namespace std;

class Solution {
public:
    bool canThreePartsEqualSum(vector<int>& arr) {
        int totalSum = 0;
        for (int num : arr) {
            totalSum += num;
        }

        if (totalSum % 3 != 0) return false;

        int target = totalSum / 3;
        int count = 0, currentSum = 0;

        for (int i = 0; i < arr.size(); i++) {
            currentSum += arr[i];
            if (currentSum == target) {
                count++;
                currentSum = 0;
                if (count == 2 && i < arr.size() - 1) {
                    return true;
                }
            }
        }

        return false;
    }
};

int main() {
    Solution sol;

    vector<vector<int>> testCases = {
        {0, 2, 1, -6, 6, -7, 9, 1, 2, 0, 1},      // true
        {0, 2, 1, -6, 6, 7, 9, -1, 2, 0, 1},      // false
        {3, 3, 6, 5, -2, 2, 5, 1, -9, 4}          // true
    };

    for (int i = 0; i < testCases.size(); ++i) {
        cout << "Example " << i + 1 << ": "
             << (sol.canThreePartsEqualSum(testCases[i]) ? "true" : "false") << endl;
    }

    return 0;
}

/*
Example 1:

Input: arr = [0,2,1,-6,6,-7,9,1,2,0,1]
Output: true
Explanation: 0 + 2 + 1 = -6 + 6 - 7 + 9 + 1 = 2 + 0 + 1
Example 2:

Input: arr = [0,2,1,-6,6,7,9,-1,2,0,1]
Output: false
Example 3:

Input: arr = [3,3,6,5,-2,2,5,1,-9,4]
Output: true
Explanation: 3 + 3 = 6 = 5 - 2 + 2 + 5 + 1 - 9 + 4
 
*/