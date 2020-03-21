class Assistant:

    def __init__(self):

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

        if (main_command == 'test'):
            print('hello!')


if __name__ == '__main__':
    Assistant()
