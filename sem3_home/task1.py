class Board:
    def __init__(self):
        self.board = [['-', '-', '-'],
                      ['-', '-', '-'],
                      ['-', '-', '-'],
                      ]
    def make_move(self, x, y, symbol):
        """Делать ход"""
        if self.board[x][y] == '-':
            self.board[x][y] = symbol
        else:
            return False
        self.checking_the_board()
        return True
    def show(self):
        """Вывод доски в консоль"""
        for item in self.board:
            print(item)
    def checking_the_board(self):
        """Проверка доски"""
        pass
class AI:
    def __init__(self, board):
        self.board = board
    def step(self):
        stop = False
        for row in range(3):
            if not stop:
                for column in range(3):
                    if self.board.board[row][column] == '-':
                        self.board.make_move(row, column, '0')
                        stop = True
                        break
            else:
                break
boardOne = Board()
aiOne = AI(boardOne)
while True:
    boardOne.show()
    x = input('Введите занчение X >>> ')
    if x != 'q':
        y = input('Введите значение Y >>> ')
        if y != 'q':
            if boardOne.make_move(int(x), int(y), 'X'):
                print('ход сделан')
                aiOne.step()
        else:
            break
    else:
        break


# В данной работе выбраны следующие парадигмы:
# 1) ООП. Данная парадигма выбрана, так как классы удобнее читать, удобно обеспечивать за счёт инкапсуляции: атрибуты принадлежат своим объектам и могут быть недоступны для вызова извне своего объекта
# 2) Процедурное программирование, так как задачи класса можно легко разбить на более мелкие подзадачи или шаги, части кода можно использовать несколько раз
# 3) Императивное программирование, так как у нас в коде пристусвуют циклы
