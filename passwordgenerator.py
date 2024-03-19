import random
import string  
length=int(input('enter the length of password  : '))
strength=input('choose an option for complexity of password : \n a: weak\n b: good \n c: strong\n ')

if strength=='a':
   password=' '.join(random.choices(string.ascii_letters,k=length))

elif strength=='b':
   password=' '.join(random.choices(string.ascii_letters+string.digits,k=length))
 
elif strength=='c':
  password=' '.join(random.choices(string.ascii_letters+string.digits+string.punctuation,k=length))


print('your password is :',password)


