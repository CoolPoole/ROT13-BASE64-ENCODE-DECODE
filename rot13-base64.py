# Python script to take input to encode/decode with rot13 and base64
# Author: JustCooLpOOLe
# Version: 1.0
# License: (o^o)

# Module Input Section
import codecs
import base64
import pyfiglet
import time

# Global Variable Declaration

again = 'Y'

# Functions 

def rot13_encode():
    new_value = input("\nPlease provide the value encode: ")

    rot13value = codecs.encode(new_value, "ROT13")
    print(rot13value)

def rot13_decode():
    new_value = input("\nPlease provide the ROT13 value: ")

    rot13value = codecs.decode(new_value, "ROT13")
    print(rot13value)

def base64_encode():
    message = input("\nPlease provide value to encode: ")

    message_bytes = message.encode('ascii')
    base64_bytes = base64.b64encode(message_bytes)
    base64_message = base64_bytes.decode('ascii')

    print(base64_message)

def base64_decode():
    base64_message = input("\nPlease provide the Base64 value: ")

    base64_bytes = base64_message.encode('ascii')
    message_bytes = base64.b64decode(base64_bytes)
    message = message_bytes.decode('ascii')

    print(message)

def quitter():
    ascii_closing_banner = pyfiglet.figlet_format("Peace!\n")
    print(ascii_closing_banner)
    time.sleep(3)

# Main 

ascii_banner = pyfiglet.figlet_format("\nEncoding \nand\n Decoding \nOld School")
print(ascii_banner)

while (again != 'N'):

    try:
        choice = int(input("\nEnter \n (1) for ROT13\n (2) for Base64\n (3) to quit \r\n\n Choice: "))
    except ValueError:
        print("Invalid Choice!")
        break

    if (choice == 1):
        next_choice = int(input("\nEnter \n (1) to encode\n (2) to decode\n (3) to quit \r\n\n Choice: "))

        if (next_choice == 1):
            rot13_encode()
        elif (next_choice == 2):
            rot13_decode()
        else:
            break
    if (choice == 2):
        next_choice = int(input("\nEnter \n (1) to encode\n (2) to decode\n (3) to quit \r\n\n Choice: "))

        if (next_choice == 1):
            base64_encode()
        elif (next_choice == 2):
            base64_decode()
        else:
            break
    else:
        quitter()
        break

    again = input("\nWould you like to look up more? (Y/N) ")

else:
    quitter()