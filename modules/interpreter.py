from os import system as terminal_command

from modules.utils import sanitize_data, web_module, math_module, get_time
from modules.database import Database
from googletrans import Translator


def handle_input(main_command='exit', commands=[]):

    if (main_command == 'exit'):
        return False

    elif (main_command == ''):
        # user only pressed enter, ... avoiding slowness
        pass

    # -> echo hello world
    elif (main_command == 'echo'):
        # modules/utils/sanitize_data -> return's formated data
        print(sanitize_data(commands, ' '))

    # -> cl
    elif (main_command == 'cl'):
        terminal_command('clear')

    # -> math 10 - 9
    elif (main_command == 'math'):

        if (len(commands) >= 4):

            number1 = commands[1]
            number2 = commands[3]
            operation = commands[2]

            result = math_module(number1, number2, operation)

            # math_module return False, if unable to perform the operation
            # but python also considers 0 as false
            if (type(result) == float):
                print(f'{number1} {operation} {number2} = {result}')
            else:
                print('Incorrect use!')
        else:
            print('Incorrect use')

    # -> search Horses runnig free
    elif (main_command == 'search'):

        # modules/utils/web_module return a string with the full URL
        url = web_module(commands, 'Google')
        terminal_command('brave-browser ' + url)

    elif (main_command == 'wikipedia'):
        url = web_module(commands, 'Wikipedia')
        terminal_command('brave-browser ' + url)

    # -> translate Hola! Como estas ?
    elif (main_command == 'translate'):

        to_translate = sanitize_data(commands, ' ')

        # google translate library
        translated = Translator().translate(to_translate, dest='en').text

        print(translated)

    # modules/database ->
    elif (main_command == 'database'):

        # initializes the class, with the name of the database as a parameter
        database = Database('database.txt')
        # possible to have multiple databases

        # commands[0] == 'database'
        # commands[1] == 'read/add/delete'
        main_database_command = commands[1]

        if (main_database_command == 'read'):
            # database.read returns all the lines from the database
            lines = database.read()

            for i in range(len(lines)):
                print(f'Index {i}: {lines[i]}', end='')

        elif (main_database_command == 'add'):
            to_add = sanitize_data(commands[1:], ' ')

            # avoiding bad usage
            if (to_add == ''):
                print('Unable to add')
                pass
            else:
                database.write(to_add)

        elif (main_database_command == 'remove'):
            if (len(commands) > 2):
                # database.delete needs the index of the item to remove
                index = int(commands[2])

                database.delete(index)
            else:
                print('Unable to remove')
                pass

        elif (main_database_command == 'update'):
            to_add = ''

            for i in range(len(commands)):
                if (i > 2):
                    to_add += commands[i]

                    if (i < len(commands) - 1):
                        to_add += ' '

            if (to_add == ''):
                print('Unable to add')
                pass
            else:
                index = int(commands[2])
                database.update(index, to_add)

        else:
            print('Not a command!')

    return
