import secrets
import string

def function():

    collection = string.digits + string.ascii_letters + string.punctuation

    nb_of_length_choices = [2, 3, 4, 5]
    nb_of_lentgh_final = secrets.choice(nb_of_length_choices)

    ranges = [5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
    array = []
    j = 0
    while j < nb_of_lentgh_final:
        array.append(secrets.choice(ranges))
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