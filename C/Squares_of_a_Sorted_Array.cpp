// Squares of a Sorted Array
/*
Given an integer array nums sorted in non-decreasing order, return an array of the squares of each number sorted in non-decreasing order.
*/
#include <iostream>
#include <vector>
#include <cmath>
using namespace std;

class Solution {
public:
    vector<int> sortedSquares(vector<int>& nums) {
        int n = nums.size();
        vector<int> ans(n);
        int left = 0, right = n - 1;
        int pos = n - 1;
        while (left <= right) {
            if (abs(nums[left]) > abs(nums[right])) {
                ans[pos--] = nums[left] * nums[left];
                left++;
            } else {
                ans[pos--] = nums[right] * nums[right];
                right--;
            }
        }
        return ans;
    }
};

void printVector(const vector<int>& vec) {
    for (int num : vec)
        cout << num << " ";
    cout << endl;
}

int main() {
    Solution sol;

    // Example 1
    vector<int> nums1 = {-4, -1, 0, 3, 10};
    cout << "Example 1 Output: ";
    printVector(sol.sortedSquares(nums1));  // [0,1,9,16,100]

    // Example 2
    vector<int> nums2 = {-7, -3, 2, 3, 11};
    cout << "Example 2 Output: ";
    printVector(sol.sortedSquares(nums2));  // [4,9,9,49,121]

    return 0;
}

/*
Example 1:

Input: nums = [-4,-1,0,3,10]
Output: [0,1,9,16,100]
Explanation: After squaring, the array becomes [16,1,0,9,100].
After sorting, it becomes [0,1,9,16,100].
Example 2:

Input: nums = [-7,-3,2,3,11]
Output: [4,9,9,49,121]

 */