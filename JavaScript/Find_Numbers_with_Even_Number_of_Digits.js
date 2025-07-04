// Find Numbers with Even Number of Digits
/*
Given an array nums of integers, return how many of them contain an even number of digits.

 
*/
/**
 * @param {number[]} nums
 * @return {number}
 */
var findNumbers = function(nums) {
    let res = 0;

    for (let n of nums) {
        if ((n > 9 && n < 100) || (n > 999 && n < 10000) || n === 100000) {
            res++;
        }
    }

    return res;  
};
nums = [12,345,2,6,7896]
console.log(findNumbers(nums))
/*
Example 1:

Input: nums = [12,345,2,6,7896]
Output: 2
Explanation: 
12 contains 2 digits (even number of digits). 
345 contains 3 digits (odd number of digits). 
2 contains 1 digit (odd number of digits). 
6 contains 1 digit (odd number of digits). 
7896 contains 4 digits (even number of digits). 
Therefore only 12 and 7896 contain an even number of digits.
Example 2:

Input: nums = [555,901,482,1771]
Output: 1 
Explanation: 
Only 1771 contains an even number of digits.
 
*/