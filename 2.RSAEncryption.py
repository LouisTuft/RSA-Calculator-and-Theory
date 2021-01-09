# -*- coding: utf-8 -*-
"""
Created on Tue Dec 29 21:07:06 2020

@author: Louis
"""
"""
This python file is the second of three and it will encode and encrypt a given 
message using RSA. It requires an input message and public key which consists 
of an encryption key e and a public number n, both of which can be calculated 
using the python file RSAValues.
"""
def encode(message,lettersToNumbers): #In order to encrypt a message we first
    encodedMessage = str('')          #need to convert it to an integer. We do
    for character in message:         #this using a dictionary.
        encodedMessage = encodedMessage + lettersToNumbers[character]
    encodedMessage = int(encodedMessage)
    return encodedMessage


def encryptionRSA(encodedMessage,e,n): #This encrypts the message by doing
    encryptedMessage = pow(encodedMessage,e,n) #encodedMessage^(e) (mod n)
    return encryptedMessage

def main():
    lettersToNumbers = {
    "0": "70", "1": "71", "2": "72", "3": "73", "4": "74", "5": "75",
    "6": "76", "7": "77", "8": "78", "9": "79",

    "a": "10", "b": "11", "c": "12", "d": "13", "e": "14", "f": "15",
    "g": "16", "h": "17", "i": "18", "j": "19", "k": "20", "l": "21",
    "m": "22", "n": "23", "o": "24", "p": "25", "q": "26", "r": "27",
    "s": "28", "t": "29", "u": "30", "v": "31", "w": "32", "x": "33",
    "y": "34", "z": "35",

    "A": "36", "B": "37", "C": "38", "D": "39", "E": "40", "F": "41",
    "G": "42", "H": "43", "I": "44", "J": "45", "K": "46", "L": "47",
    "M": "48", "N": "49", "O": "50", "P": "51", "Q": "52", "R": "53",
    "S": "54", "T": "55", "U": "56", "V": "57", "W": "58", "X": "59",
    "Y": "60", "Z": "61",
    " ": "99", ".": "98", "£": "97", "$": "96", ":": "95", "/": "94",
    }
    message = input('Input the message you wish to encrypt here: ')
    e = int(input('Input encryption key: '))
    n = int(input('Input public number (n): '))
    encodedMessage = encode(message,lettersToNumbers)
    encryptedMessage = encryptionRSA(encodedMessage,e,n)
    print('')
    print('The encrypted message is as follows: ' + str(encryptedMessage))
    return

main() 
