from os import system as terminal_command

from modules.utils import sanitize_data, get_time, math_module, web_module

from googletrans import Translator

# import asyncio
# import pyppeteer


class Assistant:

    def __init__(self):

        # modules/utils/get_time -> returns the actual time, already condensed
        print(get_time())

        self.get_input()

    # get_input will only take the user's input
    # it doesn't handle it
    def get_input(self):

        # takes the raw user input
        user_input = input('$ ')

        # all the commands, with parameters, and etc ...
        commands = user_input.split(' ')

        # the main command, for identification purpouses
        command = commands[0]

        # handling the input
        self.handle_input(command, commands)

    def handle_input(self, main_command, commands):

        if (main_command == 'exit'):
            return

        # if the user only presses enter, it doesn't look for all commands, with no necessity
        # avoiding slowness
        elif (main_command == ''):
            pass

        elif (main_command == 'echo'):
            # modules/utils/sanitize_data -> return the final data
            sanitized = sanitize_data(commands, ' ')

            print(sanitized)

        elif (main_command == 'cl'):
            terminal_command('clear')

        elif (main_command == 'math'):

            # math 10 + 21
            # main_command = math
            # number1 = 10
            # number2 = 21
            # operation = +

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

        elif (main_command == 'search'):

            # modules/utils/web_module return a string with the full URL
            URL = web_module(commands, 'Google')

            # no_output forces the terminal to execute silently
            no_output = "</dev/null >/dev/null 2>&1"

            # executes the terminal with no output
            # with brave being used as the browser
            terminal_command(f'brave-browser {URL} {no_output}')

        elif (main_command == 'wikipedia'):
            URL = web_module(commands, 'Wikipedia')
            no_output = "</dev/null >/dev/null 2>&1"

            terminal_command(f'brave-browser {URL} {no_output}')

        elif (main_command == 'translate'):

            to_translate = sanitize_data(commands, ' ')

            translated = Translator().translate(to_translate, dest='en').text

            print(translated)

        # recursive call, both methods will call each other
        # causing an endless loop, until the user type 'exit'
        self.get_input()


if __name__ == '__main__':
    Assistant()
