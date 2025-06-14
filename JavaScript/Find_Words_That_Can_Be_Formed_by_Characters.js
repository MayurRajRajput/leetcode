// Find Words That Can Be Formed by Characters
/*
You are given an array of strings words and a string chars.

A string is good if it can be formed by characters from chars (each character can only be used once for each word in words).

Return the sum of lengths of all good strings in words.

*/
var countCharacters = function(words, chars) {
    const a = 'a'.charCodeAt(0);
    const check = (word) => {
        const tmp = [...counts];
        for (let i = 0; i < word.length; i++) {
            if (--tmp[word.charCodeAt(i) - a] < 0) return 0;
        }
        return word.length;
    };
    const counts = new Array(26).fill(0);
    for (let i = 0; i < chars.length; i++) {
        counts[chars.charCodeAt(i) - a]++;
    }
    return words.reduce((res, word) => res + check(word), 0);
};
words = ["cat","bt","hat","tree"]
chars = "atach"
console.log(countCharacters(words,chars))

/*
Example 1:

Input: words = ["cat","bt","hat","tree"], chars = "atach"
Output: 6
Explanation: The strings that can be formed are "cat" and "hat" so the answer is 3 + 3 = 6.
Example 2:

Input: words = ["hello","world","leetcode"], chars = "welldonehoneyr"
Output: 10
Explanation: The strings that can be formed are "hello" and "world" so the answer is 5 + 5 = 10.
 
*/