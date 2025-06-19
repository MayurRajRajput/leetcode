// Element Appearing More Than 25% In Sorted Array
/*
Given an integer array sorted in non-decreasing order, there is exactly one integer in the array that occurs more than 25% of the time, return that integer.

*/
/**
 * @param {number[]} arr
 * @return {number}
 */
var findSpecialInteger = function(arr) {
    const n = arr.length;
    const quarter = Math.floor(n / 4);

    for (let i = 0; i < n - quarter; i++) {
        if (arr[i] === arr[i + quarter]) {
            return arr[i];
        }
    }
};
arr = [1,2,2,6,6,6,6,7,10]
console.log(findSpecialInteger(arr))
/*
Example 1:

Input: arr = [1,2,2,6,6,6,6,7,10]
Output: 6
Example 2:

Input: arr = [1,1]
Output: 1
 
*/