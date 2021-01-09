# -*- coding: utf-8 -*-
"""
Created on Wed Dec 30 02:13:03 2020

@author: Louis
"""
"""
The theory behind RSA is explained in the Readme file in the repository. This 
python file is the first of three that form a complete RSA system. This file 
in particular will allow you to construct your own set of keys for RSA. The 
goal of this file is to establish the size of primes required to encrypt the 
message you have and then provide you with an encryption and decryption key. 
Currently the user has to input there own encryption key, in the future I hope 
to add a 'choosingE():' function thatwill allow the user to pick from one of 
many random possible values of e or input their own. Due to this the user is 
required to know how to pick a 'good' value for e (and p,q), this information 
can be found in the readme file.
"""
def valuesRSA(p,q): #Calculates n and phi(n) from two input primes p,q.
    n = p*q
    phi = (p-1)*(q-1)
    return [n,phi]

def calculatingD(e,phi): #After choosing the encryption key, this function 
    if e == 0:           #calculates the decryption key. (Bezout's Theorem).
        return (phi, 0, 1)
    else:
        gcd, x, y = calculatingD(phi%e,e)
        return (gcd, y-(phi//e)*x,x)
    
def signOfD(d,phi): #Occasionally d is negative, but since we work 
    if d < 0:       #modulo phi(n), we can change this easily.
        return d + phi
    else:
        return d

def main():
    message = input('Input the message you wish to encrypt with RSA: ')
    p = int(input('Input a prime with roughly ' + str(len(message)+1) + ' digits: '))
    q = int(input('Input another prime with at least ' + str(2*len(message)-len(str(p))+1) + ' digits: '))
    n = valuesRSA(p,q)[0]
    phi = valuesRSA(p,q)[1]
    e = int(input('Input a value for e: '))
    print('')
    d = calculatingD(e,phi)[1]
    d = signOfD(d,phi)
    print('message = ' + message)
    print('p = ' + str(p))
    print('q = ' + str(q))
    print('n = ' + str(n))
    print('phi(n) = ' + str(phi))
    print('e = ' + str(e))
    print('d = ' + str(d))
    return

main()
"""
The RSA encryption key is (e,n) and decryption key is (d,n). 
"""
