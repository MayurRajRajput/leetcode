// Verifying an Alien Dictionary
/*
In an alien language, surprisingly, they also use English lowercase letters, but possibly in a different order. The order of the alphabet is some permutation of lowercase letters.

Given a sequence of words written in the alien language, and the order of the alphabet, return true if and only if the given words are sorted lexicographically in this alien language.
*/
#include <vector>
#include <string>
#include <iostream>
using namespace std;

class Solution {
public:
    bool isAlienSorted(vector<string>& words, string order) {
        int mapping[26];
        for (int i = 0; i < 26; i++) {
            mapping[order[i] - 'a'] = i;
        }

        for (int i = 0; i < words.size() - 1; i++) {
            if (!inCorrectOrder(words[i], words[i + 1], mapping)) {
                return false;
            }
        }
        return true;
    }

private:
    bool inCorrectOrder(const string& w1, const string& w2, int mapping[]) {
        int len = min(w1.length(), w2.length());
        for (int i = 0; i < len; i++) {
            if (w1[i] != w2[i]) {
                return mapping[w1[i] - 'a'] < mapping[w2[i] - 'a'];
            }
        }
        return w1.length() <= w2.length();
    }
};

int main() {
    Solution sol;
    vector<string> words = {"hello", "leetcode"};
    string order = "hlabcdefgijkmnopqrstuvwxyz";

    cout << boolalpha;
    cout << "Test : " << sol.isAlienSorted(words, order) << endl;  // true

    return 0;
}

/* 
Example 1:

Input: words = ["hello","leetcode"], order = "hlabcdefgijkmnopqrstuvwxyz"
Output: true
Explanation: As 'h' comes before 'l' in this language, then the sequence is sorted.
Example 2:

Input: words = ["word","world","row"], order = "worldabcefghijkmnpqstuvxyz"
Output: false
Explanation: As 'd' comes after 'l' in this language, then words[0] > words[1], hence the sequence is unsorted.
Example 3:

Input: words = ["apple","app"], order = "abcdefghijklmnopqrstuvwxyz"
Output: false
Explanation: The first three characters "app" match, and the second string is shorter (in size.) According to lexicographical rules "apple" > "app", because 'l' > '∅', where '∅' is defined as the blank character which is less than any other character (More info).
 
*/