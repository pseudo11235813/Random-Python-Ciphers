
#some usable math functions

def gcd(a,b): # function that returns the greatest common divisor or two integers
    while a!= 0:
        a,b = b % a , a
    return b


def modularInverse(a,b): # fucntion that returns the modular inverse of two integers, this function is used when decrypting a code that's been decrypted with the multiplicative cipher, because when we encrypt with the multiplicative cipher we multiply a number by the key then calculate the module or the remainder of the result by the length of the set of symbols, so to decrypt we gotta mltiply by the modular inverse of the encryption key by the length of symbols set.
    i = 1
    while((a * i) % b != 1):
        i += 1
    return i

def EuclidsextendedAlgorithm(a , b):
    if gcd(a , b ) != 1:
        return None
    u1, u2, u3 = 1, 0, a
    v1, v2, v3 = 0, 1, b
    while v3 != 0:
        q = u3 // v3
        v1, v2, v3, u1, u2, u3 = (u1 - q * v1), (u2 - q * v2), (u3 - q * v3), v1, v2, v3
    return u1 % b

def reltivelyPrime(a,b):
    if gcd(a,b) == 1:
        return True
    return False
