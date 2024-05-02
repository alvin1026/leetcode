"""
https://leetcode.com/problems/snakes-and-ladders/description/

You are given an n x n integer matrix board where the cells are labeled from 1 to n2 in a Boustrophedon style starting from the bottom left of the board (i.e. board[n - 1][0]) and alternating direction each row.

You start on square 1 of the board. In each move, starting from square curr, do the following:

Choose a destination square next with a label in the range [curr + 1, min(curr + 6, n2)].
This choice simulates the result of a standard 6-sided die roll: i.e., there are always at most 6 destinations, regardless of the size of the board.
If next has a snake or ladder, you must move to the destination of that snake or ladder. Otherwise, you move to next.
The game ends when you reach the square n2.
A board square on row r and column c has a snake or ladder if board[r][c] != -1. The destination of that snake or ladder is board[r][c]. Squares 1 and n2 do not have a snake or ladder.

Note that you only take a snake or ladder at most once per move. If the destination to a snake or ladder is the start of another snake or ladder, you do not follow the subsequent snake or ladder.

For example, suppose the board is [[-1,4],[-1,3]], and on the first move, your destination square is 2. You follow the ladder to square 3, but do not follow the subsequent ladder to 4.
Return the least number of moves required to reach the square n2. If it is not possible to reach the square, return -1.

"""


class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        """
        If you encounter question about finding shortest path, think about using BFS.
        By using the queue to iterate through each level
        """
        length = len(board)
        board.reverse()

        def intToPos(square):
            r = (square - 1) // length # round down
            c = (square - 1) % length # works as long as the row is even
            if r % 2:  # if it's odd row, we need to reverse the column
                c = length - 1 - c
            return [r, c]
        
        q = deque()
        q.append([1, 0]) # [square, moves]
        visit = set() # since we want to get the shortest path, if the square is visited in the previous level, we could skip it.

        while q:
            square, moves = q.popleft()
            for i in range(1, 7):
                nextSquare = square + i
                r, c = intToPos(nextSquare)
                if board[r][c] != -1: # if the board value is not -1, we need to find out the destination square through the board
                    nextSquare = board[r][c]
                if nextSquare == length * length:
                    return moves + 1
                if nextSquare not in visit:
                    visit.add(nextSquare)
                    q.append([nextSquare, moves + 1])
                
        return -1