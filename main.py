from modules.interpreter import handle_input
from modules.utils import get_time


class Assistant:

    def __init__(self):

        # modules/utils/get_time -> returns the actual time, already condensed
        print(get_time())

        # the whole program operation
        self.start_loop()

    # get_input will only take the user's input
    # it doesn't handle it
    def get_input(self):

        # takes the raw user input
        user_input = input('$ ')

        # all the commands, with parameters, and etc ...
        commands = user_input.split(' ')

        # the main command, for identification purpouses
        command = commands[0]

        # returns a tuple
        return (command, commands)

    def start_loop(self):

        while (True):
            main_command, commands = self.get_input()
            response = handle_input(main_command, commands)

            if (response == False):
                break


if __name__ == '__main__':
    Assistant()
