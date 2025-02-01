#while loop , the sequence of code under it will execute until the condition is false
where=input("you are in the lost forest.Go left or right: ")
while(where=='right'):
	where=input("you are in the lost forest.Go left or right: ")
print('you are out of the lost forest ')
#note that the condition given in the while loop is case sensitive 

#simple example
n=10
while(n<20):
	print('hii')
	n+=2 #if condition never false , then the code under while loop will execute infinite number of times
	
#factorial using while loop

num=int(input('Enter a number: '))
i=1
fact=1
while(i<=num):
	fact*=i
	i+=1
print('the factorial of' ,int(num), 'is:' ,fact)

#for loop , here loop variable is defined in the loop 

for n in range(5):
	print(n)

#in for loop , the range can be provided with start , stop and step values like strings

for i in range(1,4,1):
	print(i)
for j in range(1,4,2):
	print(j*2)
for me in range(4,0,-1):
	print("$"*me)
	
mysum=0
x=int(input("Enter a number: "))
for i in range(x):
	mysum+=i
print(mysum)#mysum is a variable


#factorial using for loop 

num=int(input('Enter a number: '))
fact=1
for i in range(1,num+1):
	fact*=i
print("the factorial of ",int(num)," is",fact)



