import random
import string

def password_generator(length: int):

    lower = string.ascii_lowercase
    upper = string.ascii_uppercase
    num = string.digits
    symbols = string.punctuation

    characters = lower + upper + num + symbols

    character_random_list = random.sample(characters, length)

    password = "".join(character_random_list)

    return password


if __name__ == "__main__":
    password = password_generator(length=16)
    print(password)



