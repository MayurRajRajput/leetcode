// Minimum Time Visiting All Points
/*
On a 2D plane, there are n points with integer coordinates points[i] = [xi, yi]. Return the minimum time in seconds to visit all the points in the order given by points.

You can move according to these rules:

In 1 second, you can either:
move vertically by one unit,
move horizontally by one unit, or
move diagonally sqrt(2) units (in other words, move one unit vertically then one unit horizontally in 1 second).
You have to visit the points in the same order as they appear in the array.
You are allowed to pass through points that appear later in the order, but these do not count as visits.
 
*/
/**
 * @param {number[][]} points
 * @return {number}
 */
var toTime = function(from, to) {
    var xDiff = Math.abs(from[0] - to[0]);
    var yDiff = Math.abs(from[1] - to[1]);

    return Math.max(xDiff, yDiff);
};
var minTimeToVisitAllPoints = function(points) {
    var time = 0;

    for (var i = 1; i < points.length; i++) {
        time += toTime(points[i - 1], points[i]);
    }

    return time;
};
points = [[1,1],[3,4],[-1,0]]
console.log(minTimeToVisitAllPoints(points))
/*
Example 1:


Input: points = [[1,1],[3,4],[-1,0]]
Output: 7
Explanation: One optimal path is [1,1] -> [2,2] -> [3,3] -> [3,4] -> [2,3] -> [1,2] -> [0,1] -> [-1,0]   
Time from [1,1] to [3,4] = 3 seconds 
Time from [3,4] to [-1,0] = 4 seconds
Total time = 7 seconds
Example 2:

Input: points = [[3,2],[-2,2]]
Output: 5
 
*/