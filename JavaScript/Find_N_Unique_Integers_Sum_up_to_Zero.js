// Find N Unique Integers Sum up to Zero
/*
Given an integer n, return any array containing n unique integers such that they add up to 0.

*/
/**
 * @param {number} n
 * @return {number[]}
 */
var sumZero = function(n) {
    var num = Math.floor(n/2); 
  var res = [];

  for(var i=1;i<=num;i++){
      res.push(i,-i)
     } 

  if(n%2!==0){
    res.push(0)
  }
  
  return res 
};
n = 5
console.log(sumZero(n))
/*
Example 1:

Input: n = 5
Output: [-7,-1,1,3,4]
Explanation: These arrays also are accepted [-5,-1,1,2,3] , [-3,-1,2,-2,4].
Example 2:

Input: n = 3
Output: [-1,0,1]
Example 3:

Input: n = 1
Output: [0]
 
*/