import random
# this is a simple tic-tac-toe game asd asd
# ----------------- GLOBAL VARIABLES ----------------- 

# liste that is the map of tic-tac-toe
liste = [
    ["-","-","-"],
    ["-","-","-"],
    ["-","-","-"],
]

# empty areas on map
playable = []

win_check = False

# print map
def maps(liste):
    map = """
      | 0 | 1 | 2 | 
    --+---+---+---+
    0 | {} | {} | {} 
    --+---+---+---+
    1 | {} | {} | {} 
    --+---+---+---+
    2 | {} | {} | {} 
    """.format(liste[0][0],liste[0][1],liste[0][2],liste[1][0],liste[1][1],liste[1][2],liste[2][0],liste[2][1],liste[2][2])
    return map


# player movement 
def playerMove(liste):
    print("Player's turn.")
    row = int(input("Row: "))
    column = int(input("Column: "))
    if(liste[row][column] == "-"):
        liste[row][column] = "X"
    else:
        print("Player can't move here.")
        print("Try again.")
        playerMove(liste)
    print(maps(liste))


# computer movement
def computerMove(liste,playable):
    playable = []
    for i in range(3):
        for j in range(3):
            if(liste[i][j] == "-"):
                playable.append([i,j])
    cp = int(random.random()*(len(playable))) #sayı
    oPut = playable[cp]
    row = oPut[0]
    column = oPut[1] 
    liste[row][column] = "O"

    print("Computer moved")
    print(maps(liste))


# function to check if there is any win situation
def winCheck(liste):
    # check row 
    for row in range(3):
        if(liste[row][0] == liste[row][1] and liste[row][0] == liste[row][2] and liste[row][0] != "-"):
            return True

    # check column 
    for column in range(3):
        if(liste[0][column] == liste[1][column] and liste[0][column] == liste[2][column] and liste[0][column] != "-"):
            return True

    # check diagonally
    if(liste[0][0] == liste[1][1] and liste[0][0] == liste[2][2] and liste[1][1] != "-"):
        return True
    if(liste[0][2] == liste[1][1] and liste[0][2] == liste[2][0] and liste[1][1] != "-"):
        return True

    # there is no win..
    else:
        return False


def game():
    print("""Player is "X".""")
    print(maps(liste))
    while(winCheck(liste) == False):
        playerMove(liste)
        print("-------------------------------")
        if(winCheck(liste) == True):
            print("Player won.")
            break
        computerMove(liste,playable)
        print("-------------------------------")
        if(winCheck(liste) == True):
            print("Computer won.")
            break


def main():
    # 1 - Read Tic-Tac-Toe Rules
    # 2 - Play Tic-Tac-Toe
    print("Welcome to Tic-Tac-Toe Game! ")
    print("Choose one:")
    print("""
    1 - Read Tic-Tac-Toe Rules
    2 - Play Tic-Tac-Toe
    """)

    choice = int(input())

    while(choice != 1 and choice != 2):
        print("enter 1 or 2")
        choice = int(input())

    if(choice == 1):
        print("this is a game.")
        choice2 = input("wanna play? (y/n)")
        if(choice2 == "y" or choice2 == "Y"):
            game()
        else: 
            print("your loss..")
            return False


    elif(choice == 2):
        game()
        
    
main()



# UPDATES -->
# 06.03.21
    # simple win mechanic is implemented.
    # menu added
    # need to be improved: 
        # game explanation is.. a bit short.
        # computer is silly af 
        # draw option is not recognized yet.



# CREDITS: CAGLA & COSKUN 