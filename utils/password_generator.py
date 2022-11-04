import random
import string

def password_generator(length: int, complexity=3):

    if length < 0:
        raise ValueError('length must have a positive value only')
    if 0 < complexity > 5:
        raise ValueError('complexity must have a positive value only less than 5')


    def characters_generator(length:int, complexity: int):

        if complexity >= 1:
            yield string.ascii_lowercase  # lower
        if complexity >= 2:
            yield string.ascii_uppercase  # upper
        if complexity >= 3:
            yield string.digits  # numbers
        if complexity == 4:
            yield string.punctuation  # symbols

    characters_list = list(characters_generator(length, complexity))

    characters = "".join(characters_list)

    character_random_list = random.sample(characters, length)

    password = "".join(character_random_list)

    return password


if __name__ == "__main__":
    password = password_generator(length=16)
    print(password)



