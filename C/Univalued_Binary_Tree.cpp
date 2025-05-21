// Univalued Binary Tree
/*
A binary tree is uni-valued if every node in the tree has the same value.

Given the root of a binary tree, return true if the given tree is uni-valued, or false otherwise.
 
*/
#include <iostream>
#include <vector>
using namespace std;

// Definition for a binary tree node.
struct TreeNode {
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
    TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
};

class Solution {
public:
    bool Find(TreeNode* root, int val) {
        if (!root) return true;
        if (root->val != val) return false;
        return Find(root->left, val) && Find(root->right, val);
    }

    bool isUnivalTree(TreeNode* root) {
        if (!root) return true;
        return Find(root, root->val);
    }
};

int main() {
    Solution sol;

    // Example: [1,1,1,1,1,null,1]
    TreeNode* root = new TreeNode(1,
        new TreeNode(1,
            new TreeNode(1),
            new TreeNode(1)
        ),
        new TreeNode(1,
            nullptr,
            new TreeNode(1)
        )
    );

    cout << boolalpha;
    cout << "Is tree univalued? " << sol.isUnivalTree(root) << endl;  // Output: true

    // Clean up memory (optional in small test programs, but good practice)
    // In real code, you should delete each node properly or use smart pointers

    return 0;
}

/*
Example 1:


Input: root = [1,1,1,1,1,null,1]
Output: true
Example 2:


Input: root = [2,2,2,5,2]
Output: false
*/