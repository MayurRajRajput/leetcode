// Binary Prefix Divisible By 5
/*
You are given a binary array nums (0-indexed).

We define xi as the number whose binary representation is the subarray nums[0..i] (from most-significant-bit to least-significant-bit).

For example, if nums = [1,0,1], then x0 = 1, x1 = 2, and x2 = 5.
Return an array of booleans answer where answer[i] is true if xi is divisible by 5.
*/
#include <iostream>
#include <vector>
using namespace std;

class Solution {
public:
    vector<bool> prefixesDivBy5(vector<int>& nums) {
        int value = 0;
        vector<bool> result;
        for (int bit : nums) {
            value = ((value << 1) + bit) % 5;
            result.push_back(value == 0);
        }
        return result;
    }
};

void printBoolVector(const vector<bool>& vec) {
    for (bool val : vec) {
        cout << (val ? "true" : "false") << " ";
    }
    cout << endl;
}

int main() {
    Solution sol;

    // Example 1
    vector<int> nums1 = {0, 1, 1};
    cout << "Example 1 Output: ";
    printBoolVector(sol.prefixesDivBy5(nums1));  // Output: [true, false, false]

    // Example 2
    vector<int> nums2 = {1, 1, 1};
    cout << "Example 2 Output: ";
    printBoolVector(sol.prefixesDivBy5(nums2));  // Output: [false, false, false]

    // Custom Example
    vector<int> nums3 = {1, 0, 1, 0, 1};  // Binary values: 1, 2, 5, 10, 21
    cout << "Custom Example Output: ";
    printBoolVector(sol.prefixesDivBy5(nums3));  // Output: [false, false, true, true, false]

    return 0;
}

/*
Example 1:

Input: nums = [0,1,1]
Output: [true,false,false]
Explanation: The input numbers in binary are 0, 01, 011; which are 0, 1, and 3 in base-10.
Only the first number is divisible by 5, so answer[0] is true.
Example 2:

Input: nums = [1,1,1]
Output: [false,false,false]
*/