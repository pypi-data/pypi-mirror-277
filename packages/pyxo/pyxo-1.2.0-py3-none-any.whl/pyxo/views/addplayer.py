from pyxo.views import View
from pyxo.utils import clear

class AddPlayer(View):
    

    def __init__(self,controler:"Engin") -> None:
        
        self.controler :"Engin" = controler

    
    def print(self) -> None:

        clear()
        name_first_player :str = str(input("     the name of the player - 1 - :\t"))
        choise :str = input("      chose {X} or {O}  :\t ")
        self.controler.add_player(name_first_player,choise)
        name_second_player :str = str(input("     the name of the player - 2 - :\t"))
        self.controler.add_player(name_second_player)

