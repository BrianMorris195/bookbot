def get_num_words(file_contents):
    text = file_contents.split()
    return len(text)



def get_num_char(text):
    char = {
    'a': 0,
    'b': 0,
    'c': 0,
    'd': 0,
    'e': 0,
    'f': 0,
    'g': 0,
    'h': 0,
    'i': 0,
    'j': 0,
    'k': 0,
    'l': 0,
    'm': 0,
    'n': 0,
    'o': 0,
    'p': 0,
    'q': 0,
    'r': 0,
    's': 0,
    't': 0,
    'u': 0,
    'v': 0,
    'w': 0,
    'x': 0,
    'y': 0,
    'z': 0,}
    lowered_text = text.lower()
    for letter in lowered_text:
        if letter == "a":
            char["a"] += 1 
        
        if letter == "b":
            char['b'] += 1

        if letter == "c":
            char['c'] += 1

        if letter == "d":
            char['d'] += 1

        if letter == "e":
            char['e'] += 1

        if letter == "f":
            char['f'] += 1

        if letter == "g":
            char['g'] += 1

        if letter == "h":
            char['h'] += 1

        if letter == "i":
            char['i'] += 1
        
        if letter == "j":
            char['j'] += 1

        if letter == "k":
            char['k'] += 1

        if letter == "l":
            char['l'] += 1

        if letter == "m":
            char['m'] += 1

        if letter == "n":
            char['n'] += 1
        
        if letter == "o":
            char['o'] += 1
        
        if letter == "p":
            char['p'] += 1

        if letter == "q":
            char['q'] += 1

        if letter == "r":
            char['r'] += 1

        if letter == "s":
            char['s'] += 1

        if letter == "t":
            char['t'] += 1

        if letter == "u":
            char['u'] += 1

        if letter == "v":
            char['v'] += 1

        if letter == "w":
            char['w'] += 1

        if letter == "x":
            char['x'] += 1

        if letter == "y":
            char['y'] += 1

        if letter == "z":
            char['z'] += 1
    return char

def char_count_list(char_dict):
    report_counts = []
    for letter in char_dict:
        counts = char_dict[letter]
        count_dictionary = {}
        count_dictionary["char"] = letter
        count_dictionary["num"] = counts
        report_counts.append(count_dictionary)
    return report_counts