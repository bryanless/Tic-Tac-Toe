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
from copy import deepcopy
from math import inf
import sys

from Board import Board


class Game:
    # Start the game
	def startGame(self):
		self.showMenu()

    # Show main menu
	def showMenu(self):
		choice = ''
		while (True):
			print('''=== Tic Tac Toe ===
1. Play
2. Quit
			''')

			choice = input('Choice: ')
			if (choice == '1'):
				self.choosePlayer()
			elif (choice == '2'):
				sys.exit()
			else:
				self.invalidInput()

    # Ask player to play as X or O
	def choosePlayer(self):
		choice = ''
		while (True):
			print('''Play as X or O?
> X will play first
			''')

			choice = input('Choice: ')
			if (choice.upper() == 'X' or choice.upper() == 'O'):
				self.playGame(choice.upper())
				break
			else:
				self.invalidInput()

    # Play game
	def playGame(self, player: str):
		self.initializeGame(player)
		print()
		self.gameBoard.show()

		while (True):
			choice = ''
			# Check winning condition - Terminal-Test(s)
			if (self.isGameOver(self.gameBoard)):
				self.gameWinner(self.gameBoard)
				break

			# Check if player's turn
			if (self.isPlayerTurn):
				while (True):
					print('Your turn')

					choice = int(input('Choice: '))
					if (choice - 1) in self.gameBoard.getAvailableBlock():
						self.gameBoard.replace((choice - 1), self.player)
						self.isPlayerTurn = False
						break
					else:
						print('Invalid move')
			else:
				print('Opponent is thinking...')
				self.gameBoard.replace(self.minimax(), self.opponent)
				self.isPlayerTurn = True
			
			self.gameBoard.show()


    # Initialize game
	def initializeGame(self, player: str):
		self.gameBoard = Board()
		self.player = player
		self.opponent = 'O' if player == 'X' else 'X'
		self.isPlayerTurn = True if player == 'X' else False

    # Input error handling
	def invalidInput(self):
		print('Invalid input\n')

	# Minimax algorithm
	def minimax(self):
		# X is MAX
		# O is MIN

		# Default chosen block in game board
		action = -1

		if (self.opponent == 'X'):
			utilityValue = -inf

			for index in self.gameBoard.getAvailableBlock():
				currentUtilityValue = self.minValue(self.makeMove(self.gameBoard, index, self.opponent))

				if (utilityValue < currentUtilityValue):
					utilityValue = currentUtilityValue
					action = index
		else:
			utilityValue = +inf

			for index in self.gameBoard.getAvailableBlock():
				currentUtilityValue = self.maxValue(self.makeMove(self.gameBoard, index, self.opponent))
				
				if (currentUtilityValue < utilityValue):
					utilityValue = currentUtilityValue
					action = index

		return action
	
	def maxValue(self, gameBoard: Board):
		# X is MAX

		# Terminal-Test
		if (self.isGameOver(gameBoard)):
			return self.isPlayerWin(gameBoard)

		# Default utility value
		utilityValue = -inf

		for index in gameBoard.getAvailableBlock():
			currentUtilityValue = self.minValue(self.makeMove(gameBoard, index, 'X'))
			if (utilityValue < currentUtilityValue):
				utilityValue = currentUtilityValue

		return utilityValue

	def minValue(self, gameBoard: Board):
		# O is MIN

		# Terminal-Test
		if (self.isGameOver(gameBoard)):
			return self.isPlayerWin(gameBoard)

		# Default utility value
		utilityValue = inf

		for index in gameBoard.getAvailableBlock():
			currentUtilityValue = self.maxValue(self.makeMove(gameBoard, index, 'O'))
			if (currentUtilityValue < utilityValue):
				utilityValue = currentUtilityValue

		return utilityValue

	# Result(s, a)
	def makeMove(self, gameBoard: Board, index: int, gameTurn: str):
		currentBoard = deepcopy(gameBoard)
		currentBoard.replace(index, gameTurn)
		return currentBoard

	# Terminal-Test(s)
	def isGameOver(self, gameBoard: Board):
		# All blocks are filled
		if not (gameBoard.getAvailableBlock()):
			return True

		# Any win condition is reached
		for winCondition in gameBoard.winConditions:
			# Check if 3 blocks in win condition has the same player
			if (gameBoard.board[winCondition[0]] == gameBoard.board[winCondition[1]]
			and gameBoard.board[winCondition[1]] == gameBoard.board[winCondition[2]]
			and gameBoard.board[winCondition[0]] == gameBoard.board[winCondition[2]]):
				return True

		return False

	# Utility(s)
	def isPlayerWin(self, gameBoard: Board):
		# Any win condition is reached
		for winCondition in gameBoard.winConditions:
			# Check if 3 blocks in win condition has the same player
			if (gameBoard.board[winCondition[0]] == gameBoard.board[winCondition[1]]
			and gameBoard.board[winCondition[1]] == gameBoard.board[winCondition[2]]
			and gameBoard.board[winCondition[0]] == gameBoard.board[winCondition[2]]):
				# X wins
				if (gameBoard.board[winCondition[0]] == 'X'):
					return 1
				
				# O wins
				return -1

		# Draw
		return 0

	def gameWinner(self, gameBoard: Board):
		for winCondition in gameBoard.winConditions:
			# Check if 3 blocks in win condition has the same player
			if (gameBoard.board[winCondition[0]] == gameBoard.board[winCondition[1]]
			and gameBoard.board[winCondition[1]] == gameBoard.board[winCondition[2]]
			and gameBoard.board[winCondition[0]] == gameBoard.board[winCondition[2]]):
				# Player wins
				if (gameBoard.board[winCondition[0]] == self.player):
					print('You Win!\n')
					return
				
				print('You Lose!\n')
				return

		# Draw
		print('It\'s a draw\n')