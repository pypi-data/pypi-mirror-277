

class Player:

    """the player class is a model that hold :
        the name :str of the player. 
        the points :int contain how many time you win.
        the choise :bool contain true if player X other wise it contain flase.
    """

    def __init__(self,name:str) -> None:

        """to create an player you need just a name and the number of point 
        hold by default 0 in the begining of th game.
        ```python
        >>> player = Player('rachid')
        >>> # to change the name
        >>> player.name = 'new name'
        ```
        """

        self.name :str = name
        self.points :int = 0

    def set_choise(self,choise:bool) -> None:
        
        """ this methode allow you to set the choise of the player
        like this:
        ```python
        >>> player = Player('rachid')
        >>> player.set_choise('X')
        >>> player.choise
        True
        ```
        """

        self.choise :bool = choise

    def get_choise(self) -> bool:
        return self.choise


