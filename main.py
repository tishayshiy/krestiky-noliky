board = [['1', '2', '3'], ['4', '5', '6'], ['7', '8', '9']] #пустой игровой стол

class TicTacToe():

    def __init__(self, board):
        self.board = board

    def board_print(self): #выводит стол
        print(self.board[0][0] + '   ' + self.board[0][1] + '   ' + self.board[0][2])
        print()
        print(self.board[1][0] + '   ' + self.board[1][1] + '   ' + self.board[1][2])
        print()
        print(self.board[2][0] + '   ' + self.board[2][1] + '   ' + self.board[2][2])

    def moves(self): #проверка можно ли совершить ход, возвращает список доступных ходов
        movess = []
        for i in self.board:
            for j in i:
                if j != 'X' and j != 'O':
                    movess.append(j)
        return movess

    def win(self, XO): #проверка победил ли игрок
        for i in self.board:
            if i.count(XO) == 3:
                return True
        for i in range(3):
            if self.board[0][i] == XO and self.board[1][i] == XO and self.board[2][i] == XO:
                return True
        if self.board[0][0] == XO and self.board[1][1] == XO and self.board[2][2] == XO:
            return True
        elif self.board[0][2] == XO and self.board[1][1] == XO and self.board[2][0] == XO:
            return True
        return False

    def game_over(self): #проверка завершилась ли игра
        self.moves()
        if len(self.moves()) == 0 or self.win('X') == True or self.win('O') == True:
            return True
        return False

    def get_move(self, turn): #получение от игрока координаты
        move = int(input(f'Ход игрока {turn}: '))
        return move

    def num_to_X_or_O(self, turn, num): #закрашивание клетки на поле
        string = (num - 1) // 3
        col = (num - 1) % 3
        self.board[string][col] = str(turn)


game = TicTacToe(board) 
while not game.game_over():
    game.board_print()
    X = game.get_move('X')
    game.num_to_X_or_O('X', X)
    game.board_print()
    if game.game_over():
        break
    O = game.get_move('O')
    game.num_to_X_or_O('O', O)

if game.win('X'):
    print('Крестики победили')
elif game.win('O'):
    print('Нолики победили')
else: print('Ну, что сказать.. Ничья!')
