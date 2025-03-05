
acronym = input('Kindly input acronym you want to add:\n')
definition = input('Kindly specify the definition for this acronym:\n')

with open("myinput.txt", 'a') as file:
    file.write(acronym + ' - ' + definition + '\n')

    