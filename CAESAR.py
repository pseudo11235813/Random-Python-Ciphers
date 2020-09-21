##typical ceasar cipher algorithm with infinite value for the encryption/decryption key.
import math
def start(text,Cmode,key,LETTERS = "\"!#$%&'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\\] ^_`abcdefghijklmnopqrstuvwxyz{|}~"):
    ciphertext = ""
    if key >= len(LETTERS):
        key = int(math.remainder(key,len(LETTERS)))
    for letter in text:
        if letter in LETTERS:
            num = LETTERS.find(letter)
            if Cmode == 'e' :
                num += key
            elif Cmode == 'd':
                num -= key
                
            if num >= len(LETTERS) :
                num -= len(LETTERS)
            elif num < 0:
                num = len(LETTERS) + num
            ciphertext += LETTERS[num]
        else:
            ciphertext += letter
    return ciphertext    

def bruteForce(text,Cmode,LETTERS = "\"!#$%&'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\\] ^_`abcdefghijklmnopqrstuvwxyz{|}~"):
    listed = []
    for key in range(len(LETTERS)):
        ciphertext = ''
        for letter in text:
            if letter in LETTERS:
                num = LETTERS.find(letter)
                if Cmode == 'e' :
                    num += key
                elif Cmode == 'd':
                    num -= key
                
                if num >= len(LETTERS) :
                    num -= len(LETTERS)
                elif num < 0:
                    num = len(LETTERS) + num

                ciphertext += LETTERS[num]
            else:
                ciphertext += letter
        listed.append(ciphertext)
    return listed    

def main():
    text = input("enter your text : ")
    text = text.upper()
    cipherMode = input("chose a ciphering mode,(e) for encypting and (d) for decrypting : ")
    while cipherMode.lower() not in ['e','d']:
        print("invalid mode.re-enter.")
        cipherMode = input("chose a ciphering mode,(e) for encypting and (d) for decrypting : ")
    sal = input("chose whether to use a key(k) or to genrate texts using all keys(bruteForce)(b) : ")
    while sal not in ['k','b']:
        print('invalid CHOICE. re-enter')
        sal = input("chose whether to use a key(k) or to genrate texts using all keys(bruteForce)(b) : ")
    if sal == 'b':
        cipherText = bruteForce(text,cipherMode)
        h = 0
        for i in cipherText:
            print('key %s , text:%s'%(h,i))
            h+=1
    
    else:
        key = int(input("enter key : "))
        cipherText = start(text,cipherMode,key)
        print(cipherText)
    quit = input("click enter to exit")
if __name__ == '__main__':
    main()
