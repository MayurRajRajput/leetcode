// Find a Corresponding Node of a Binary Tree in a Clone of That Tree
/*
Given two binary trees original and cloned and given a reference to a node target in the original tree.

The cloned tree is a copy of the original tree.

Return a reference to the same node in the cloned tree.

Note that you are not allowed to change any of the two trees or the target node and the answer must be a reference to a node in the cloned tree.

 
*/
/**
 * Definition for a binary tree node.
 * function TreeNode(val) {
 *     this.val = val;
 *     this.left = this.right = null;
 * }
 */
/**
 * @param {TreeNode} original
 * @param {TreeNode} cloned
 * @param {TreeNode} target
 * @return {TreeNode}
 */
// TreeNode constructor
function TreeNode(val) {
    this.val = val;
    this.left = this.right = null;
}

// Helper to build binary tree from array (level-order)
function buildTree(arr) {
    if (!arr.length || arr[0] === null) return null;

    let root = new TreeNode(arr[0]);
    let queue = [root];
    let i = 1;

    while (i < arr.length) {
        let node = queue.shift();

        if (arr[i] != null) {
            node.left = new TreeNode(arr[i]);
            queue.push(node.left);
        }
        i++;

        if (i < arr.length && arr[i] != null) {
            node.right = new TreeNode(arr[i]);
            queue.push(node.right);
        }
        i++;
    }

    return root;
}

// Find a reference to a node by value (DFS)
function findNode(root, val) {
    if (!root) return null;
    if (root.val === val) return root;
    return findNode(root.left, val) || findNode(root.right, val);
}

// Your function
var getTargetCopy = function(original, cloned, target) {
    if (original == null) return null;
    if (original === target) return cloned;
    return getTargetCopy(original.left, cloned.left, target) || 
           getTargetCopy(original.right, cloned.right, target);
};

// === Example Usage ===

// Example 1: tree = [7,4,3,null,null,6,19], target = 3
let arr = [7, 4, 3, null, null, 6, 19];
let original = buildTree(arr);
let cloned = buildTree(arr);
let target = findNode(original, 3);

let result = getTargetCopy(original, cloned, target);
console.log("Target in cloned tree:", result);         // should show the TreeNode with val 3
console.log("Target value:", result.val);              // should output 3
console.log("Same object as cloned? ", result === target); // should be false (different objects)

/*
Example 1:


Input: tree = [7,4,3,null,null,6,19], target = 3
Output: 3
Explanation: In all examples the original and cloned trees are shown. The target node is a green node from the original tree. The answer is the yellow node from the cloned tree.
Example 2:


Input: tree = [7], target =  7
Output: 7
Example 3:


Input: tree = [8,null,6,null,5,null,4,null,3,null,2,null,1], target = 4
Output: 4
 
*/