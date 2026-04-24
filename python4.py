#program to check membership in a list
numbers=[10,20,30,40,50]
print("is 20 in list?",20 is numbers)
print("is 60 not in list?",60 not in numbers)


#program to check membership in a string
text="Python Programming"
print("is 'P'in text?",'P'in text)
print("is 'java'in text?",'java' not in text)


#identity operator with integers
a=10
b=10
print("a is b.",a is b)
print("a is not b.",a is not b)

#different list objects
x=[1,2,3]
y=[1,2,3]
print("x is y.",x is y)
print("x==y.",x==y)

#program to check even or odd
num = int(input("Enter a number:"))
if num % 2 == 0:
   print("even number")


#program to classify a number as positive,negative, or zero. using if else
   num=int(intput("enter the number:"))
   if num>0:
       print("positive number")
elif num<0:
       print("negative number")
else:
    print("zero number")

    
#progrm to find largest of the three number
a=int(input("enter the first number:"))
b=int(input("enter the second number:"))
c=int(input("enter the third number:"))      
if a>b and a>c:
      print("largest:",a)
elif b>c:
      print("largest:",b)
else:
      print("largest:",c)



#print 1 to 5 usinf while loop
i = 1
while i<=5:
 print(i)
 i += 1

 #for loop example
 for i in range(1,6):
  print(i)
          
    
