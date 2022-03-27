from re import L
import sys

script, input_encoding, error = sys.argv

def main(language_file, encoding, errors):
    line = language_file.readline()

    if line:
        print_line(line, encoding, errors)
        #return main(language_file, encoding, errors)

def print_line(line, encoding, errors):
    next_lang = line.strip() #removes the spaces in front and back
    #Raw bytes are parsed by encoding
    raw_byte = next_lang.encode(encoding, errors = errors)
    cooked_string = raw_byte.decode(encoding,errors = errors)

    print(raw_byte, "<=======>", cooked_string)

languages = open("languages.txt", encoding="utf-8")

main(languages, input_encoding, error)