class Game:
    def init(self):
        self.board = [' ' for _ in range(24)]
        self.current_player = 1  # 1 для первого игрока, 2 для второго
        self.game_over = False

    def make_move(self, column):
        if not (0 <= column < 24):
            raise ValueError("Неверный номер столбца. Пожалуйста, введите число от 0 до 23.")
        if self.board[column] == ' ':
            self.board[column] = str(self.current_player)
            self.check_win()
            self.current_player = 3 - self.current_player  # Смена игрока
        else:
            raise ValueError("Столбец уже занят. Пожалуйста, выберите другой столбец.")

    def check_win(self):
        # Проверка на победу (по горизонтали, для простоты)
        for i in range(20):
            if self.board[i] == self.board[i+1] == self.board[i+2] == self.board[i+3] and self.board[i] != ' ':
                print(f"Игрок {self.board[i]} победил!")
                self.game_over = True
                return

        # Проверка на ничью (если все поля заняты и нет победителя)
        if ' ' not in self.board:
            print("Ничья!")
            self.game_over = True

    # Оценочная функция (простая версия)
    def evaluate_board(self):
        count = [0, 0]
        for i in range(24):
            if self.board[i] == '1':
                count[0] += 1
            elif self.board[i] == '2':
                count[1] += 1

        # Простая оценка: чем больше фишек у первого игрока, тем лучше
        return count[0] * 10 - count[1] * 10

    # Функция для альфа-бета обрезки (реализация упрощена для демонстрации)
    def alpha_beta(self, depth, alpha, beta, maximizing_player):
        if depth == 0 or self.game_over:
            return self.evaluate_board()

        if maximizing_player:
            max_eval = -float('inf')
            for move in range(24):  # Предположим, что все 24 поля доступны для хода
                new_game = Game()
                new_game.board = self.board.copy()
                try:
                    new_game.make_move(move)
                except ValueError as e:
                    print(e)
                    continue
                eval = new_game.alpha_beta(depth - 1, alpha, beta, False)
                max_eval = max(max_eval, eval)
                alpha = max(alpha, eval)
                if beta <= alpha:
                    break  # Обрезка
            return max_eval
        else:
            min_eval = float('inf')
            for move in range(24):
                new_game = Game()
                new_game.board = self.board.copy()
                try:
                    new_game.make_move(move)
                except ValueError as e:
                    print(e)
                    continue
                eval = new_game.alpha_beta(depth - 1, alpha, beta, True)
                min_eval = min(min_eval, eval)
                beta = min(beta, eval)
                if beta <= alpha:
                    break  # Обрезка
            return min_eval

# Пример использования
game = Game()
while True:
    try:
        if game.game_over:
            print("Game Over!")
            play_again = input("Хотите сыграть еще раз? (yes/no): ")
            if play_again.lower() == "yes":
                game = Game()
            else:
                break
        move = int(input(f"Игрок {game.current_player}, введите номер ячейки (0-23): "))
        game.make_move(move)
    except ValueError as e:
        print(e)
        continue

  
