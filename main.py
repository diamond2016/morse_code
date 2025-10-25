import fileinput
import re
import json
# una pausa breve tra i punti e le linee che compongono una lettera, 
# una pausa più lunga tra le lettere e una pausa ancora più lunga tra le parole. 
# noi usiamo uno spazio per spazio tra lettere e quattro per spazio tra parole

MORSE_DICT_FILE = "morse.json"
MORSE_BRIEF_PAUSE = " "
MORSE_LONG_PAUSE = "    "

morse_dict = {}
lines_to_encode = []
lines_encoded = []

with open(MORSE_DICT_FILE, 'r') as f:
    morse_dict = json.load(f)

# letter -> morse
def encode_word(word):
    encoded_word=""
    for c in word:
        cu = c.upper()
        if cu in morse_dict:
            encoded_word = encoded_word + MORSE_BRIEF_PAUSE + morse_dict[cu]
    return encoded_word

def encode(line):
    encoded_line=""
    for w in line.split(' '):
        encoded_line = encoded_line + encode_word(w) + MORSE_LONG_PAUSE
    return encoded_line

def decode_char(value_to_find):
    for key, value in morse_dict.items():
        if value == value_to_find:
            return key
    return None

# morse -> letter
def decode_word(word):
    decoded_word=""
    for m in word.split(MORSE_BRIEF_PAUSE):
        if decode_char(m):
                decoded_word = decoded_word + str(decode_char(m))
    return decoded_word

def decode(line):
    decoded_line=""
    for w in line.split(MORSE_LONG_PAUSE):
        decoded_line = decoded_line + decode_word(w) + " "
    return decoded_line

print("Morse encoder, input lines to encode, terminate with <ctrl>D")
for line in fileinput.input():
    encoded_line = ""
    line_to_encode = re.sub(' +', ' ', line.strip()) #remove newline, remove multiple spaces
    lines_encoded.append(encode(line_to_encode))

print("MORSE")
for line in lines_encoded:
    print(line)
    
print("DECODED TEXT")
for line in lines_encoded:
   print(decode(line))
