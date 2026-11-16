# Tic-tac-toe game
# Requirements
# 1. game has board 3x3 grid with symbol (X/O) with two players
# 2. first player who get three symbols in row (horizontal/vertical/diagonally)
# 3. if all cells are filled and no player won then game is draw
from enum import Enum

class Symbol(Enum):
    EMPTY="EMPTY"
    X="X"
    O="O"

class GameStatus(Enum):
    WINNER_X="X"
    WINNER_O="O"
    IN_PROGRESS="IN_PROGRESS"
    DRAW="DRAW"


class Player:
    def __init__(self, name:str, symbol: Symbol):
        self.name=name
        self.symbol=symbol

class Cell:
    def __init__(self,symbol):
        self.symbol=symbol

    def changeSymbol(self, value: Symbol):
        self.symbol=value

    def isEmpty(self):
        return self.symbol==Symbol.EMPTY

class Board:
    def __init__(self,board_size:int):
        self.cells=[[Cell(Symbol.EMPTY) for _ in range(board_size)] for _ in range(board_size)]
        self.empty_cells=board_size**2

    def placeSymbol(self,row:int, col:int, symbol:Symbol):
        if self.isCellEmpty(row,col):
            self.cells[row-1][col-1].changeSymbol(symbol)
            self.empty_cells-=1

    def isCellEmpty(self, row:int, col:int):
        return self.cells[row-1][col-1].isEmpty()

    def isBoardFull(self):
        return self.empty_cells==0

class Game:
    def __init__(self, player1: Player, player2: Player, board_size:int):
        self.board_size=board_size
        self.board=Board(board_size)
        self.players=[player1, player2]
        self.currentPlayerIndex=0
        self.gameStatus=GameStatus.IN_PROGRESS

    def __str__(self):
        for i in range(self.board_size):
            for j in range(self.board_size):
                print(self.board.cells[i][j].symbol, end=" ")

            print(end="\n")


    def makemove(self, row:int , col:int):
        if self.board.isBoardFull():
            self.gameStatus = GameStatus.DRAW
        
        if self.board.isCellEmpty(row,col):
            currentSymbol = self.players[self.currentPlayerIndex].symbol
            self.board.placeSymbol(row,col,currentSymbol)
            self.currentPlayerIndex = 1 if self.currentPlayerIndex==0 else 0

            if self._check_win(row,col,currentSymbol):
                if currentSymbol==Symbol.X:
                    self.gameStatus = GameStatus.WINNER_X
                if currentSymbol==Symbol.O:
                    self.gameStatus = GameStatus.WINNER_O
            else:
                self.gameStatus = GameStatus.IN_PROGRESS
                                

    def _check_win(self, row:int, col:int, symbol: Symbol):
        i=0
        while i<self.board_size and self.board.cells[i][col-1].symbol==symbol:
            i+=1

        if i==self.board_size:
            return True

        i=0
        while i<self.board_size and self.board.cells[row-1][i].symbol==symbol:
            i+=1

        if i==self.board_size:
            return True

        i=0
        while i<self.board_size and self.board.cells[i][i].symbol==symbol:
            i+=1
        
        if i==self.board_size:
            return True

        i=0
        while i<self.board_size and self.board.cells[i][self.board_size - 1 -i].symbol==symbol:
            i+=1
        
        if i==self.board_size:
            return True
        

        return False