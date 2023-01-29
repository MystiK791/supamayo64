##--SUPAMAYO64 (Competition Version)--##
#Author: MysticAxolotl
#Usage: Decodes any base64 encoded string. This competition version has support for [REDACTED]-encoded strings removed.

import base64

# Gets user input and returns as list
def getUserInput():
    text = input("Enter a string to run this program on: ")

    raw = input("Is this text already encoded [y/n]: ").lower()

    yn = raw[0]

    return [text, yn]

# Checks for python bytearray-formatted string and converts it
def fixPythonFormat(text):
    if text[0] + text[1] == "b'":
        text = ''.join(text.split('b', 1))
        text = text.strip('\'')
    return text

# Decodes encoded text from base64
def decodeText(text):
    decoded = base64.b64decode(text).decode()
    return decoded

# Encodes plain text to base64
def encodeText(text):
    encoded = base64.b64encode(text.encode())
    return encoded

# Main function
def main():
    inputVals = getUserInput()
    text = inputVals[0]
    yn = inputVals[1]
    
    if yn == 'y':

        # Fix strange Python bytearray formatting
        text = fixPythonFormat(text)
    
        # Decode the encoded text
        decoded = decodeText(text)

        # Print results
        print("Text:", text)
        print("Base64 Encoded:", text)
        print("Base64 Decoded:", decoded)
    
    else:

        encoded = encodeText(text)

        decoded = decodeText(encoded)
        
        print("Text:", text)
        print("Base64 Encoded:", encoded)
        print("Base64 Decoded:", decoded)


if __name__ == "__main__":
    main()
