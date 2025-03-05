def search_acronym():
    print('Searching Acronym')
    lookup = input('Please input the Acronym you want to lookup:\n')

    found = False

    with open("myinput.txt") as file:
        for i in file:
            if lookup in i:
                print(i)
            #v=i.split('-')
            #v=i
            # for x in i:
            #     if lookup in x:
            #         print(x)
            #         found = True

def update_acronym():
    print('Updating Acronym')
    
    acronym = input('Kindly input acronym you want to add:\n')
    definition = input('Kindly specify the definition for this acronym:\n')

    with open("myinput.txt", 'a') as file:
        file.write(acronym + ' - ' + definition + '\n')

def main():
    print('Main Function')
    print('[A] - Search for Acronym')
    print('[B] - Update List of Acronyms')
    print('[X] - Exit')
    choice=input('\nKindly Choose from the options above: ')

    if choice == 'X' or choice == 'x':
        print("You've chosen to exit")
        return
    elif choice == 'A' or choice == 'a':
        print("You've chosen [A]")
        search_acronym()
    elif choice == 'B' or choice == 'b':
        print("You've chosen [B]")
        update_acronym()

main()

