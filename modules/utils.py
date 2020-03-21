from datetime import datetime as date


def get_time():
    return date.now().strftime('%d/%m/%Y  %H:%M:%S')


def sanitize_data(data, replacement):

    # if there's actual data
    if (len(data) >= 1):
        result = ''

        for word in data:

            # removing the first index ( usually the main_command )
            if (word != data[0]):
                result += word

                # only add the replacement until the last word
                # sanitize_data(['hello', 'world], '-') -> hello-word
                # instead of -> hello-world-
                if (word != data[-1]):
                    result += replacement

    return result


def math_module(number1, number2, operation):

    try:
        result = 0

        if (operation == '+'):
            result = float(number1) + float(number2)

        elif (operation == '-'):
            result = float(number1) - float(number2)

        elif (operation == '*'):
            result = float(number1) * float(number2)

        elif (operation == '/'):
            result = float(number1) / float(number2)

        return result

    except:
        return False


def web_module(data, provider):

    if (provider == 'Google'):
        search_term = sanitize_data(data, '%20')

        URL = 'https://www.google.com/search?q='

    elif (provider == 'Wikipedia'):
        search_term = sanitize_data(data, '_')

        URL = 'https://en.wikipedia.org/wiki/'

    # web_module doesn't search anything, it just returns the full url
    return URL + search_term
