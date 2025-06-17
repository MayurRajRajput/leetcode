// Check If It Is a Straight Line
/*
You are given an array coordinates, coordinates[i] = [x, y], where [x, y] represents the coordinate of a point. Check if these points make a straight line in the XY plane.
*/
/**
 * @param {number[][]} coordinates
 * @return {boolean}
 */
var checkStraightLine = function(coordinates) {
    const [[x1, y1], [x2, y2]] = coordinates.slice(0, 2), dy = y2 - y1, dx = x2 - x1;
    return coordinates.every(([x, y]) => (y - y1) * dx === dy * (x - x1));
};
coordinates = [[1,2],[2,3],[3,4],[4,5],[5,6],[6,7]]
console.log(checkStraightLine(coordinates))
/*
Example 1:



Input: coordinates = [[1,2],[2,3],[3,4],[4,5],[5,6],[6,7]]
Output: true
Example 2:



Input: coordinates = [[1,1],[2,2],[3,4],[4,5],[5,6],[7,7]]
Output: false
 
*/