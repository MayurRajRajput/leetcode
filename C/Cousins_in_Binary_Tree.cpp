// Cousins in Binary Tree
/*
Given the root of a binary tree with unique values and the values of two different nodes of the tree x and y, return true if the nodes corresponding to the values x and y in the tree are cousins, or false otherwise.

Two nodes of a binary tree are cousins if they have the same depth with different parents.

Note that in a binary tree, the root node is at the depth 0, and children of each depth k node are at the depth k + 1.

*/
// Definition for a binary tree node.
#include<iostream>
using namespace std;

struct TreeNode {
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode() : val(0), left(nullptr), right(nullptr) {}
    TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
    TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
};
class Solution {
public:
    TreeNode* xParent = NULL, *yParent = NULL;
    int xDepth = -1, yDepth = -2;
    bool isCousins(TreeNode* root, int x, int y) {
        dfs(root, NULL, x, y, 0);
        return xDepth == yDepth && xParent != yParent;
    }
    void dfs(TreeNode* root, TreeNode* parent, int x, int y, int depth) {
        if (root == NULL) return;
        if (x == root->val) {
            xParent = parent;
            xDepth = depth;
        } else if (y == root->val) {
            yParent = parent;
            yDepth = depth;
        } else {
            dfs(root->left, root, x, y, depth + 1);
            dfs(root->right, root, x, y, depth + 1);
        }
    }
};
int main() {
    Solution sol;

    // Example: root = [1,2,3,null,4,null,5], x = 5, y = 4
    TreeNode* root = new TreeNode(1);
    root->left = new TreeNode(2);
    root->right = new TreeNode(3);
    root->left->right = new TreeNode(4);
    root->right->right = new TreeNode(5);

    int x = 5, y = 4;
    bool result = sol.isCousins(root, x, y);
    cout << (result ? "True" : "False") << endl;  // Expected: True

    return 0;
}

/*
Example 1:


Input: root = [1,2,3,4], x = 4, y = 3
Output: false
Example 2:


Input: root = [1,2,3,null,4,null,5], x = 5, y = 4
Output: true
Example 3:


Input: root = [1,2,3,null,4], x = 2, y = 3
Output: false
 
*/