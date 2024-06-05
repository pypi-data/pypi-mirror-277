from pyxo.views import View 
from pyxo.utils import clear

class ShoWiner(View):

    def __init__(self,controler:"Engin") -> None:
        self.controler:"Engin" = controler

    def print(self) -> None:
        clear()
        print(f"\n\n the winer is 🏆 {self.controler.winer} 🏆")

    def print_no_winer(self) -> None:
        print("\n\n   draw no winer 🫠")

