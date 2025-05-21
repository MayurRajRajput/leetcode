// N-Repeated Element in Size 2N Array
/* 
You are given an integer array nums with the following properties:

nums.length == 2 * n.
nums contains n + 1 unique elements.
Exactly one element of nums is repeated n times.
Return the element that is repeated n times.

*/
#include <vector>
#include <iostream>
#include <unordered_set>
using namespace std;

class Solution {
public:
    int repeatedNTimes(vector<int>& nums) {
        unordered_set<int> seen;
        for (int num : nums) {
            if (seen.count(num)) return num;
            seen.insert(num);
        }
        return -1; // Should never reach here if input is valid
    }
};

int main() {
    Solution sol;

    vector<int> nums = {5, 1, 5, 2, 5, 3, 5, 4};  // Example input
    cout << "Repeated element: " << sol.repeatedNTimes(nums) << endl;  // Output: 5

    return 0;
}

/*
Example 1:

Input: nums = [1,2,3,3]
Output: 3
Example 2:

Input: nums = [2,1,2,5,3,2]
Output: 2
Example 3:

Input: nums = [5,1,5,2,5,3,5,4]
Output: 5

*/