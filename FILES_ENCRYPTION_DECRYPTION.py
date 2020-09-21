#SELF-DEV FILES ENCRYPTING/DECRYPTING WITH THE TRANSPOSITION CIPHER.

import sys,os,time,transpositionCipherdecryption as trd,transpositionCipherencryption as tre

def main():
    print("TRANSPOSITION CIPHER PROGRAM STARTED.")
    print("enter the File name that you want to encrypt/decrypt.\nnote : enter the File with its full path, unless if it exists in the the same folder where the this program exists(python32-by default)(if the file is in the program Folder you can just type the text File's name without the name).\nnote : in the path enter double back/forward slashes instead of one (//-\\\)")
    inputFile = input('make sure to add the .txt extinsion \n>> ')
    while not os.path.exists(inputFile):
        print("the File %s doesn't exist please Re-enter the File's name."%inputFile)
        inputFile = input('>> ')
    print("the File %s exists."%inputFile)
    print("enter the File(with path) name where you want to save the encrypted/decypted text.\nnote : if the File doesn't exist a File with the name you've entered will be created. \nnote : if the File exists it'll be overwritten.\nnote : if you don't enter the whole path this program will create the File in the Desktop Folder. \nnote : if you enter only the file name the default path will be this program's containing Folder(will be asked if you want it be created in the Desktop Folder).")
    outputFile = input('>> ')
    print("By default this program will create the output File in the Desktop Folder.")
    print("If you already entered the whole path this option will be canceled. ")
    print("Did you specify the whole path (Y/N) ?")
    resp = input('>> ')
    while (resp.lower() != "y") and (resp.lower() != "n"):
        print("Re-enter your reply please.")
        resp = input('>> ')
    if resp.lower() == 'n':
        print("Is it okay that the output File will be created in the Desktop Folder ?")
        print('(Y/N)?')
        ans = input('>> ')
        while ans.lower() != 'y' and ans.lower() != 'n':
            print("Re-enter your reply please.")
        if ans.lower() == 'n':
            print("your File will be created in this program's containing Folder  ")
        else:#change this path below if necessary
             #it is necessary :D
            outputFile = "c:/users/kais/Desktop/" + outputFile
            print("your File right now will be created in the Desktop Folder.")
    else:
        print("nice")
    if not outputFile.endswith(".txt"):
        outputFile += ".txt"
    print("the output File : %s" % outputFile)
    check = True
    while os.path.exists(outputFile) and check == True:
        print("are you sure you want to save the output in the File %s ? if so, this File will be replaced by another one that contains the encrypted/decrypted text."%outputFile)
        print("the File %s will be overwritten."%outputFile)
        print("enter (C)ontinue to complete the operation, (E)xit to reenter the output Fil's name or (S)ystemExit to end the program. (C/E/S)?")
        response = input('>> ')
        while response.lower() != 'c' and response.lower() != 'e' and response.lower() != 's':
            print("your reply is not understandable, Re-enter please.")
            response = input('>> ')
        if response.lower() == 's':
            sys.exit()
        elif response.lower() == 'c':
            check = False
        elif response.lower() == 'e':
            print("please enter the full path :)")
            outputFile = input('>> ')
        if not outputFile.endswith(".txt"):
            outputFile += ".txt"
    letin = open(inputFile)
    inputTxt =letin.read()
    letin.close()
    print("Enter whether you want to (E)ncrypt or (D)ecrypt (E/D) ?")
    CiphMode = input('>> ')
    while CiphMode.lower()!= 'e' and CiphMode.lower() != 'd' :
        print('Re-enter please.')
        CiphMode = input('>> ')
    print("Enter the Ciphering key please.")
    cKey = int(input('>> '))
    if cKey >= len(inputTxt):
        print("nothing will change in the output File because the key is longer than the number of characters in the inputFile.")
        print("the output File will be created anyway.")
    startTime = time.time()
    if CiphMode.lower() == 'e':
        transpositioned = tre.encryptText(inputTxt,cKey)
    elif CiphMode.lower() == 'd':
        transpositioned = trd.decryptText(inputTxt,cKey)
    endtTime = time.time()
    totalTime = round(startTime - endtTime , 2)
    if CiphMode == 'e':
        print("Encrypting done in %s seconds "%totalTime)
    elif CiphMode == 'd':
        print("Decrypting done in %s seconds "%totalTime)

    letout = open(outputFile,'w')
    letout.write(transpositioned)
    letout.close()

    if CiphMode == 'e':
        print("Encrypting Done.")
    elif CiphMode == 'd':
        print("Decrypting Done.")
    print("File contains %s characters"%len(inputTxt))
    print("output File : %s"%outputFile)

if __name__ == '__main__':
    main()

