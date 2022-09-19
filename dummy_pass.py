import secrets
import string
import random

def function():

    charac_type = {
        "1": string.ascii_lowercase,
        "2": string.ascii_uppercase,
        "3": string.digits,
        "4": string.punctuation
    }

    nb_of_length_choices = random.randrange(2,5)

    array = []
    j = 0
    while j < nb_of_length_choices:
        array.append(random.randrange(5,20))
        j += 1

    length = int(secrets.choice(array))

    dict_index = ['1', '2', '3', '4']

    password = ""

    i = 0
    while i < length:
        nb = secrets.choice(dict_index)
        password += str(secrets.choice(charac_type.get(nb)))
        i += 1

    print(length)

    return password


if __name__ == "__main__":
    print(function())