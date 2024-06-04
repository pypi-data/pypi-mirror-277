from pyxo.utils import clear
from pyxo.views import View

class Start(View):

    """this class represent this view of the strat of the game 
    that show the rule of the game of the XO like this :


                    {welcome to the game [X,O] }
    that is the roles you should chose one the nomber between {1...9}
                        
                        _|___|___|___|_         
                         | 1 | 2 | 3 |         
                        _|___|___|___|_         
                         | 4 | 5 | 6 |         
                        _|___|___|___|_         
                         | 7 | 8 | 9 |         
                        _|___|___|___|_
                         |   |   |   |

        shel we start who will begin first you or your friend !

    """
    
    def print(self) -> None:
        
        clear()

        print("""
                    {welcome to the game [X,O] }
    that is the roles you should chose one the nomber between {1...9}
                        
                        _|___|___|___|_         
                         | 1 | 2 | 3 |         
                        _|___|___|___|_         
                         | 4 | 5 | 6 |         
                        _|___|___|___|_         
                         | 7 | 8 | 9 |         
                        _|___|___|___|_
                         |   |   |   |

        shel we start who will begin first you or your friend !
      """)
        _ = input(" press ENTER to begin ..")

