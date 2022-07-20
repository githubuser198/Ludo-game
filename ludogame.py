import random

print("1.Start Game")
print("2.Exit")
choice=int(input("Enter your choice :"))

# this function for random numbers
def roll():
    return random.randint(1,6)


if choice==1:
    # taking input by user for playing game
    print("1. 1 vs 1 Multiplayer")
    print("2. 1 vs 2 Multiplayer")
    print("3. 1 vs 3 Multiplayer")
    pc=int(input("Select your choice.. "))
    # this is for 1 vs 1 multiplayer game
    if pc==1:
        score=10
        player1=0
        player2=0
        while True:
            nop=2
            for player in range(1,nop+1):
                print(f"Player {player} turn,would you like to roll")
                print("_____________________________________________")
                pc1=int(input("for roll press 1,for exit 0 "))
                if pc1==1:
                    dice=roll()
                    if player==1:
                        player1=player1+dice
                        print(f"you got {dice},score={player1}")
                        print("___________________________________")
                    if player==2:
                        player2=player2+dice
                        print(f"you got {dice}, score={player2}")
                        print("___________________________________")
                    if player1>=score or player2>=score:
                        break
                elif pc1==0:
                    break
                else:
                    print("Invalid choice..try again!")
            if player1 >= score:
                print("Player1 won...")
                break
            if player2 >= score:
                print("Player2 won...")
                break
# this is for 3 players
    elif pc==2:
        score = 20
        player1 = 0
        player2 = 0
        player3 = 0
        while True:
            nop = 3
            for player in range(1, nop + 1):
                print(f"Player {player} turn,would you like to roll")
                print("_____________________________________________")
                pc1 = int(input("for roll press 1,for exit 0 "))
                if pc1 == 1:
                    dice = roll()
                    if player == 1:
                        player1 = player1 + dice
                        print(f"you got {dice},score={player1}")
                        print("___________________________________")
                    if player == 2:
                        player2 = player2 + dice
                        print(f"you got {dice}, score={player2}")
                        print("___________________________________")
                    if player == 3:
                        player3 = player3 + dice
                        print(f"you got {dice}, score={player3}")
                        print("___________________________________")
                    if player1 >= score or player2 >= score or player3 >= score:
                        break
                elif pc1 == 0:
                    break
                else:
                    print("Invalid choice..try again!")
            if player1 >= score:
                print("Player1 won...")
                break
            if player2 >= score:
                print("Player2 won...")
                break
            if player3 >= score:
                print("Player3 won...")
                break
# this is for 4 players
    elif pc==3:
        score = 30
        player1 = 0
        player2 = 0
        player3 = 0
        player4 = 0
        while True:
            nop = 4
            for player in range(1, nop + 1):
                print(f"Player {player} turn,would you like to roll")
                print("_____________________________________________")
                pc1 = int(input("for roll press 1,for exit 0 "))
                if pc1 == 1:
                    dice = roll()
                    if player == 1:
                        player1 = player1 + dice
                        print(f"you got {dice},score={player1}")
                        print("___________________________________")
                    if player == 2:
                        player2 = player2 + dice
                        print(f"you got {dice}, score={player2}")
                        print("___________________________________")
                    if player == 3:
                        player3 = player3 + dice
                        print(f"you got {dice}, score={player3}")
                        print("___________________________________")
                    if player == 4:
                        player4 = player4 + dice
                        print(f"you got {dice}, score={player4}")
                        print("___________________________________")
                    if player1 >= score or player2 >= score or player3 >= score or player4 >= score:
                        break
                elif pc1 == 0:
                    break
                else:
                    print("Invalid choice..try again!")
            if player1 >= score:
                print("Player1 won...")
                break
            if player2 >= score:
                print("Player2 won...")
                break
            if player3 >= score:
                print("Player3 won...")
                break
            if player4 >= score:
                print("Player1 won...")
                break
    else:
        print("Invalid choice..try again")

elif choice==2:
    exit()
else:
    print("Invalid choice....Please try again!")
