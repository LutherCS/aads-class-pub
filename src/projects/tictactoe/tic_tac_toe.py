#!/usr/bin/env python3
"""
`tic_tac_toe` implementation and driver

Implement Minimax to play Tic Tac Toe

@authors:
@version: 2022.9
"""

import tkinter
import tkinter.messagebox
from turtle import RawTurtle, ScrolledCanvas

SCREEN_MIN = 0
SCREEN_MAX = 300
COMPUTER = 1
HUMAN = -1
PLAYER = {1: "COMPUTER", -1: "HUMAN"}
AI_LEVEL = {"Naive": 0, "Easy": 2, "Normal": 5, "Hard": 6}


class Board:
    """Game board"""

    def __init__(self, board_: "Board" = None, screen_: ScrolledCanvas = None) -> None:
        """
        Board constructor

        When a board is constructed, you may want to make a copy of the board.
        This can be a shallow copy of the board because `Turtle` objects are
        immutable from the perspective of a `board` object.
        """
        if board_:
            self._screen = board_.screen
        else:
            self._screen = screen_

        self.items = []
        for i in range(3):
            row = []
            for j in range(3):
                if not board_:
                    row.append(Dummy())
                else:
                    row.append(board_[i][j])

            self.items.append(row)

    @property
    def screen(self):
        """
        Screen accessor
        """
        return self._screen

    def __getitem__(self, index) -> list:
        """
        Row accessor

        That row itself is indexable (it is just a list)
        so accessing a row and column in the board can be written
        board[row][column] because of this method.

        :param index: row of the board to get
        :return: a specific row
        """
        return self.items[index]

    def __eq__(self, other) -> bool:
        """
        Compare two boards

        :param other: another Board
        :return: `True` if two boards represent the same state, `False` otherwise
        """
        # TODO: Implement this function
        ...

    def __hash__(self) -> int:
        """
        Calculate hash value of a board

        :return: integer hash value
        """
        result = 0
        for i in range(3):
            for j in range(3):
                result += (i + j) * self.items[i][j].eval()
        return result

    def reset(self) -> None:
        """
        Reset the board state

        This method will mutate this board to contain all `Dummy` turtles.
        This way the board can be reset when a new game is selected.
        It should NOT be used except when starting a new game.
        """
        for i in range(3):
            for j in range(3):
                self.items[i][j].goto(-100, -100)
                self.items[i][j] = Dummy()
        self.screen.tracer(0)

    def eval(self) -> int:
        """
        Evaluate the board

        :return: an integer representing the state of the board
        If the computer has won, return 1.
        If the human has won, return -1.
        Otherwise, return 0.
        """
        # TODO: Implement this function
        ...

    def full(self) -> bool:
        """
        Check if the board is full

        :return: `True` if the board is completely filled up (no `Dummy` turtles).
        Otherwise, it should return `False`.
        """
        # TODO: Implement this function
        ...

    def draw_marks(self) -> None:
        """
        Draw `X`s and `O`s on the screen
        """
        for row in range(3):
            for col in range(3):
                if self[row][col].eval() != 0:
                    self[row][col].showturtle()
                    self[row][col].goto(col * 100 + 50, row * 100 + 50)

        self.screen.update()

    def available(self) -> list[tuple[int, int]]:
        """
        Return available (empty) cells

        :return: a list of tuples where each tuple is a (row, column) pair
        """
        # TODO: Implement this function
        ...

    def clone(self) -> "Board":
        """
        Return a copy of the board
        
        :return: a copy of this board
        """
        return Board(self)


class Dummy:
    """
    This class is just for placeholder objects when no move has been made
    yet at a position in the board.
    Having eval() return 0 is convenient when no move has been made.
    """

    def __init__(self):
        """Placeholder"""

    def eval(self) -> int:
        """Evaluate to 0"""
        return 0

    def goto(self, x, y):
        """Placeholder"""


class MarkX(RawTurtle):
    """Class for the X mark"""

    def __init__(self, canvas):
        """
        The constructor begins by initializing the
        RawTurtle part of the object with the call to super().__init__(canvas).
        The super() call returns the class of the superclass
        (the class above the X or O in the class hierarchy).
        In this case, the superclass is RawTurtle.
        Calling __init__ on the superclass initializes the part of the object that is a RawTurtle.
        """
        super().__init__(canvas)
        self.hideturtle()
        self.getscreen().register_shape(
            "X",
            (
                (-40, -36),
                (-40, -44),
                (0, -4),
                (40, -44),
                (40, -36),
                (4, 0),
                (40, 36),
                (40, 44),
                (0, 4),
                (-40, 44),
                (-40, 36),
                (-4, 0),
                (-40, -36),
            ),
        )
        self.pencolor("blue")
        self.shape("X")
        self.penup()
        self.speed(5)
        self.goto(-100, -100)

    def eval(self):
        """Evaluate the mark"""
        return COMPUTER


class MarkO(RawTurtle):
    """Class for the O mark"""

    def __init__(self, canvas):
        """
        The constructor begins by initializing the
        RawTurtle part of the object with the call to super().__init__(canvas).
        The super() call returns the class of the superclass
        (the class above the X or O in the class hierarchy).
        In this case, the superclass is RawTurtle.
        Calling __init__ on the superclass initializes the part of the object that is a RawTurtle.
        """
        super().__init__(canvas)
        self.hideturtle()
        self.shapesize(5, 5, 10)
        self.fillcolor("white")
        self.pencolor("red")
        self.shape("circle")
        self.penup()
        self.speed(5)
        self.goto(-100, -100)

    def eval(self):
        """Evaluate the mark"""
        return HUMAN


def minimax(player, board: Board, depth: int = 5) -> int:
    """
    The minimax function is given a player (1 = Computer, -1 = Human) and a board object.
    When the player = Computer, minimax returns the maximum value of all possible moves that the Computer could make.
    When the player = Human then minimax returns the minimum value of all possible moves the Human could make.
    Minimax works by assuming that at each move the Computer will pick its best move and the Human will pick its best move.
    It does this by making a move for the player whose turn it is, and then recursively calling minimax.
    The base case results when, given the state of the board, someone has won or the board is full.
    """
    # TODO: Implement this function
    ...


class TicTacToe(tkinter.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.pack()
        self.paused = False
        self.stop = False
        self.running = False
        self.turn = HUMAN
        self.level = "Normal"
        self.locked = False
        self.buildWindow()

    def buildWindow(self):

        canvas = ScrolledCanvas(self, 600, 600, 600, 600)
        canvas.pack(side=tkinter.LEFT)
        t = RawTurtle(canvas)
        screen = t.getscreen()
        screen.tracer(100000)

        screen.setworldcoordinates(SCREEN_MIN, SCREEN_MIN, SCREEN_MAX, SCREEN_MAX)
        screen.bgcolor("white")
        t.hideturtle()

        frame = tkinter.Frame(self)
        frame.pack(side=tkinter.RIGHT, fill=tkinter.BOTH)
        board = Board(None, screen)

        def drawGrid():
            screen.clear()
            screen.tracer(1000000)
            screen.setworldcoordinates(SCREEN_MIN, SCREEN_MIN, SCREEN_MAX, SCREEN_MAX)
            screen.bgcolor("white")
            screen.tracer(0)
            t = RawTurtle(canvas)
            t.hideturtle()
            t.penup()
            t.width(10)
            t.color("black")
            for i in range(2):
                t.penup()
                t.goto(i * 100 + 100, 10)
                t.pendown()
                t.goto(i * 100 + 100, 290)
                t.penup()
                t.goto(10, i * 100 + 100)
                t.pendown()
                t.goto(290, i * 100 + 100)

            screen.update()

        drawGrid()

        def newGame():
            # drawGrid()
            self.turn = HUMAN
            board.reset()
            self.locked = False
            screen.update()

        def startHandler():
            newGame()

        btn_Start = tkinter.Button(frame, text="New Game", command=startHandler)
        btn_Start.pack()

        tkvar = tkinter.StringVar(self)
        tkvar.set(self.level)

        def levelHandler(*args):
            self.level = tkvar.get()

        lbl_Level = tkinter.Label(frame, text="AI level")
        lbl_Level.pack()

        dd_Level = tkinter.OptionMenu(frame, tkvar, command=levelHandler, *AI_LEVEL)
        dd_Level.pack()
        
        status = tkinter.Text(frame, height=20, width=10)
        status.pack()

        def quitHandler():
            self.master.quit()

        btn_Quit = tkinter.Button(frame, text="Quit", command=quitHandler)
        btn_Quit.pack()

        def computerTurn():
            """Call Minimax to find the best move to make

            After writing this code, the `next_move` tuple should contain the next move for the computer.
            For instance, if the best move is in the first row and third column then `next_move` would be (0,2).
            The locked variable prevents another event from being processed while the computer is making up its mind.
            """
            self.locked = True
            next_move = None
            # TODO: Implement the game logic
            ...
            row, col = next_move
            board[row][col] = MarkX(canvas)
            self.locked = False

        def mouseClick(x, y):
            if not self.locked:
                row = int(y // 100)
                col = int(x // 100)

                if board[row][col].eval() == 0:
                    board[row][col] = MarkO(canvas)

                    self.turn = COMPUTER

                    board.draw_marks()

                    if not board.full() and not abs(board.eval()) == 1:
                        computerTurn()

                        self.turn = HUMAN

                        board.draw_marks()
                    else:
                        self.locked = True

                    if board.eval() == 1:
                        tkinter.messagebox.showwarning(
                            "Game Over", "Expectedly, Machine wins."
                        )
                    elif board.eval() == -1:
                        tkinter.messagebox.showerror(
                            "Game Over", "Surprisingly, Human wins."
                        )
                    elif board.full():
                        tkinter.messagebox.showinfo("Game Over", "It was a tie.")

        screen.onclick(mouseClick)

        screen.listen()


def main():
    root = tkinter.Tk()
    root.title("Tic Tac Toe")
    application = TicTacToe(root)
    application.mainloop()


if __name__ == "__main__":
    main()
