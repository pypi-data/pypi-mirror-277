from pyxo.views import View


class PlayAgain(View):


    def print(self) -> str:
        return input("\n\ndo you want to play again (yes,no)")

