// Available Captures for Rook
/*
You are given an 8 x 8 matrix representing a chessboard. There is exactly one white rook represented by 'R', some number of white bishops 'B', and some number of black pawns 'p'. Empty squares are represented by '.'.

A rook can move any number of squares horizontally or vertically (up, down, left, right) until it reaches another piece or the edge of the board. A rook is attacking a pawn if it can move to the pawn's square in one move.

Note: A rook cannot move through other pieces, such as bishops or pawns. This means a rook cannot attack a pawn if there is another piece blocking the path.

Return the number of pawns the white rook is attacking.
*/
#include<vector>
#include<iostream>
using namespace std;
class Solution {
public:
    int numRookCaptures(vector<vector<char>>& board) {
        for(int i = 0; i < 8; ++i){
            for(int j = 0; j < 8; ++j){
                if(board[i][j] == 'R'){
                    int moves = 0;
                    for(int x = i + 1; x < 8; ++x){
                        if(board[x][j] != '.'){
                            if(board[x][j] == 'p') ++moves;
                            break;
                        }
                    }
                    for(int x = i - 1; x >= 0; --x){
                        if(board[x][j] != '.'){
                            if(board[x][j] == 'p') ++moves;
                            break;
                        }
                    }
                    for(int y = j + 1; y < 8; ++y){
                        if(board[i][y] != '.'){
                            if(board[i][y] == 'p') ++moves;
                            break;
                        }
                    }
                    for(int y = j - 1; y >= 0; --y){
                        if(board[i][y] != '.'){
                            if(board[i][y] == 'p') ++moves;
                            break;
                        }
                    }
                    return moves;
                }
            }
        }
        return 0;
    }
};
int main() {
    Solution sol;

    vector<vector<char>> board1 = {
        {'.','.','.','.','.','.','.','.'},
        {'.','.','.','p','.','.','.','.'},
        {'.','.','.','R','.','.','.','p'},
        {'.','.','.','.','.','.','.','.'},
        {'.','.','.','.','.','.','.','.'},
        {'.','.','.','p','.','.','.','.'},
        {'.','.','.','.','.','.','.','.'},
        {'.','.','.','.','.','.','.','.'}
    };

    vector<vector<char>> board2 = {
        {'.','.','.','.','.','.','.'},
        {'.','p','p','p','p','p','.','.'},
        {'.','p','p','B','p','p','.','.'},
        {'.','p','B','R','B','p','.','.'},
        {'.','p','p','B','p','p','.','.'},
        {'.','p','p','p','p','p','.','.'},
        {'.','.','.','.','.','.','.','.'},
        {'.','.','.','.','.','.','.','.'}
    };

    vector<vector<char>> board3 = {
        {'.','.','.','.','.','.','.','.'},
        {'.','.','.','p','.','.','.','.'},
        {'.','.','.','p','.','.','.','.'},
        {'p','p','.','R','.','p','B','.'},
        {'.','.','.','.','.','.','.','.'},
        {'.','.','.','B','.','.','.','.'},
        {'.','.','.','p','.','.','.','.'},
        {'.','.','.','.','.','.','.','.'}
    };

    cout << "Example 1 Output: " << sol.numRookCaptures(board1) << endl; // Expected: 3
    cout << "Example 2 Output: " << sol.numRookCaptures(board2) << endl; // Expected: 0
    cout << "Example 3 Output: " << sol.numRookCaptures(board3) << endl; // Expected: 3

    return 0;
}

/*
Example 1:


Input: board = [[".",".",".",".",".",".",".","."],[".",".",".","p",".",".",".","."],[".",".",".","R",".",".",".","p"],[".",".",".",".",".",".",".","."],[".",".",".",".",".",".",".","."],[".",".",".","p",".",".",".","."],[".",".",".",".",".",".",".","."],[".",".",".",".",".",".",".","."]]

Output: 3

Explanation:

In this example, the rook is attacking all the pawns.

Example 2:


Input: board = [[".",".",".",".",".",".","."],[".","p","p","p","p","p",".","."],[".","p","p","B","p","p",".","."],[".","p","B","R","B","p",".","."],[".","p","p","B","p","p",".","."],[".","p","p","p","p","p",".","."],[".",".",".",".",".",".",".","."],[".",".",".",".",".",".",".","."]]

Output: 0

Explanation:

The bishops are blocking the rook from attacking any of the pawns.

Example 3:


Input: board = [[".",".",".",".",".",".",".","."],[".",".",".","p",".",".",".","."],[".",".",".","p",".",".",".","."],["p","p",".","R",".","p","B","."],[".",".",".",".",".",".",".","."],[".",".",".","B",".",".",".","."],[".",".",".","p",".",".",".","."],[".",".",".",".",".",".",".","."]]

Output: 3

Explanation:

The rook is attacking the pawns at positions b5, d6, and f5.
*/