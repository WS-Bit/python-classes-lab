class Game:
    def __init__(self) -> None:
        self.turn = 'X'
        self.tie = False
        self.winner = None
        self.board = {
            'a1': None, 'b1': None, 'c1': None,
            'a2': None, 'b2': None, 'c2': None,
            'a3': None, 'b3': None, 'c3': None,
        }

    def play_game(self):
        print("Let's play a game!")
        while not self.winner and not self.tie:
            self.render() # <-- this calls the print board and print message functions
            self.get_move() # <-- this calls the user to input a move to the board
            self.check_for_winner() # <-- this then checks for a winner of the game
            self.check_for_tie() # <-- if there is no winner, check for a tie
            self.switch_turn() # <-- this switches the player

        
        self.render() # <-- this renders the board for the last time with who won

    def get_move(self):
        while True: # <-- we force the function into a While loop to stop an invalid input exiting the function
            move = input(f"Enter a valid move (example: a1): ").lower()
            if (move in self.board and self.board[move] is None):
                self.board[move] = self.turn
                break # <-- if this is called, the infinite loop breaks
            else:
                print("Invalid move, please input a valid position!")

    def switch_turn(self):
        if (self.winner is None):
            opposite_of = { 'X': 'O', 'O': 'X' }
            self.turn = opposite_of[self.turn]


    def check_for_winner(self):
        b = self.board
        # horizontal win conditions
        if (b['a1'] and (b['a1'] == b['b1'] == b['c1'])):
            self.winner = self.turn
        if (b['a2'] and (b['a2'] == b['b2'] == b['c2'])):
            self.winner = self.turn
        if (b['a3'] and (b['a3'] == b['b3'] == b['c3'])):
            self.winner = self.turn
        # vertical win conditions
        if (b['a1'] and (b['a1'] == b['a2'] == b['a3'])):
            self.winner = self.turn
        if (b['b1'] and (b['b1'] == b['b2'] == b['b3'])):
            self.winner = self.turn
        if (b['c1'] and (b['c1'] == b['c2'] == b['c3'])):
            self.winner = self.turn
        #diagonal win conditions
        if (b['a1'] and (b['a1'] == b['b2'] == b['c3'])):
            self.winner = self.turn
        if (b['c1'] and (b['c1'] == b['b2'] == b['a3'])):
            self.winner = self.turn

    def check_for_tie(self):
        if (None not in self.board.values() and self.winner is None):
            self.tie = True

    def render(self): # <-- here are the print board and print message functions
        self.print_board()
        self.print_message()

    def print_board(self):
        b = self.board
        print(f"""
                A   B   C
            1)  {b['a1'] or ' '} | {b['b1'] or ' '} | {b['c1'] or ' '}
                ----------
            2)  {b['a2'] or ' '} | {b['b2'] or ' '} | {b['c2'] or ' '}
                ----------
            3)  {b['a3'] or ' '} | {b['b3'] or ' '} | {b['c3'] or ' '}
        """)

    def print_message(self):
        ## If there is a tie: print("Tie game!")
        if (self.tie):
            print("It's a tie...")
        ## If there is a winner: print(f"{self.winner} wins the game!")
        elif (self.winner):
            print(f"{self.winner} wins the game!")
        ## Otherwise: print(f"It's player {self.turn}'s turn!")
        else:
            print(f"It's player {self.turn}'s turn!")



game_instance = Game()
game_instance.play_game()

