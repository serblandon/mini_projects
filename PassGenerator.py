import secrets
import string
import random

def function():

    collection = string.digits + string.ascii_letters + string.punctuation

    nb_of_length_choices = random.randrange(2, 5)

    array = []
    j = 0
    while j < nb_of_length_choices:
        array.append(random.randrange(5, 20))
        j += 1

    length = int(secrets.choice(array))

    dict_index = ['1', '2', '3', '4']

    password = ""

    i = 0
    while i < length:
        nb = secrets.choice(dict_index)
        password += str(secrets.choice(collection))
        i += 1

    print(length)
    return password


if __name__ == '__main__':
    print(function())