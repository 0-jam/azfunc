import random

# All characters on the keyboard as integers
CHARS = list(range(32, 128)) + [8, 9, 10]


def shuffle(orig_list):
    return random.sample(orig_list, k=len(orig_list))


def generate_text(gen_size=100):
    generated_text = ''

    for _ in range(gen_size):
        generated_text += chr(shuffle(CHARS)[0])

    return generated_text
