# -*- coding: utf-8 -*-
"""
Created on Wed Dec 30 01:38:35 2020

@author: Louis
"""
"""
This is the third of three python files that encrypt a message using RSA. As
an input it requires an encrypted message, the decryption key d and the public
number n. It will return the original message completely decrypted.
"""
def decryptionRSA(encryptedMessage,d,n):
    decryptedMessage = pow(encryptedMessage,d,n)
    return decryptedMessage

def decode(decryptedMessage,numbersToLetters):
    D = str(decryptedMessage)
    decodedMessage = ''
    for i in range(0,len(D),2):
            a = str(D[i]+D[i+1])
            decodedMessage += numbersToLetters[a] 
    return decodedMessage

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
    numbersToLetters = {l:n for n,l in lettersToNumbers.items()}
    encryptedMessage = int(input('Input the message you wish to decrypt here: '))
    d = int(input('Input decryption key: '))
    n = int(input('Input public number (n): '))
    print('')
    decryptedMessage = decryptionRSA(encryptedMessage,d,n)
    print('Your decrypted message is: ' + str(decryptedMessage))
    print('')
    decodedMessage = decode(decryptedMessage,numbersToLetters)
    print('Your message is: ' + decodedMessage)
    return

main() 