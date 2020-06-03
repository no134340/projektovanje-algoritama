from tree import Node, Tree
from math import log2, floor

char_keys = {'5': 0, 'H': 1, '4': 2, 'S': 3, 'V': 5, '3': 6, 'I': 7, 'F': 9, 'U': 11, '2': 14, 'E': 15, 'L': 17,
             'R': 19, '+': 20, 'A': 23, 'P': 25, 'W': 27, 'J': 29, '1': 30, '6': 32, 'B': 33, '=': 34, 'D': 35, '/': 36,
             'X': 37, 'N': 39, 'C': 41, 'K': 43, 'Y': 45, 'T': 47, '7': 48, 'Z': 49, 'G': 51, 'Q': 53, 'M': 55, '8': 56,
             'O': 59, '9': 60, '0': 62}

dodatni = {'5': 1, 'H': 3, '4': 5, 'S': 7, 'V': 11, 'Ŝ': 9, '3': 13, 'I': 15, 'U': 23, 'F': 19, 'É': 17, 'Ü': 27,
           '2': 29, 'Đ': 25, '?': 24, '_': 26, 'E': 31, 'A': 47, 'R': 39, 'L': 35, 'È': 37, '"': 37, 'Ä': 43, '+': 41,
           '.': 42, 'W': 55, 'P': 51, 'þ': 49, '@': 52, 'À': 53, 'J': 59, '1': 61, "'": 60, 'Ĵ': 57, 'T': 95, 'N': 79,
           'D': 71, 'B': 67, '6': 65, '=': 69, '-': 66, 'X': 75, 'K': 87, 'C': 83, 'Y': 91, 'Ç': 81, ';': 85, '!': 87,
           'Ĥ': 89, '(': 88, ')': 90, 'M': 111, 'G': 103, 'Z': 99, 'Q': 107, '7': 97, ',': 102, 'Ĝ': 105, 'Ñ': 109,
           'O': 119,
           'Ö': 115, 'CH': 123, '9': 121, '0': 125, ':': 112, '/': 73, '8': 113}

dot_code = ".-.-.-"


def inorder_tree_walk(tree):
    print("Inorder tree walk:")
    for x in tree.inorder():
        print(x)


def build_tree(tree, tree_size, chars):
    elements = [Node(i, None) for i in range(tree_size)]
    for k, v in chars.items():
        elements[v].data = k
    if chars == dodatni:
        elements[101].data = '*'
        elements[86].data = '*'
    else:
        elements[13].data = '*'
        elements[21].data = '*'
        elements[57].data = '*'
        elements[61].data = '*'

    mid = len(elements) // 2
    tree.insert(elements[mid])
    final_offset = len(elements) // 2
    offset = tree_size // 4 + 1
    h = floor(log2(offset))
    while offset <= final_offset:
        step = offset
        while step > 0:
            tree.insert(elements[mid - step])
            tree.insert(elements[mid + step])
            step -= 2 ** (h + 1)
        h -= 1
        offset += ((tree_size + 1) // 2 - offset) // 2
        if h == -1:
            break


def search_tree(tree, char, chars):
    key = None
    if char in chars.keys():
        key = chars[char]
    elif char == " ":
        return "/"
    elif char == ".":
        return dot_code
    else:
        return None
    return tree.encode(key)


def find_character(tree, seq):
    if seq == dot_code:
        return "."
    elif seq == "/":
        return " "
    else:
        return tree.decode(seq)


def encode(tree, text, chars):
    ret = ""
    i = 0
    while i < len(text):
        char = text[i]
        if char == '*':
            print(f"Invalid character: {char}")
            return ""
        if char == "C" and chars == dodatni:
            if i < len(text) - 1:
                if text[i + 1] == "H":
                    char = "CH"
                    i += 1
        encoded = search_tree(tree, char, chars)
        if encoded:
            ret += encoded + " "
        else:
            print(f"Invalid character: {char}")
            return ""
        i += 1
    return ret.rstrip()


def decode(tree, code):
    ret = ""
    seqs = code.split(" ")
    for seq in seqs:
        char = find_character(tree, seq)
        if char:
            ret += char
        else:
            print(f"Invalid morse code: {seq}")
            return ""
    return ret


if __name__ == '__main__':
    """
        Potrebno je:
        1. Inicijalizovati stablo
        2. Pozvati build_tree sa parametrima:
           stablo, veličina (63 za redovan, 127 za dodatni zadatak), rečnik sa ključevima za svaki karakter
           (char_keys za redovan, dodatni za dodatni zadatak)
        Ukoliko se enkoduje/dekoduje samo jedan znak/sekvenca dovoljno je pozvati search_tree/find_character
        uz parametre:
         - stablo, znak, rečnik (koji je korišćen za pravljenje stabla) za search_tree
         - stablo, sekvenca za find_character
        Ukoliko se enkoduje/dekoduje niz karaktera/kodovanih karaktera potrebno je pozvati encode/decode uz parametre:
         - stablo, niz karaktera, rečnik (koji je korišćen za pravljenje stabla) za encode
         - stablo, niz kodovanih karaktera
    """
    tree = Tree()

    build_tree(tree, 63, char_keys)

    inorder_tree_walk(tree)

    text = "JA SAM STUDENT. CH 9 +"
    print(f"Coding: {text}")
    coded = encode(tree, text, char_keys)
    print(f"Coded: {coded}")
    print()

    print(f"Decoding: {coded}")
    decoded = decode(tree, coded)
    print(f"Deoded: {decoded}")
    print()

    text = "?a"
    print(f"Coding: {text}")
    coded = encode(tree, text, char_keys)
    print()

    code = ".-.-.-.-----"
    print(f"Decoding: {code}")
    decoded = decode(tree, code)
    print()

    ########################################

    text = "JA SAM STUDENT. CH (Ĥ),!?"

    tree1 = Tree()
    build_tree(tree1, 127, dodatni)
    inorder_tree_walk(tree1)

    coded1 = encode(tree1, text, dodatni)
    print(coded1)
    decoded1 = decode(tree1, coded1)
    print(decoded1)

    text = "?,"
    print(f"Coding: {text}")
    coded = encode(tree1, text, dodatni)
    print()

    # u slučaju dodatnog zadatka:
    #  - promenila sam da se '(' i ')' koduju različitim kodovima (umesto istim,
    #    kako je na stablu u pdf-u), tj. '(' sam pomerila da bude levo dete 'Ĥ'
    #  - stablo je napravljeno na isti način kao za redovan zadatak, prolazila sam
    #    kroz stablo sa pdf-a inorder redom i tim redom u rastućem redosledu dodeljivala ključeve
