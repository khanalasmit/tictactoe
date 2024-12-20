class Stats:
    def __init__(self,screen):
        self.signstat=1
        self.winner_combination = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Horizontal
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Vertical
        [0, 4, 8], [2, 4, 6]              # Diagonal
        ]
        self.sideA=[]
        self.sideB=[]
        self.board=["-", "-", "-", "-", "-", "-", "-", "-", "-"]
        self.game_active=False
        
    def winner(self):
        for combination in self.winner_combination:
            if all(pos in self.sideA for pos in combination):  # Check if `sideA` has a winning combination
                return 1
            if all(pos in self.sideB for pos in combination):  # Check if `sideB` has a winning combination
                return -1
    def gameover(self):
    # Check for all winning conditions (rows, columns, diagonals)
        if (self.board[0] == self.board[1] == self.board[2] != "-") or \
        (self.board[3] == self.board[4] == self.board[5] != "-") or \
        (self.board[6] == self.board[7] == self.board[8] != "-") or \
        (self.board[0] == self.board[3] == self.board[6] != "-") or \
        (self.board[1] == self.board[4] == self.board[7] != "-") or \
        (self.board[2] == self.board[5] == self.board[8] != "-") or \
        (self.board[0] == self.board[4] == self.board[8] != "-") or \
        (self.board[2] == self.board[4] == self.board[6] != "-"):
            return True
        else:
            return False

        