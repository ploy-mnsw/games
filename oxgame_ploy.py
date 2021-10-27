table = ["0", "1", "2",
         "3", "4", "5",
         "6", "7", "8"]

def displaytable():
    print(table[0] + " / " + table[1] + " / " + table[2])
    print("----------")
    print(table[3] + " / " + table[4] + " / " + table[5])
    print("----------")
    print(table[6] + " / " + table[7] + " / " + table[8])
    print("----------")

def playgame():
    player = "x"
    print("Welcome to Tic Tac game")
    for x in range(9):
        displaytable()
        # checkwin()
        if table[0] == table[1] == table[2] or\
            table[3] == table[4] == table[5] or\
            table[6] == table[7] == table[8] or\
            table[0] == table[3] == table[6] or\
            table[1] == table[4] == table[7] or\
            table[2] == table[5] == table[8] or\
            table[0] == table[4] == table[8] or\
            table[6] == table[4] == table[2]:
            if player == "x":
                print("Player o win")
            elif player == "o":
                print("Player x win")
            break
                #insert xo
        while True:
            try:
                print("It's " + player + " turn")
                pos = int(input("Please insert your position"))
                if pos in range(0,9) and table[pos] == str(pos): # "x" == "o"
                    table[pos] = player
                    if player == "x":
                        player = "o"
                    elif player == "o":
                        player = "x"
                    break
                else:print("Your position has already been used")
            except:
                print("You entered wrong key")
    while True:
        playagain = input("Play again?(yes/no): ")
        if playagain == 'yes':
            for x in range(9):
                table[x]=str(x)
            playgame()
        elif playagain == 'no':
            print("Thank you for playing!")
            break

if __name__ == "__main__":
    playgame()

