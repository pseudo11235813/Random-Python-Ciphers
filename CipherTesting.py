#self dev program testing the 2 algorithms that encrypt and decrypt texts using the Transposition Cipher .
#can be done to other Ciphering Algorithms.

import sys,random,TRENCRYPTION as tre,TRDECRYPTION as trd

def main():
    random.seed(42)#setting the seed to 42 so we can generate predictable numbers using randint or else, change the seed will change the pseudorandom numbers
    for i in range(20):#testing the cipher 20 times for 20 random texts
        pt = "ABCDEFGHIJKLMNOPQRSTUVWXYZ" * random.randint(4,20)# creating a random text
        ptlist = list(pt)# converting the String (text) into a list
        random.shuffle(ptlist) #shuffling the list items
        pt = ''.join(ptlist) #converting the shuffledl list into a String
        for numb in range(2,len(pt)): #trying the Transposition cipher with all possible keys for the generated plain text
            encrpt = tre.encryptText(pt,numb)#encrypting the text
            decrpt = trd.decryptText(encrpt,numb)#decrypting the text
            if(decrpt != pt):#checking if the decrypted text is the same as the original plain text ; if not there is an error on the tranposition program ,the enc or the dec
                print("error in the cipher Algorithm detected")
                print("the plain text isn't the same as the decrypted encrypted text")
                print("the cipher didn't work correctly using the key %s" %numb)
                print("encypted text : %s" %encrpt)
                print("decrypted text : %s" %decrpt)
                print("plain text : %s" %pt)
                sys.exit()#the program immediately stops working
            print("text number %s , key number : %s" %(i+1 , numb) , "works just fine :3 ")
        print()
    print("the Transposition Cipher works 100% for the generated Strings.")
    quit=input("press enter to exit")

if __name__ =='__main__':#makes sure that the program isn't imported as a module
    main() #run :v






