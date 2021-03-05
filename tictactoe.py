import random
liste = [
    ["-","-","-"],
    ["-","-","-"],
    ["-","-","-"],
]
playable = []
"""param = {
    "00" : "-",
    "01" : "-",
    "02" : "-",
    "10" : "-",
    "11" : "-",
    "12" : "-",
    "20" : "-",
    "21" : "-",
    "22" : "-",
}"""
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

print("""Player is "X".""")

##############
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
##############

###########
def computerMove(liste,playable):



for i in range(3):
    for j in range(3):
        if(liste[i][j] == "-"):
            playable.append([i,j])
cp = int(random.random()*(len(playable))) #sayı
oPut = playable[cp]
row = oPut[0]
column = oPut[1] 
liste[row][column] = "O"
###########

## SIRAYLA DÖNME
## WIN CHECK
"""
[a,b]
a%2==0 and b%2==0 ise çaprazlara da bakılır

diğer durumlarda sadece dikey ve yatay

x y x 0   2
y z y   2  
x y x 2   4

"""
#########
def winCheck(liste,row,column):
    if(liste[row][0] == liste[row][1] and liste[row][0] == liste[row][2]):
        return True
    if(liste[0][column] == liste[1][column] and liste[0][column] == liste[2][column]):
        return True
    if((row+column) %2 == 0):
        if(liste[0][0] == liste[1][1] and liste[0][0] == liste[2][2]):
            return True
        if(liste[0][2] == liste[1][1] and liste[0][2] == liste[2][0]):
            return True
    else:
        return False
########
win_check = False

while(winCheck(liste,row,column) == False or len(playable) != 0):

    ### player oynayacak
    playerMove(liste)

    ##wincheck
    if(winCheck(liste,row,column) == True):
        print("Player won.")
        break

    ### pc oynayacak
    

    ###wincheck
    if(winCheck(liste,row,column) == True):
        print("Computer won.")
        break






### CREDITS: CAGLA & COSKUN ###