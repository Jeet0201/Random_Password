import random
import string

pass_len=12
charValue=string.ascii_letters + string.digits +string.punctuation


#list comrehension [function for i in range (n)]
password="".join([random.choice(charValue) for i in range (pass_len)])   #----Methode(1)

# password=""
# for i in range(pass_len):                                              #----Methode(2)
#     password+=random.choice(charValue)

print("Your Random Password is: ",password)