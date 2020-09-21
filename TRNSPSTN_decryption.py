#self dev transposition decryption algorithm

import math

def main():
    ct = input("enter your Text : \n")
    lenn = len(ct)
    print(lenn)
    encKey = int(input("enter the Encryption key : \n"))
    pt = decryptText(ct , encKey)
    print("ciphered text : %s" %ct )
    print("plain Text : %s" %pt + "|")
    quit = input("press enter to exit")
    #the pipe is added to recognize the spaces at the end.

def decryptText(text , mky):
    lenn = len(text)
    numberOfRows = mky
    numberOfColumns = math.ceil(lenn/mky)
    numberOfshadowedCases = numberOfRows*numberOfColumns - lenn
    somnumb = numberOfRows - numberOfshadowedCases  
    vertical = [""] * numberOfColumns
    for i in range(numberOfColumns):
        index = i
        raw = 0
        col = i
        while index <= len(text) - 1:
            if col == numberOfColumns - 1 and raw == somnumb:
                break
            vertical[i] += text[index]
            if col != numberOfColumns - 1 and raw >= somnumb:
               index += numberOfColumns - 1
            else:
                index += numberOfColumns
            raw += 1
            
                
    return ''.join(vertical)


if __name__ == '__main__' :
    main()

    
    
