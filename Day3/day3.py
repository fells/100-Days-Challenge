"""


"""



import os

def Borders ():
    print(60 * "*")

def Logo ():
    print("""  
 ___                         _               
|_ _|_  _  _    _     _  _  | |_ ||_    _  ||
 | |/_|/o\/o\|U(c'|U|/_|/o\ | (c'|/o\ |/ \/o|
 |_|L| \( \_,]_|_)\_/L| \(  |_\_)L\_,]L_n|\_|                                             
    """)


def Game ():

    restart_game = False

    Borders()

    Logo()

    Borders()

    print("Welcome to Treasure Island.\nYour mission is to find the treasure")
    choice_1 = input(f"You're at a cross road. Where do you want to go ? Type 'left' or 'Right'\n")

    if (choice_1.lower() == "left"):
        choice_2 = input("You come to a lake. There is a island in the middle of the lake. Type 'wait' fot a boat. Type 'swim' to swim acroos.")
        if (choice_2.lower() == "wait"):
            choice_3 = input("A boat came for you to go to the island, but there are some pirates. Do you wish to go with them ? or fight ?")
            if (choice_3.lower() == "go"):
                print("You won the game and got the gold 🪙")

            else:
                print("The pirates killed you and took you're gold.")
                restart_game_choice = input("GAME OVER. Do you want to play the game again ?")
                if (restart_game_choice.lower() == "y" or restart_game_choice.lower() == "yes"):
                    restart_game = True
                    Game()
                else:
                    os.system('cls')
        else:
            print("A shark eat you.")
            restart_game_choice = input("GAME OVER. Do you want to play the game again ?")
            if (restart_game_choice.lower() == "y" or restart_game_choice.lower() == "yes"):
                restart_game = True
                Game()
            else:
                os.system('cls')
    else:
        print("You ran into a Lion and got you killed.")
        restart_game_choice = input("GAME OVER. Do you want to play the game again ?")
        if (restart_game_choice.lower() == "y" or restart_game_choice.lower() == "yes"):
            restart_game = True
            Game()
        else:
            os.system('cls')


Game()