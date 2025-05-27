// Sort Colors
/*
Given an array nums with n objects colored red, white, or blue, sort them in-place so that objects of the same color are adjacent, with the colors in the order red, white, and blue.

We will use the integers 0, 1, and 2 to represent the color red, white, and blue, respectively.

You must solve this problem without using the library's sort function.

*/
#include <iostream>
#include <vector>
using namespace std;

class Solution {
public:
    void sortColors(vector<int>& nums) {
        int zero = 0, one = 0, two = 0;
        for (int n : nums) {
            if (n == 0) zero++;
            else if (n == 1) one++;
            else two++;
        }

        for (int i = 0; i < nums.size(); ++i) {
            if (zero > 0) {
                nums[i] = 0;
                zero--;
            } else if (one > 0) {
                nums[i] = 1;
                one--;
            } else {
                nums[i] = 2;
                two--;
            }
        }
    }
};

int main() {
    Solution sol;

    vector<int> nums = {2, 0, 2, 1, 1, 0};
    sol.sortColors(nums);

    cout << "Sorted colors: ";
    for (int n : nums) {
        cout << n << " ";
    }
    cout << endl;

    return 0;
}

/*
Example 1:

Input: nums = [2,0,2,1,1,0]
Output: [0,0,1,1,2,2]
Example 2:

Input: nums = [2,0,1]
Output: [0,1,2]
 
*/