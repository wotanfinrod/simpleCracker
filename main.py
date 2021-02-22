import crypt
import sys



password = sys.argv[1]

salt = password[0:2]
isFound = False


sozlukFile = open("TDK-kelime-listesi.txt", "r")

for word in sozlukFile:
    word = word.rstrip("\n")
    x = crypt.crypt(word, salt)

    if x == password:
        foundpassword = word
        isFound = True
        break


if isFound == True:
    print("PASSWORD IS DECRYPTED!!!! GG EZ")
    print("Password is: " + foundpassword)
    print("HACKED BY XXXw0+4nXXX")
else:
    print("Password cannot be found :(")
