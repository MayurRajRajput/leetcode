// Decrypt String from Alphabet to Integer Mapping
/*
You are given a string s formed by digits and '#'. We want to map s to English lowercase characters as follows:

Characters ('a' to 'i') are represented by ('1' to '9') respectively.
Characters ('j' to 'z') are represented by ('10#' to '26#') respectively.
Return the string formed after mapping.

The test cases are generated so that a unique mapping will always exist.
 */
/**
 * @param {string} s
 * @return {string}
 */
var freqAlphabets = function(s) {
    const res = [], a = 'a'.charCodeAt(0) - 1;
    for (let i = 0, n = s.length; i < n; i++) {
        res.push(+(i < n - 2 && s[i + 2] === '#' ? `${s[i++]}${s[i++]}` : s[i]));
    }
    return res.map((v) => String.fromCharCode(a + v)).join('');
};
s = "10#11#12"
console.log(freqAlphabets(s))
/*
Example 1:

Input: s = "10#11#12"
Output: "jkab"
Explanation: "j" -> "10#" , "k" -> "11#" , "a" -> "1" , "b" -> "2".
Example 2:

Input: s = "1326#"
Output: "acz"
 
*/