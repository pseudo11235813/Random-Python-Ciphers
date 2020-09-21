

#self-dev rail fence transposition Algorithm
#rail fence is one the so many transposition Ciphers, relies on the message is written with alternating letters on separate upper and lower lines.The sequence of letters on the lower line is then tagged on at the end of the sequence on the upper line to create the ﬁnal encrypted message.

def RFENC(text):
    i = 0
    upper = ""
    lower = ""
    while i < len(text):
        if i%2==0:
            upper += text[i]
        else:
            lower += text[i]
        i += 1
    ciphered = upper + lower
    return ciphered
def RFDCP(text):
    if len(text)%2 == 0:
        first = text[:int((len(text)/2))]
        last = text[int((len(text)/2)):]
        i = 0
        plained = ""
        while i < len(first):
            plained += first[i] + last[i]
            i += 1
    else:
        first = text[:(int((len(text) - 1) / 2) +1)]
        last = text[(int((len(text) - 1) / 2) +1) :]
        i = 0
        plained = ""
        while len(plained) != len(text):
            if i == len(first)-1:
                plained += first[i]
            else:
                plained += first[i] + last[i]
                i += 1
    return plained

def main():
    print("rail fence started.")
    text = input("enter your text : ")
    print("do you want to encrypt or to decrypt? (E/D)")
    response = input(">> ")
    while response.lower() != 'e' and response.lower() != 'd':
        print("wrong answer, Re-enter Please.")
        response = input(">> ")
    if response.lower() == "e":
        enc = RFENC(text)
        print("encrypted text : %s"%enc)
    elif response.lower() == "d":
        dec = RFDCP(text)
        print("decrypted text : %s"%dec)
    quit = input("press enter to exit.")
if __name__ == '__main__':
    main()     












            
