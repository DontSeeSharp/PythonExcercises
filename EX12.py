""""Creates heatmap from a text file."""
from PIL import Image, ImageDraw, ImageFont
import re
from math import log


def read_file(file):
    """Read file and return data in a list."""
    with open(file, 'r', encoding="utf-8") as f:
        read_data = f.read()
    read_data = read_data.lower()
    return_data = re.split("[^abcdefghijklmnopqrsšzžtuvwõäöüxy]", read_data)
    return_data = [i for i in return_data if i != '']

    return return_data


def pair_frequency(word_list):
    """Take a list of words and convert it to a dictionary, which keys are Estonian alphabet character pair combinations."""
    word_list = ' '.join(word_list)
    alphabet_list = [
        'a',
        'b',
        'c',
        'd',
        'e',
        'f',
        'g',
        'h',
        'i',
        'j',
        'k',
        'l',
        'm',
        'n',
        'o',
        'p',
        'q',
        'r',
        's',
        'š',
        'z',
        'ž',
        't',
        'u',
        'v',
        'w',
        'õ',
        'ä',
        'ö',
        'ü',
        'x',
        'y']
    pair_dictionary = {}
    for character in alphabet_list:
        for number in range(len(alphabet_list)):
            dict_key = character + alphabet_list[number]
            if dict_key in pair_dictionary:
                pair_dictionary[dict_key] += word_list.count(dict_key)
            else:
                if word_list.count(dict_key) != 0:
                    pair_dictionary[dict_key] = word_list.count(dict_key)
    return pair_dictionary


def create_heatmap(filename, pair_dictionary):
    """Create a heatmap with character pairs from dictionary and save asfilename.

    Args:
    filename - name of the file to be saved
    pair_dictionary - dictionary, which contains alphabet character pairs
    as keys and their count in a text as values

    Returns:
    Nothing, but saves file as filename
    """
    if pair_dictionary is None:
        print("Pair-dictionary is none!")
        return None
    for i in pair_dictionary:
        if pair_dictionary[i] != 0:
            pair_dictionary[i] = log(pair_dictionary[i])
    image = Image.new("RGB", (3400, 4000), color="hsl(0,0%,50%)")
    draw = ImageDraw.Draw(image)
    if len(pair_dictionary) == 0:
        print(len(pair_dictionary))
        max_value = 1
    else:
        max_value = max(pair_dictionary.values())
    if max_value == 0:
        max_value = 1
    font = ImageFont.truetype("arial.ttf", 90)
    alphabet_list = [
        'a',
        'b',
        'c',
        'd',
        'e',
        'f',
        'g',
        'h',
        'i',
        'j',
        'k',
        'l',
        'm',
        'n',
        'o',
        'p',
        'q',
        'r',
        's',
        'š',
        'z',
        'ž',
        't',
        'u',
        'v',
        'w',
        'õ',
        'ä',
        'ö',
        'ü',
        'x',
        'y']

    for char_num in range(len(alphabet_list)):
        for number in range(32):
            if alphabet_list[char_num] + \
                    alphabet_list[number] in pair_dictionary:
                color = pair_dictionary[
                    alphabet_list[char_num] +
                    alphabet_list[number]]
                a = int((color / max_value * 100) // 1)
                draw.rectangle(
                    [(char_num * 100 + 100, number * 100 + 100),
                     (char_num * 100 + 200, number * 100 + 200)],
                    fill="hsl(0,0%," + str(a) + "%)", outline="white")
            else:
                draw.rectangle(
                    [(char_num * 100 + 100, number * 100 + 100),
                     (char_num * 100 + 200, number * 100 + 200)],
                    fill="hsl(0,0%,0%)", outline="white")
    draw_legend(draw, alphabet_list, max_value, font)
    image.save(filename)
    return -1


def draw_legend(draw, alphabet_list, max_value, font):
    """Draw legend for the map.

    Args:
    draw - ImageDraw.draw() object
    alphabet_list list of the alphabet
    max_value - value for the maximum value of the character pair value
    font - pillow ImageFont object
    """
    for i in range(32):
        draw.text((100 * i + 120, 0), alphabet_list[i], fill="black",
                  font=font,
                  anchor=None)
        draw.text((10, 100 * i + 100), alphabet_list[i],
                  fill="black",
                  font=font,
                  anchor=None)
    for number in range(3000):
        percentage = int(((number / 3000) * 100) // 1)
        draw.rectangle([(150 + number, 3400),
                        (150 + number, 3500)],
                       fill="hsl(0,0%," + str(percentage) + "%)", outline=None)
    for i in range(7):
        draw.text(
            (100 + 3000 * (i / 6),
             3550),
            str(round(max_value * (i / 6))),
            fill="black",
            font=font,
            anchor=None)

    draw.text(
        (100, 3700),
        "Number represents occurences of logarithm of character pairs in text.",
        fill="black",
        font=font,
        anchor=None)

if __name__ == '__main__':

    create_heatmap(
        "test2.png",
        pair_frequency(
            read_file("Kolm isamaalist kõnet.txt")))
