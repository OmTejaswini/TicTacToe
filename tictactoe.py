import math
import copy

X = "X"
O = "O"
EMPTY = None


def initial_state():
#     Returns starting state of the board.

    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
#     Returns player who has the next turn on a board.

    if board == initial_state():
        return X
    if terminal(board):
        return "The game is already over!!"
    x_count = 0
    o_count = 0
    for i in board:
        x_count += i.count(X)
    for i in board:
        o_count += i.count(O)
    
    if x_count > o_count:
        return O
    return X
#     raise NotImplementedError


def actions(board):
#     Returns set of all possible actions (i, j) available on the board.

    if terminal(board):
        return "The game is completed no further actions allowed"
    actions = set()
    turn = player(board)
    for i in range(0,3):
        for j in range(0,3):
            if board[i][j] is EMPTY:
                actions.add((i,j))
    return actions


def result(board, action):
#     Returns the board that results from making move (i, j) on the board.

    brd = copy.deepcopy(board)
    i = action[0]
    j = action[1]
#     if(type(i)!=int | type(j) != int):
#         print(board,"board")
#         print(action, "actions")
#         print(i,j, "i and j")
#     print(i,j)
    if brd[i][j] is not EMPTY:
        raise Exception("Action not possible")
    turn = player(board)
    brd[i][j] = turn
    return brd


def winner(board):
#     Returns the winner of the game, if there is one.

    if board[0][0] == board[1][1] == board[2][2] == X:
        return X
    if board[0][2] == board[1][1] == board[2][0] == X:
        return X
    if board[0][2] == board[1][1] == board[2][0] == O:
        return O
    if board[0][0] == board[1][1] == board[2][2] == O:
        return O
    for i in board:
        if i.count(X) == 3:
            return X
        if i.count(O) == 3:
            return O
    for i in range(0,3):
        if board[0][i] == board[1][i] == board[2][i] == X:
            return X
        if board[0][i] == board[1][i] == board[2][i] == O:
            return O
    return None


def terminal(board):
#     Returns True if game is over, False otherwise.

    if(winner(board)):
        return True
    return not any(ele is None for i in board for ele in i)


def utility(board):
#     Returns 1 if X has won the game, -1 if O has won, 0 otherwise.

    if winner(board) == X:
        return 1
    if winner(board) == O:
        return -1
    if winner(board) is None:
        return 0

def max_value(board, alpha, beta):
    #     Returns maximum value possible in that state of board.

    if terminal(board):
        return utility(board)
    for action in actions(board):
        child = min_value(result(board, action), alpha, beta)
        alpha = max(alpha, child)
        if alpha >= beta:
            return child
    return alpha

def min_value(board, alpha, beta):
    #     Returns maximum value possible in that state of board.

    if terminal(board):
        return utility(board)
    for action in actions(board):
        child = max_value(result(board, action), alpha, beta)
        beta = min(beta, child)
        if alpha >= beta:
            return child
    return beta

def minimax(board):
    if terminal(board):
        return None
    # if(board == initial_state()):
    #     return (1,1)
    alpha = -math.inf
    beta = math.inf
    if player(board) == X:
        action = ()
        v = max_value(board, alpha, beta)
        for a in actions(board):
            if min_value(result(board, a), alpha, beta) == v:
                action = a
        return action

    if player(board) == O:
        action = ()
        v = min_value(board, alpha, beta)
        for a in actions(board):
            if v == max_value(result(board, a), alpha, beta):
                action = a
        return action
    