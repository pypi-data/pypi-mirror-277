from abc import ABC,abstractmethod


class View(ABC):
    
    @abstractmethod
    def print(self) -> None:
        pass


from pyxo.views.start import *
from pyxo.views.addplayer import *
from pyxo.views.playing import *
from pyxo.views.showiner import *
from pyxo.views.playagain import *
