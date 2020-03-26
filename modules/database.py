class Database():

    def __init__(self, database_name):

        self.database_name = database_name

    # passes the 'data' parameter to the database file
    def write(self, data):

        file = open(self.database_name, 'a')

        file.write(data + '\n')

    def read(self):

        file = open(self.database_name, 'r')
        lines = file.readlines()

        return lines

    def delete(self, index):

        file = open(self.database_name, 'r')

        # lines = all the characters in the file, splited by a line breaker
        # without the last line (always an empty line)
        lines = file.read().split('\n')[:-1]
        # file.read returns all the characters, instead of all the lines

        if (index >= len(lines)):
            print('Unable to remove such index')
            return

        data = []

        # passing all the existing data to the array
        # except for the one, on the index we want to remove
        for i in range(len(lines)):
            if (i != index):
                data.append(lines[i])

        # erasing all the data from the database file
        file = open(self.database_name, 'w')

        # passing all the data from the array to the fresh database
        for value in data:
            self.write(value)

    def update(self, index, new_data):

        file = open(self.database_name, 'r')

        # lines = all the characters in the file, splited by a line breaker
        # without the last line (always an empty line)
        lines = file.read().split('\n')[:-1]
        # file.read returns all the characters, instead of all the lines

        if (index >= len(lines)):
            print('Unable to remove such index')
            return

        data = []

        # passing all the existing data to the array
        # except for the one, on the index we want to remove
        for i in range(len(lines)):
            if (i != index):
                data.append(lines[i])
            else:
                data.append(new_data)

        # erasing all the data from the database file
        file = open(self.database_name, 'w')

        # passing all the data from the array to the fresh database
        for value in data:
            self.write(value)


if __name__ == '__main__':
    database = Database('database.txt')

    # database.write('This is index 0')
    # database.write('This is index 1')
    # database.write('This is index 2')
    # database.write('This is index 3')

    # database.read()

    # database.delete(0)
