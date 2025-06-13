// Nested Array Generator
/*
Given a multi-dimensional array of integers, return a generator object which yields integers in the same order as inorder traversal.

A multi-dimensional array is a recursive data structure that contains both integers and other multi-dimensional arrays.

inorder traversal iterates over each array from left to right, yielding any integers it encounters or applying inorder traversal to any arrays it encounters.

*/
// Nested Array Generator: Inorder Traversal
/**
 * @param {Array} arr
 * @return {Generator}
 */
var inorderTraversal = function* (arr) {
    for (let element of arr) {
        if (Array.isArray(element)) {
            yield* inorderTraversal(element); // recursively yield from nested arrays
        } else {
            yield element; // yield integer directly
        }
    }
};

// === Example 1 ===
const arr1 = [[[6]], [1, 3], []];
const result1 = [...inorderTraversal(arr1)];
console.log("Output 1:", result1); // [6, 1, 3]

// === Example 2 ===
const arr2 = [];
const result2 = [...inorderTraversal(arr2)];
console.log("Output 2:", result2); // []

// === Example 3 ===
const arr3 = [1, [2, [3, 4]], 5];
const result3 = [...inorderTraversal(arr3)];
console.log("Output 3:", result3); // [1, 2, 3, 4, 5]

/**
 * const gen = inorderTraversal([1, [2, 3]]);
 * gen.next().value; // 1
 * gen.next().value; // 2
 * gen.next().value; // 3
 */
/*
Example 1:

Input: arr = [[[6]],[1,3],[]]
Output: [6,1,3]
Explanation:
const generator = inorderTraversal(arr);
generator.next().value; // 6
generator.next().value; // 1
generator.next().value; // 3
generator.next().done; // true
Example 2:

Input: arr = []
Output: []
Explanation: There are no integers so the generator doesn't yield anything.
 
*/