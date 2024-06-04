from pyxo.utils import  equals


class Board:

    """the Board is the model responseble of saving 
    the information about the board of the X O game
    and every player move.
    Every board has three rows every row contain three
    case with True for X and False for O.
    """

    def __init__(self) -> None:
       
        """to create an object Board use this following code:
        ```python
        >>> xo_board = Board()
        >>> # to see the rows you need this code
        >>> xo_board.row_1 # or xo_board.row_2
        ```
        """

        self.row_1 :list[bool] = 3*[None]
        self.row_2 :list[bool] = 3*[None]
        self.row_3 :list[bool] = 3*[None]


    def reset(self) -> None:
        
        """After the end of the game of XO
        we need to reset the board to do that we use this
        folowing code :
        ```python
        >>> xo_board = Board()
        >>> xo_board.reset()
        ```
        """

        self.row_1 :list[bool] = 3*[None]
        self.row_2 :list[bool] = 3*[None]
        self.row_3 :list[bool] = 3*[None]

    
    def check_move(self,move :int) -> bool:
        new_move = move % 3
        if move in [1,2,3]: return True if self.row_1[new_move-1] is None else False
        if move in [4,5,6]: return True if self.row_2[new_move-1] is None else False
        if move in [7,8,9]: return True if self.row_3[new_move-1] is None else False
        return False

    def make_move(self,move:int,choise:bool) -> None:
        new_move = move % 3
        if move in [1,2,3]: self.row_1[new_move-1] = choise
        if move in [4,5,6]: self.row_2[new_move-1] = choise
        if move in [7,8,9]:self.row_3[new_move-1] = choise

    def game_ended(self) -> bool:
        return self.count_full() == 8 or self.winer_exist()


    def winer_exist(self) -> bool:
        return self.check_row() or self.check_colum() or self.check_corner()

    def check_row(self) -> bool:
        if equals(self.row_1[0],self.row_1[1],self.row_1[2]) :return True
        if equals(self.row_2[0],self.row_2[1],self.row_2[2]) :return True
        if equals(self.row_3[0],self.row_3[1],self.row_3[2]) :return True
        return False


    def check_colum(self) -> bool:
        
        if equals(self.row_1[0],self.row_2[0],self.row_3[0]) :return True
        if equals(self.row_1[1],self.row_2[1],self.row_3[1]) :return True
        if equals(self.row_1[2],self.row_2[2],self.row_3[2]) :return True
        return False

    def check_corner(self) -> bool:
        
        if equals(self.row_1[0],self.row_2[1],self.row_3[2]) :return True
        if equals(self.row_3[0],self.row_2[1],self.row_1[2]) :return True
        return False

    def count_full(self) -> int:
        count :int = 0
        for i in range(3):
            if self.row_1[i] is not None:
                count += 1
            if self.row_2[i] is not None:
                count += 1
            if self.row_3[i] is not None:
                count += 1
        return count
