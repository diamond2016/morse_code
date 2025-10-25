## Text to Morse Code Converter

# Use
* encode(line) encodes line in morse code
* decode(line): decodes line from morse code

# Design
The morse code is contained in a dictionary of JSON data, { code, value }. 
All text is conveted in upper case, multiple spaces are reduced to oune. 
The "brief pause" in morse is one char, the long pause between words is four chars (tab in spaces)

Text is read from standard input, line per line. <CTRL><D> to signal end of input.