// Maximize Sum Of Array After K Negations
/*
Given an integer array nums and an integer k, modify the array in the following way:

choose an index i and replace nums[i] with -nums[i].
You should apply this process exactly k times. You may choose the same index i multiple times.

Return the largest possible sum of the array after modifying it in this way.

*/

#include <iostream>
#include <vector>
#include <queue>
#include <string>

using namespace std;

class Solution {
public:
    int largestSumAfterKNegations(vector<int>& A, int K) {
        // Min-heap to always access the smallest element
        priority_queue<int, vector<int>, greater<int>> pq(A.begin(), A.end());

        while (K--) {
            int x = pq.top();
            pq.pop();
            pq.push(-x); // Flip sign of the smallest element
        }

        int res = 0;
        while (!pq.empty()) {
            res += pq.top();
            pq.pop();
        }
        return res;
    }
};

int main() {
    Solution sol;

    vector<int> nums1 = {4, 2, 3};
    int k1 = 1;
    cout << "Result 1: " << sol.largestSumAfterKNegations(nums1, k1) << endl;  // Expected: 5

    vector<int> nums2 = {3, -1, 0, 2};
    int k2 = 3;
    cout << "Result 2: " << sol.largestSumAfterKNegations(nums2, k2) << endl;  // Expected: 6

    vector<int> nums3 = {2, -3, -1, 5, -4};
    int k3 = 2;
    cout << "Result 3: " << sol.largestSumAfterKNegations(nums3, k3) << endl;  // Expected: 13

    return 0;
}

/*
Example 1:

Input: nums = [4,2,3], k = 1
Output: 5
Explanation: Choose index 1 and nums becomes [4,-2,3].
Example 2:

Input: nums = [3,-1,0,2], k = 3
Output: 6
Explanation: Choose indices (1, 2, 2) and nums becomes [3,1,0,2].
Example 3:

Input: nums = [2,-3,-1,5,-4], k = 2
Output: 13
Explanation: Choose indices (1, 4) and nums becomes [2,3,-1,5,4].
 
*/