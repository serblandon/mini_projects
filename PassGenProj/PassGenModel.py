import secrets
import string


def genrndnb():
    collection = string.ascii_letters + string.digits + string.punctuation

    pass_length = secrets.randbelow(21)
    while pass_length < 6:
        pass_length = secrets.randbelow(21)

    password = ""
    i = 0
    while i < pass_length:
        password += secrets.choice(collection)
        i += 1

    return password, pass_length


if __name__ == '__main__':
    print(genrndnb())
