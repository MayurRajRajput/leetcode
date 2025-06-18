// Find Winner on a Tic Tac Toe Game
/*
Tic-tac-toe is played by two players A and B on a 3 x 3 grid. The rules of Tic-Tac-Toe are:

Players take turns placing characters into empty squares ' '.
The first player A always places 'X' characters, while the second player B always places 'O' characters.
'X' and 'O' characters are always placed into empty squares, never on filled ones.
The game ends when there are three of the same (non-empty) character filling any row, column, or diagonal.
The game also ends if all squares are non-empty.
No more moves can be played if the game is over.
Given a 2D integer array moves where moves[i] = [rowi, coli] indicates that the ith move will be played on grid[rowi][coli]. return the winner of the game if it exists (A or B). In case the game ends in a draw return "Draw". If there are still movements to play return "Pending".

You can assume that moves is valid (i.e., it follows the rules of Tic-Tac-Toe), the grid is initially empty, and A will play first.

 
*/
/**
 * @param {number[][]} moves
 * @return {string}
 */
var tictactoe = function(moves) {
    const x = 'X';
    const o = 'O';
    const board = Array(9);
    const winCombinations = [[0,1,2], [3,4,5], [6,7,8], [0,3,6], [1,4,7], [2,5,8], [0,4,8], [2,4,6]];
    for(let i = 0; i < moves.length; i++) {
        [row, col] = moves[i];
        const index = row * 3 + col;
        board[index] = i % 2 === 0 ? x : o;
    }

    for(let i = 0; i < winCombinations.length; i++) {
        let isA = true;
        let isB = true;

        for(let j = 0; j < winCombinations[0].length; j++) {
            index = winCombinations[i][j];

            isA = isA && board[index] === x;
            isB = isB && board[index] === o;
        }

        if (isA) return 'A';
        if (isB) return 'B';
    }
    return moves.length === 9 ? 'Draw' : 'Pending';
};
moves = [[0,0],[2,0],[1,1],[2,1],[2,2]]
console.log(tictactoe(moves))
/*

Example 1:


Input: moves = [[0,0],[2,0],[1,1],[2,1],[2,2]]
Output: "A"
Explanation: A wins, they always play first.
Example 2:


Input: moves = [[0,0],[1,1],[0,1],[0,2],[1,0],[2,0]]
Output: "B"
Explanation: B wins.
Example 3:


Input: moves = [[0,0],[1,1],[2,0],[1,0],[1,2],[2,1],[0,1],[0,2],[2,2]]
Output: "Draw"
Explanation: The game ends in a draw since there are no moves to make.
 
*/