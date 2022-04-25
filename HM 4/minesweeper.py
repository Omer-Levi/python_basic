"""
Student: Omer levi
ID: 203499090
Assignment no. 4
program: minesweeper.py
"""
from random import randint


class GamePlay:
  

    def __init__(self):
        self.game_board = Board()
        self.lose = False
        self.win = False


    def check_win(self):

        opens = 0
        hidden_mines = self.game_board.get_num_of_mines()
        for row in range(self.game_board.get_size()):
            for col in range(self.game_board.get_size()):
                if self.game_board.this_board[row][col].get_has_mine() and not self.game_board.this_board[row][col].get_hidden():
                    self.lose = True
                if not self.game_board.this_board[row][col].get_has_mine() and not self.game_board.this_board[row][col].get_hidden():
                    opens += 1

        if self.game_board.get_size()**2 == opens + hidden_mines:
            self.win = True
            return

    def player_move(self, row, col):
        x, y = int(row)-1, int(col)-1
        if self.game_board.this_board[x][y].get_has_mine():
            self.game_board.this_board[x][y].set_hidden(False)
            self.lose = True
        else:
            self.game_board.show_all_squares(x, y)


    def expose(self):
        if self.lose == True:
            for row in range(self.game_board.get_size()):
                for col in range(self.game_board.get_size()):
                    if self.game_board.this_board[row][col].get_has_mine():
                        self.game_board.this_board[row][col].set_hidden(False)




    def get_lose(self):
        return self.lose

    def get_game_board(self):
        return self.game_board

    # ----------setters--------

    def set_game_board(self, size, minnum):
        self.game_board = Board(size, minnum)

    def set_lose(self, value):
        if type(value) != bool:
            return
        self.lose = value


class Board:

    def __init__(self, size=4, num_of_mines=8):
        self._size = size
        self._num_of_mines = num_of_mines
        self.this_board = self._create_board
        self._populate()
        self._add_neighbors()

    def show_all_squares(self, row, col):  # recursive
        if not 0 <= row < self._size or not 0 <= col < self._size:
            return
        if self.this_board[row][col].get_neighbor_mines() > 0:
            self.this_board[row][col].set_hidden(False)
            return
        if self.this_board[row][col].get_hidden() == True and \
                self.this_board[row][col].get_has_mine() != True:
            self.this_board[row][col].set_hidden(False)
            for i in range(-1, 2, 1):
                for j in range(-1, 2, 1):
                    self.show_all_squares(row + i, col + j)

    @property
    def _create_board(self):
        return [[MSSquare() for _ in range(self._size)] for _ in range(self._size)]

    def _populate(self):
        counter = self._num_of_mines
        while counter > 0:
            x, y = randint(0, self._size - 1), randint(0, self._size - 1)
            if self.this_board[x][y].get_has_mine():
                continue
            self.this_board[x][y].set_has_mine(True)
            counter -= 1

    def _add_neighbors(self):
        for row in range(0, self._size):
            for col in range(0, self._size):
                if self.this_board[row][col].get_has_mine():
                    for i in range(-1, 2, 1):
                        for j in range(-1, 2, 1):
                            if not 0 <= col + j < self._size or not 0 <= row + i < self._size:
                                continue
                            if not self.this_board[row + i][col + j].get_has_mine():
                                self.this_board[row + i][col + j].set_neighbor_mines(1)

 

    def get_size(self):
        return self._size

    def get_num_of_mines(self):
        return self._num_of_mines

 

    def set_size(self, value):
        self._size = value

    def set_num_of_mines(self, value):
        self._num_of_mines = value

    def __str__(self):
        s = ""
        for row in range(self._size):
            s += " +---+" + "---+" * (self._size - 1) + "\n"
            s += "{0}|".format(row + 1)
            for col in range(self._size):
                s += " {0} |".format(self.this_board[row][col])
            s += '\n'
        s += " +---+" + "---+" * (self._size - 1) + "\n"
        for i in range(1, self._size + 1):
            s += "   {0}".format(i)
        return s


class MSSquare:

    def __init__(self, has_mine=False, hidden=True, neighbor_mines=0):
        self._has_mine = has_mine
        self._hidden = hidden
        self._neighbor_mines = neighbor_mines

   

    def get_has_mine(self):
        return self._has_mine

    def get_hidden(self):
        return self._hidden

    def get_neighbor_mines(self):
        return self._neighbor_mines

 

    def set_has_mine(self, value):
        if type(value) != bool:
            raise Exception("Only  boolean type can go here!")
        self._has_mine = value
        return self._has_mine

    def set_hidden(self, value):
        self._hidden = value

    def set_neighbor_mines(self, value):
        self._neighbor_mines += value

    def __str__(self):
        if self.get_hidden():
            return " "
        if self.get_has_mine() and not self.get_hidden():
            return "x"
        return "{0}".format(self.get_neighbor_mines())



def main():
    game_key = False
    while not game_key:
        n = -1
        num_of_mines = -1
        while not 4 <= n <= 9:
            n = input("To Start MineSweeper first choose board size (4 - 9) :")
            if not n.isdigit() or len(n) != 1:
                n = -1
                continue
            n = int(n)

        while not 1 <= num_of_mines <= 2 * n:
            num_of_mines = input("second choose the number of mines you like to please(1 - {0})".format(n * 2))
            if not num_of_mines.isdigit() or (len(num_of_mines) > 2):
                num_of_mines = -1
                continue
            num_of_mines = int(num_of_mines)
        player_name = input("please enter your name: ")
        current_game_board = Board(n, num_of_mines)
        game = GamePlay()
        game.game_board = current_game_board
        print(game.game_board)

        while game.lose != True and game.win != True:
            playermove = input("enter the coordinates for the mine you like to sweep n,m :")
            if len(playermove) != 3 or not playermove[0].isdigit() or not playermove[2].isdigit() or int(
                    playermove[0]) > game.game_board.get_size() or int(playermove[2]) > game.game_board.get_size():
                continue
            row, col = playermove[0], playermove[2]

            game.player_move(row, col)
            game.check_win()
            game.expose()
            print(game.game_board)
        if game.lose:
            print("Nice try {0}, better luck next time ".format(player_name))
        if game.win:
            print("you win! nicly done {0}".format(player_name))
        continue_game = "?"
        while continue_game != "Y" and continue_game != "N":
            continue_game = input("Would you like to play another game? [Y/N] ").upper()
        if continue_game == "Y":
            continue
        else:
            game_key = True
    print("Thanks for playing minesweep")


main()

