class Board():
	def __init__(self):
		self.board = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
		self.winConditions = [
			[0, 1, 2], [3, 4, 5], [6, 7, 8],
			[0, 3, 6], [1, 4, 7], [2, 5, 8],
			[0, 4, 8], [2, 4, 6]]

	def show(self):
		for i in range(len(self.board)):
			block = self.board[i]
			print('| {} '.format(block), end='')
			
			if ((i + 1) % 3 == 0):
				print('|')
		print()

	def replace(self, index: int, player: str):
		self.board[index] = player

	# Action(s)
	def getAvailableBlock(self):
		availableBlock = []

		for i in range(len(self.board)):
			block = self.board[i].upper()
			if (block != 'X' and block != 'O'):
				availableBlock.append(i)
		
		return availableBlock