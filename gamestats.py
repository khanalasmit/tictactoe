class Stats:
    def __init__(self, screen):
        self.signstat = 1
        self.winner_combination = [
            [0, 1, 2], [3, 4, 5], [6, 7, 8],
            [0, 3, 6], [1, 4, 7], [2, 5, 8],
            [0, 4, 8], [2, 4, 6]
        ]
        self.sideA = []
        self.sideB = []
        self.board = ["-", "-", "-", "-", "-", "-", "-", "-", "-"]
        self.game_active = False

    def winner(self):
        for combination in self.winner_combination:
            if all(pos in self.sideA for pos in combination):
                return 1
            elif all(pos in self.sideB for pos in combination):
                return -1
        if "-" not in self.board:
            return 0
        return None

    def gameover(self):
        for combination in self.winner_combination:
            if self.board[combination[0]] == self.board[combination[1]] == self.board[combination[2]] != "-":
                return True
        if "-" not in self.board:
            return True
        return False
