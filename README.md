# RSA-calculator-and-theory
RSAValues will calculate your decryption key value d. RSA encryption and decryption files will take input values from the user and encrypt/ decrypt messages respectively. Any feedback is welcomed.

# RSA System
RSA is an encryption system. It is highly secure due to the fact that factorisation of larger integers is very difficult but multiplication of large integers is easy. The systems works by assigning a public key (e,n) and a private key (d,n) to each user, where e and d are found using phi(n). As the names would suggest (e,n) is visible to all, but it is specific to one user, so anyone intending to send an encrypted message to said user can do so. First, we must encode the message using a public code. Then we can take the encoded message (EncdMsg) to the power of e and reduce this modulo n to encrypt the message. 

Encode - Convert a message made up of characters into one larger integer. In this example this is done by replacing each character in the message with a two digit integer from a prearranged public code (lettersToNumbers dictionary) and then concatenating these integers to form one large integer. This integer will have twice as many digits as there are characters in the code.

Encrypt - Put information into a form such that only those who know how to decrypt it can retrieve the information. In this example this is done by computing: Encrypted message =  (Encoded Message)^e (mod n)

Once we have encrypted the message we can happily send it to the intended receiver knowing that if it is intercepted then the data remains secure as only the receiver has the specific decryption key required. To decrypt the message you take the encrypted message to the power of d and reduce it modulo n, then after decoding the integer we are back to the original message.

Decrypt - (Encrypted Message)^d (mod n)

Decode - Reverse of Encode (numbersToLetters dicitonary)

# RSA Theory
So we have seen how this system works but we may have been left with a few holes in our knowledge, I will attempt to fill these below:

What is n?
n is the product of our two chosen primes p and q. n = pq.

What is phi(n)?
phi(n) represents Euler's totient function of a given variable n. This tells you the exact amount of positive integers less than n that are coprime to n. In our case, since n is a product of primes, we know that phi(n) = (p-1)(q-1) which is easy to calculate if we know p and q, but difficult if we do not.

What are e and d?
These values are vital parts of the encryption and decryption keys respectively. They are completely dependant on each other and once one has been chosen the other one can be calculated and is unique. This is how they work in the RSA cryptosystem:
((EncodeMessage)^e)^d (modulo n) = (EncodedMessage)^ed = EncodedMessage (i.e. encrypting and decrypting returns the encoded message.)
We will calculate them below.
 
# Choosing p and q
As stated above, the factorisation of large integers is difficult. With this knowledge we let n = pq, where p and q are both prime. Since n only has two factors it is incredibly difficult to factor provided p and q are not 'predictable. This is ultimately due to the fact that the more factors an integer has, the more likely you are to find one. Below I will list properties that make p and q easier to find prefixed by the way that they can be found:

Simple to spot -  If n is the product of two primes but is even, the sum of it's digits are divisible by 3 or it ends in a 5, then we know that n is divisible by 2, 3 or 5 respectively with very little work to figure that out. 

Trial division - Since trial division divides a given integer n by every prime from 2 up to and including the floor of the square root of n, small factors can be found incredibly quickly. Obviously, as n increases in size, we tend to set a limit of trial division as it isn't very efficient so as long as our primes are bigger than this limit then we are safe. We often choose p and q of similar magnitude to avoid this.

Fermat's algorithm - Works in a similar way to the trial division algorithm but it instead starts at the square root and works out to find factor pairs. This means that p and q shouldn't be too close to eachother. However, above we said they should be of similar magnitude, this is because when we use primes large enough to make RSA genuinely secure they are so large that they can be of a similar magnitude and still massively far apart.

Pollard (p-1) - This is a more difficult flaw to explain, so I recommend reading D.M.Bressoud's book 'Primality testing and integer factorisation' if you wish to understand it. However, if you are just here to understand how the cryptosystem works then this knowledge is surplus, but the book is fantastic.

# Choosing e
The only real constraint when choosing e is that it must be coprime to phi(n) which in turn means it must be coprime to p-1 and q-1. It is a part of the publicly available encryption key so we don't need to bend over backwards coming up with an integer that seems to be more secure because it is larger or a prime because everyone can see it. People often use e = 65537 = 2^16 + 1, since it is 1 above a power of 2 it can be written in binary as a 10000000000000001, this makes for much faster computation when using larger numbers.

# Calculating d
From our discussion above we know the following:
((EncodeMessage)^e)^d (modulo n) = (EncodedMessage)^ed = EncodedMessage (i.e. encrypting and decrypting returns the encoded message.)

Now, this is equivalent to saying that ed is congruent to 1 modulo phi(n), in other words:

ed + k.phi(n) = 1 for some integer k. (This actually has infinitely many solutions but we are interested in the smallest, positive value of d.)

If we choose e then the unknowns in the equation above are d and k, we want to know d but we don't need to know k as we are working modulo phi(n) so its irrelevant. But we can workout the two unkowns by using the Extended Euclidean algorithm, here is an example:

p = 7, q = 5, n = 35, phi(n) = 24. Let e = 7. Then ed + k.phi(n) = 7.d + k.24 = 1.

24 = 7.3 + 3

 7 = 3.2 + 1
 
 3 = 1.3 + 0
 
Now we go back up from our smallest non-zero remainder.

 1 = 7 - 3.2
 
 1 = 7 - (24 - 7.3).2 = 7 - 24.2 + 7.6 = 7.7 - 24.2
 
Therefore d = 7 and k = 2.
