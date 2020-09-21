
import random, TRENCRYPTION as tree,CAESAR_CIPHER as cc,TRDECRYPTION as dr


LETTERS = " \"!#$%&'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\\] ^_`abcdefghijklmnopqrstuvwxyz{|}~"
flag = False
while flag == False:
    Rseed = int(input("ENTER FIRST KEY(integer) : "))
    flag = True
    for i in str(Rseed):
        if int(i) in list(range(2,10)):
            flag = False
            print('INVALID KEY MY GUY.')
            break

flag0 = False
while flag0 == False:
    rotkey = int(input("ENTER SECOND KEY(integer) : "))
    flag0 = True
    for i in str(rotkey):
        if int(i) in list(range(2,10)):
            flag0 = False
            print('INVALID KEY MY GUY.')
            break
Rseed = int(str(Rseed),2)
rotkey = int(str(rotkey),2)
print("FIRST KEY : %s"%(Rseed))
print("SECOND KEY : %s"%(rotkey))

Ptext = input("enter Text...\n")
mode = input("enter mode,(e)encryption/(d)decryption..... ")
while mode.lower() not in ['e','d']:
    print("invalid mode.")
    mode = input("enter mode,(e)encryption/(d)decryption..... ")
random.seed(Rseed)
Rcode = random.randint(2,len(LETTERS))
shuffeled = tree.encryptText(LETTERS,Rcode)
duck = cc.start(Ptext,mode,rotkey,shuffeled)
print("\n" + duck + "\n")
mod = input("press enter to die-6.-6.-6.")




    
