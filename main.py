from modules.interpreter import handle_input
from modules.utils import get_time


class Assistant:

    def __init__(self):

        # modules/utils/get_time -> returns the actual time, already formated
        time = get_time()
        print(time)

        # the whole program operation
        self.main_loop()

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

    def main_loop(self):

        # the program will run, until the user exit it
        while (True):
            # get_input retuns a tuple
            main_command, commands = self.get_input()

            # which then returns a response, already formated
            response = handle_input(main_command, commands)

            # the response retuns False, if an exception is raised, or if the program ends
            if (response == False):
                break


if __name__ == '__main__':
    Assistant()
