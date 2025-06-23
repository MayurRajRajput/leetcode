// Count Negative Numbers in a Sorted Matrix
/*
Given a m x n matrix grid which is sorted in non-increasing order both row-wise and column-wise, return the number of negative numbers in grid.

*/
/**
 * @param {number[][]} grid
 * @return {number}
 */
var countNegatives = function(grid) {
    let count = 0
    const cols = grid[0].length
    for(const row of grid){
        let left = 0
        let right = cols - 1
        while (left <= right){
            const mid = Math.floor(left + (right - left) / 2 )
            if (row[mid] < 0){
                count += right - mid + 1
                right = mid - 1
            }else{
                left = mid + 1
            }
        }
    }
    return count
};
grid = [[4,3,2,-1],[3,2,1,-1],[1,1,-1,-2],[-1,-1,-2,-3]]
console.log(countNegatives(grid))
/*
Example 1:

Input: grid = [[4,3,2,-1],[3,2,1,-1],[1,1,-1,-2],[-1,-1,-2,-3]]
Output: 8
Explanation: There are 8 negatives number in the matrix.
Example 2:

Input: grid = [[3,2],[1,0]]
Output: 0
 
*/