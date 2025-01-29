#string is a sequence of characters surrounded by quotes
#we can concatenate and repeat strings
a='hello'
b='world'
c=a+' '+b
print(c) #concatenation of two strings

#repeatation of a string

print((a+' ')*5)

#examples
b = ":"
c = ")"
s1 = b + 2*c
print(s1)

f = "a"
g = "b"
h = "3"
s2 = (f+g)*int(h)
print(s2)


#len() is a function used to determine the length of a string

s1='how are you '
print(len(s1))

#len() function is also space sensitive and it provides the output as integer values

#slicing the string

s = 'abcdefgh'
print(s[3:6])
print(s[3:6:2])
print(s[:])
print(s[::-1])
print(s[6:2])


#input concept of strings

num1 = input("Type a number: ")
print(5*num1)
num2 = int(input("Type a number: "))
print(5*num2) #here the output will be integer value because the the input string is casted into integer


#practice problem

v=input('Enter a verb: ')
print('I can'+' '+v+' '+'better than you')
print((v+' ')*5)


#comparison operators

i=2
j=5
print(i==j)
print(i<=j)
print(i != j )


#braching example

s=10
t=int(input('Enter a number: '))
if(s==t):
	print('the number is correct')
elif(t<s):
	print('the number is low')
else:
	print('the number is high')