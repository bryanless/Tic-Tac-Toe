# Create game board
# Ask player to play as X or O
# X plays first, MAX
# O plays next, MIN

# Node
# DFS
# MINIMAX Algorithm

# State - game board
# Player(s) - defines which player has the move in a state
# Action(s) - Available moves
# Result(s, a) - State after a move is taken
# Terminal-Test(s) - Is it a winning condition - bool
# Utility(s) - Who wins - enum(-1, 0, 1)


# Gameplay
from Game import Game

# Tic Tac Toe
game = Game()
game.startGame()
