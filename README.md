## Text to Morse Code Converter

# Design
The morse code is contained in a list of JSON data, { code, value }. Codes are letters, numbers, special characters, special codes (like 'KA')
We will store data in an csv file to load initially in dictionary.

def encode(line): encodes line in morse code
def decode(line): decodes line from morse code

All text is conveted in upper case, multiple spaces are reduced to oune. 
The "brief pause" in morse is one char, the long pause between words is four chars (tab in spaces)
