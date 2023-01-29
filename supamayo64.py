##--SUPAMAYO64--##
#Author: MysticAxolotl
#Usage: Decodes any base32 or base64 encoded string, with automatic detection between the formats. It

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

# Determines if a text is base32 or base64 encoded
def checkBase(text):
    if text.isupper():
        base = '32'
    else:
        base = '64'
    return base

# Decodes encoded text
def decodeText(text, base):
    if base == '32':
        decoded = base64.b32decode(text).decode()
    elif base == '64':
        decoded = base64.b64decode(text).decode()
    return decoded

# Encodes plain text
def encodeText(text, base):
    if base == '32':
        # Encode the text to Base64
        encoded = base64.b32encode(text.encode())
        
    elif base == '64':
        # Encode the text to Base64
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
        
        # Check for Base32 instead of Base64
        base = checkBase(text)
    
        # Decode the encoded text
        decoded = decodeText(text, base)

        # Print results
        print("Text:", text)
        print("Base" + base + " Encoded:", text)
        print("Base" + base + " Decoded:", decoded)
    
    else:
        base = input("Would you like to encode to base32 or base64 (write the numerical portion only; e.g. type 32 if you want to encode to base32)? ")

        encoded = encodeText(text, base)

        decoded = decodeText(encoded, base)
        
        print("Text:", text)
        print("Base" + base + " Encoded:", encoded)
        print("Base" + base + " Decoded:", decoded)


if __name__ == "__main__":
    main()
