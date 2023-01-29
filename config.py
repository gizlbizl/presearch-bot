import string
import random


chars = string.ascii_letters + string.digits
PasswordLength = 8

GetPwd = ''.join((random.choice(chars)) for x in range(PasswordLength)) 

if GetPwd in open('log.txt').read():
    print ("generation")
    GetPwd = ''.join((random.choice(chars)) for x in range(PasswordLength)) 

else:
 print ("mots generer")                  
with open("log.txt", "w") as myfile:
    myfile.write(GetPwd)
	
