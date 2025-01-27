#Objects have a type that defines the the data type of the objects
# int , float , bool are scalar objects
print(type(5))
print(type(3.44))
print(type(True))

# casting is knows as type conversion

print(float(5))
print(int(4.55))
print(int(7.7))#here int returs the integer value only and the decimal values are avoided

#round func is used for rounding off
print(round(5.59))

#Expressions:Combine objects and operators to form expressions
print(3+2)
print((4+2)*6-1)
print(float((4+2)*6-1))
print(type(4.0*3))
print(int(1/2))

#Binding variables to values

pi=355/113
print(pi)

#the progrom should be easy to undetstand - best coding style

#calculate area and circumference of a circle 
#using an approximation for pi
pi = 355/113
radius = 2.2
area = pi*(radius**2)
circumference = pi*(radius*2)
print(area)
print(circumference)

#swaping

x=5
y=19
y=x
x=y
print(x)
print(y)