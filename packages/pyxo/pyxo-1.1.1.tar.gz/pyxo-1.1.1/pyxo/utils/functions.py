import os

def clear() -> None:

    """this function is respenseble of clearing 
    the terminal on linux or the console on 
    windows .
    """

    try:
        os.system("clear")
    except Exception as ex:
        os.system("cls")


def bool_str(boolean:bool) -> str:
    if boolean is None: return " "
    if boolean : return "X"
    if not boolean : return "O"



def show_board(board:"Board",players:list["Player"]) -> None:
    
    row_1 :list[str] = [ bool_str(cas) for cas in board.row_1] 
    row_2 :list[str] = [ bool_str(cas) for cas in board.row_2] 
    row_3 :list[str] = [ bool_str(cas) for cas in board.row_3]
    player_1 = players[0]
    player_2 = players[1]
    more_points = player_1.points - player_2.points

    print(f"""    


            _|___|___|___|_       |       _|___|___|___|_         
             | {row_1[0]} | {row_1[1]} | {row_1[2]} |        |       _| 1 | 2 | 3 |_  {'👑' if more_points > 0 else '  '} {player_1.name} :  {player_1.points}
            _|___|___|___|_       |       _|___|___|___|_   
             | {row_2[0]} | {row_2[1]} | {row_2[2]} |        |       _| 4 | 5 | 6 |_  {'👑' if more_points < 0 else '  '} {player_2.name} :  {player_2.points}
            _|___|___|___|_       |       _|___|___|___|_         
             | {row_3[0]} | {row_3[1]} | {row_3[2]} |        |       _| 7 | 8 | 9 |_
            _|___|___|___|_       |       _|___|___|___|_         


        ____________________________________________________________
        
        """)


def equals(a:bool,b:bool,c:bool) -> bool:
    return (a == b and b == c and a is not None)


