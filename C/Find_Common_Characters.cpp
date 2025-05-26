// Find Common Characters
/*
Given a string array words, return an array of all characters that show up in all strings within the words (including duplicates). You may return the answer in any order.
*/
#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#include <climits>  // for INT_MAX

using namespace std;

class Solution {
public:
    vector<string> commonChars(vector<string>& words) {
        vector<int> minFreq(26, INT_MAX);  // initialize with max int
        for (const string& word : words) {
            vector<int> freq(26, 0);
            for (char c : word) {
                freq[c - 'a']++;
            }
            for (int i = 0; i < 26; ++i) {
                minFreq[i] = min(minFreq[i], freq[i]);
            }
        }

        vector<string> res;
        for (int i = 0; i < 26; ++i) {
            while (minFreq[i]-- > 0) {
                res.push_back(string(1, 'a' + i));
            }
        }
        return res;
    }
};

int main() {
    Solution sol;

    vector<string> strs1 = {"bella", "label", "roller"};
    vector<string> result1 = sol.commonChars(strs1);

    cout << "Common characters: ";
    for (const string& c : result1) {
        cout << c << " ";
    }
    cout << endl;

    vector<string> strs2 = {"cool", "lock", "cook"};
    vector<string> result2 = sol.commonChars(strs2);

    cout << "Common characters: ";
    for (const string& c : result2) {
        cout << c << " ";
    }
    cout << endl;

    return 0;
}



/*
Example 1:

Input: words = ["bella","label","roller"]
Output: ["e","l","l"]
Example 2:

Input: words = ["cool","lock","cook"]
Output: ["c","o"]
*/