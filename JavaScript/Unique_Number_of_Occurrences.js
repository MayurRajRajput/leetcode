// Unique Number of Occurrences
/*
Given an array of integers arr, return true if the number of occurrences of each value in the array is unique or false otherwise.

*/
/**
 * @param {number[]} arr
 * @return {boolean}
 */
var uniqueOccurrences = function(arr) {
    arr.sort((a, b) => a - b);
    let v = [];

    for (let i = 0; i < arr.length; i++) {
        let cnt = 1;

        // Count occurrences of the current element
        while (i + 1 < arr.length && arr[i] === arr[i + 1]) {
            cnt++;
            i++;
        }

        v.push(cnt);
    }

    v.sort((a, b) => a - b);

    for (let i = 1; i < v.length; i++) {
        if (v[i] === v[i - 1]) {
            return false;
        }
    }

    return true;
};
arr = [1,2,2,1,1,3]
console.log(uniqueOccurrences(arr))
/*
Example 1:

Input: arr = [1,2,2,1,1,3]
Output: true
Explanation: The value 1 has 3 occurrences, 2 has 2 and 3 has 1. No two values have the same number of occurrences.
Example 2:

Input: arr = [1,2]
Output: false
Example 3:

Input: arr = [-3,0,1,-3,1,1,1,-3,10,0]
Output: true
 
*/