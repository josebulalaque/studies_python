
import random

def rolldice():
    dicetotal = random.randint(1, 6) + random.randint(1, 6)
    return dicetotal

def main():
    playername = input("Enter your name: ")

    roll1 = rolldice()
    roll2 = rolldice()

    print(playername, 'rolled', roll1)
    print('Computer rolled', roll2)

    if roll1 > roll2:
        print(playername, 'Wins')
    elif roll1 < roll2:
        print('Computer Wins')
    else:
        print('Its a TIE!')

main()