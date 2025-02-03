#break statement used to terminate from any loop
#examples
mysum=0
for i in range(1,10):
	mysum+=i
	break
print(mysum)

mysum=0
for i in range(5,11,2):
	mysum+=i
	if mysum==5:
		break
		mysum+=1
print(mysum)

#to find even number and count them

x=int(input('Enter a start range:'))
y=int(input('Enter a stop range:'))
z=int(input('Enter a step range:'))
even=0
for i in range(x,y,z):
	if(i%2==0):
		
		even+=1
print(even)


#strings in loop 

s='hello,how can i help you'
for index in range(len(s)):
	if(s[index]=='i' or s[index]=='e'):
		print('there is i or e')
		
for char in s:
	if(char=='i' or char=='e'):
		print('there is i or e')
		
for char in s:
		if char in 'ie':
			print('there is i or e')
			
#count the unique characters in a strings

s='abcdefffffgggggghhhhh'
seen=''
for char in s:
	if char not in seen:#not is an logical operator which converts the true into false and vice versa
		seen+=char
		print(seen)
print(len(seen))


#guess and check algorithm
#to find square root of an number

guess=0
num=int(input('Enter a number: '))
while guess**2<num:
	guess+=1
if(guess**2==num):
	print('the square root is',guess)
else:
	print(num,'is not a perfect square')
	
	
#if negative number is given , the above program is rewritten as

guess=0
neg_flag=False
num=int(input('Enter a number: '))
if(num<0):
	neg_flag=True
while guess**2<num:
	guess+=1
if(guess**2==num):
	print('the square root is',guess)
else:
	print(num,'is not a perfect square')
	if(neg_flag):
		print('Just checking...did you mean',-num,'?')
		
#example 		
secret=100
found=True
for i in range(1,11):
		if(i==secret):
			print('yes its',i)
			found=False
if(found):
			print('not found')
			
			
#program using guess and check to find cube root of an number

cube = int(input("Enter an integer: "))
for guess in range(abs(cube)+1):
	if guess**3 >= abs(cube):
		break
if guess**3 != abs(cube):
		print(cube, "is not a perfect cube")
else:
	if cube < 0:
		guess = -guess
	print("Cube root of "+str(cube)+" is "+str(guess))
	
	



		




			
		


