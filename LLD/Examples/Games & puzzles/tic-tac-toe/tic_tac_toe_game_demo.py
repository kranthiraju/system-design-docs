from tic_tac_toe_game import Game, Player, Symbol

class TicTacToeDemo:
    @staticmethod
    def main():
        player1 = Player("Apple", Symbol.X)
        player2 = Player("Bob", Symbol.O)

        game = Game(player1, player2, 3)

        game.makemove(2,1)
        game.makemove(1,1)
        game.makemove(2,3)
        game.makemove(2,2)
        game.makemove(3,1)
        game.makemove(3,3)

        print(f"Result: {game.gameStatus}")

if __name__ == "__main__":
    TicTacToeDemo.main()