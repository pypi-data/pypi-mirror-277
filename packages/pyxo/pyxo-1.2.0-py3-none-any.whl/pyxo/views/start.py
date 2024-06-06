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
        from pyxo import __version__
        clear()

        print(f"""
           _____ _        _____            _____          
          |_   _(_) ___  |_   _|_ _  ___  |_   _|__   ___ 
            | | | |/ __|   | |/ _` |/ __|   | |/ _ \ / _ \\
            | | | | (__    | | (_| | (__    | | (_) |  __/
            |_| |_|\___|   |_|\__,_|\___|   |_|\___/ \___|

            by ouhammmourachid                      v{__version__}
          
          
                welcome to the game [X,O]

      that is the roles you should chose one the nomber between (1...9)
                        
                        _|___|___|___|_         
                         | 1 | 2 | 3 |         
                        _|___|___|___|_         
                         | 4 | 5 | 6 |         
                        _|___|___|___|_         
                         | 7 | 8 | 9 |         
                        _|___|___|___|_
                         |   |   |   |

      should we start who will begin first you or your friend !
""")
        _ = input(" press ENTER to begin ..")

