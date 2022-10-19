import random
import string

def password_generator(length: int, complexity=3):

    def characters_generator(length:int, complexity: int):

        lower = string.ascii_lowercase
        upper = string.ascii_uppercase
        numbers = string.digits
        symbols = string.punctuation

        if complexity == 1:
            return lower
        elif complexity == 2:
            return lower + upper
        elif complexity == 3:
            return lower + upper + numbers
        elif complexity == 4:
            return lower + upper + numbers + symbols

    characters = characters_generator(length, complexity)

    character_random_list = random.sample(characters, length)

    password = "".join(character_random_list)

    return password


if __name__ == "__main__":
    password = password_generator(length=16)
    print(password)



