// Sum of Root To Leaf Binary Numbers
/*
You are given the root of a binary tree where each node has a value 0 or 1. Each root-to-leaf path represents a binary number starting with the most significant bit.

For example, if the path is 0 -> 1 -> 1 -> 0 -> 1, then this could represent 01101 in binary, which is 13.
For all leaves in the tree, consider the numbers represented by the path from the root to that leaf. Return the sum of these numbers.

The test cases are generated so that the answer fits in a 32-bits integer.
*/

// Definition for a binary tree node.
#include <iostream>
using namespace std;

// Definition for a binary tree node.
struct TreeNode {
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
};

class Solution {
    int sumRootToLeafHelper(TreeNode* root, int sum) {
        if (!root) return 0;
        sum = (sum << 1) | root->val;  // Binary left shift and add current bit
        if (!root->left && !root->right) return sum;  // Leaf node
        return sumRootToLeafHelper(root->left, sum) + sumRootToLeafHelper(root->right, sum);
    }
public:
    int sumRootToLeaf(TreeNode* root) {
        return sumRootToLeafHelper(root, 0);
    }
};

// Helper to build the tree from the example: [1,0,1,0,1,0,1]
TreeNode* buildExampleTree() {
    TreeNode* root = new TreeNode(1);
    root->left = new TreeNode(0);
    root->right = new TreeNode(1);
    root->left->left = new TreeNode(0);
    root->left->right = new TreeNode(1);
    root->right->left = new TreeNode(0);
    root->right->right = new TreeNode(1);
    return root;
}

int main() {
    Solution sol;

    TreeNode* root = buildExampleTree();
    cout << "Sum of Root to Leaf Binary Numbers: " << sol.sumRootToLeaf(root) << endl;

    // Cleanup tree (optional in small programs, but good practice)
    // Normally you'd implement a destructor or use smart pointers

    return 0;
}

/*
Example 1:


Input: root = [1,0,1,0,1,0,1]
Output: 22
Explanation: (100) + (101) + (110) + (111) = 4 + 5 + 6 + 7 = 22
Example 2:

Input: root = [0]
Output: 0
 
*/