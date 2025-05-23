// Largest Perimeter Triangle
/*
Given an integer array nums, return the largest perimeter of a triangle with a non-zero area, formed from three of these lengths. If it is impossible to form any triangle of a non-zero area, return 0.
*/
#include <iostream>
#include <vector>
#include <algorithm>  // for sort
using namespace std;

class Solution {
public:
    int largestPerimeter(vector<int>& nums) {
        sort(nums.begin(), nums.end());
        int n = nums.size();

        for (int i = n - 3; i >= 0; --i) {
            if (nums[i] + nums[i + 1] > nums[i + 2]) {
                return nums[i] + nums[i + 1] + nums[i + 2];
            }
        }
        return 0;
    }
};

int main() {
    Solution sol;

    // Example 1
    vector<int> nums1 = {2, 1, 2};
    cout << "Example 1 Output: " << sol.largestPerimeter(nums1) << endl;  // 5

    // Example 2
    vector<int> nums2 = {1, 2, 1, 10};
    cout << "Example 2 Output: " << sol.largestPerimeter(nums2) << endl;  // 0

    return 0;
}

/*
Example 1:

Input: nums = [2,1,2]
Output: 5
Explanation: You can form a triangle with three side lengths: 1, 2, and 2.
Example 2:

Input: nums = [1,2,1,10]
Output: 0
Explanation: 
You cannot use the side lengths 1, 1, and 2 to form a triangle.
You cannot use the side lengths 1, 1, and 10 to form a triangle.
You cannot use the side lengths 1, 2, and 10 to form a triangle.
As we cannot use any three side lengths to form a triangle of non-zero area, we return 0.
 
*/