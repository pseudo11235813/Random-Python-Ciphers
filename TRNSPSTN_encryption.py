#self dev transposition encryption algorithm

def main():
    plainText = input("enter your text : \n")
    print("length of the text : %s" %len(plainText))
    key = int(input("enter the ciphering key : "))
    cipherText = encryptText(plainText , key)
    print("plain Text : %s" %plainText )
    print("encrypted Text : %s" %cipherText +"|")
    quit = input("press enter to exit")
    

def encryptText(text , mky):
    vertical = [""] * mky
    for i in range(mky):
        position = i
        while position < len(text):
            vertical[i] += text[position]
            position += mky
    return ''.join(vertical)


if __name__ == '__main__' :
    main()
