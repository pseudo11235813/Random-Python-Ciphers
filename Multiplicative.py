import cryptoMath

def main():
    letters = "\"!#$%&'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\\] ^_`abcdefghijklmnopqrstuvwxyz{|}~"
    text = input("enter text... ")
    resp = input("enter (E) to encypt/(D) to decrypt... ")
    while resp.lower() not in ['e','d']:
        resp = input("wrong answer, re-enter... ")
    if resp == 'e':
        print("wanna go semytric or anti?")
        
        s = input("(S)/(AS)....")
        while s.lower() not in ['s','as']:
            s = input("invalid, re-enter...")
        if s.lower == 's':
            key = int(input("enter key... "))
            while (cryptoMath.reltivelyPrime(key,len(letters))) != True:
                key = int(input("key invalid, key must be relatively prime with the length of the letters set which is 26 for now, re-enter... "))
    
            trans = encrypt_decrypt(text,key,letters)
            print("entered text : %s"%(text))
            print("transformed text : %s"%(trans) + "\n")
            print("since you went for a Semetric Enctyption, you wouldn't need the decryption key just use the same key.")            
        else:
            key = int(input("enter key... "))
            while (cryptoMath.reltivelyPrime(key,len(letters))) != True:
                key = int(input("key invalid, key must be relatively prime with the length of the letters set which is 26 for now, re-enter... "))
            trans = encrypt_decrypt(text,key,letters)    
            print("plain text : %s"%(text))
            print("transformed text : %s"%(trans) + "\n")
            print('here is the decryption key : ' , cryptoMath.modularInverse(key,len(letters)))
    
            
    else:
        print("wanna go semytric or anti?")
        s = input("(S)/(AS)....")
        while s.lower() not in ['s','as']:
            s = input("invalid, re-enter...")
        if s.lower() == 's':
            key = int(input("enter the same key that you've done the encryption with... "))
            d_key = cryptoMath.EuclidsextendedAlgorithm(key,len(letters))
            trans = encrypt_decrypt(text,d_key,letters)
            print("entered text : %s"%(text))
            print("transformed text : %s"%(trans) + "\n")
        else:
            key = int(input("enter the decryption key..(either returned by the same encryption function in this program or the one you're aware of)... "))
            trans = encrypt_decrypt(text,key,letters)
            print("plain text : %s"%(text))
            print("transformed text : %s"%(trans) + "\n")
    

def encrypt_decrypt(text,key,letters):
    kawaii = ""
    indx = 0
    for char in text:
        old_index = letters.find(char)
        indx = old_index * key % len(letters)
        if indx >= len(letters):
            indx -= len(letters)
        kawaii += letters[indx]
    return kawaii


if __name__ == '__main__':
    main()
