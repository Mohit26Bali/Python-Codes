#Celcius_to_fahrenheit:-

'''print("Enter Temperature in Celcius:")
cel=float(input())
fah=(cel*1.8)+32
print("\nEquivalent Value in Fahrenheit=",fah)'''

#Calculating_average_%_marks:-

'''print("Enter Marks obatined in 5 subjects:")
a=int(input())
b=int(input())
c=int(input())
d=int(input())
e=int(input())
sum=a+b+c+d+e
avg=sum/5
perc=(sum/500)*100
print(sum)
print(avg)
print(perc)'''

#Area_of_a_triangle:-

'''print("Enter the base length of triangle:")
b=float(input())
print("Enter the height length of triangle:")
h=float(input())
a=0.5*b*h
print("\nArea=",a)'''

#Solving_Quadratic_Equations:-

'''import cmath
print("Enter the value of a:",end="")
a=int(input())
print("Enter the value of b:",end="")
b=int(input())
print("Enter the value of c:",end="")
c=int(input())
discriminant=(b**2)-(4*a*c)
solutionOne=(-b-cmath.sqrt(discriminant))/(2*a)
solutiontwo=(-b+cmath.sqrt(discriminant))/(2*a)
print(solutionOne)
print(solutiontwo)'''

#FInding&printing ASCII value:-

'''print("Enter a character:")
ch=input()
asc=ord(ch)
print("\n ASCII Value:",asc)'''

'''print("Enter A Unicode:")
asc=int(input())
ch=chr(asc)
print("\n Character is:",ch)'''

#Keyword_list:-

'''import keyword
print(keyword.kwlist)'''

#if_condition:-

'''z=5
if z%2==0:
    print("z is even number")
else:
    print("z is odd number")'''

#if-elif-else:-

'''z=5
if z%2==0:
    print("z is divisible by 2")
elif z%3==0:
    print("z is divisible by 3")
else:
    print("z is neither divisible by 3 and 2")'''

#Program_for_if_condition:-

'''a=int(input("Enter the marks of subject 1:"))
b=int(input("Enter the marks of subject 2:"))
c=int(input("Enter the marks of subject 3:"))
d=int(input("Enter the marks of subject 4:"))
e=int(input("Enter the marks of subject 5:"))
avg=(a+b+c+d+e)/5
if (avg>90):
    print("A+ Grade")
elif (avg>=80 and avg<90):
    print("A Grade")
elif(avg>=70 and avg<80):
    print("B Grade")
elif(avg>=60 and avg<70):
    print("C Grade")
else:
    print("D Grade")'''

#Calculator:-

'''print("CALCULATOR ")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")
ch=int(input("Enter Choice(1-4):"))
if ch==1:
    a=int(input("Enter A:"))
    b=int(input("Enter B:"))
    c=a+b
    print("Sum=",c)
elif ch==2:
    a=int(input("Enter A:"))
    b=int(input("Enter B:"))
    c=a-b
    print("Difference=",c)
elif ch==3:
     a=int(input("Enter A:"))
     b=int(input("Enter B:"))
     c=a*b
     print("Product=",c)
elif ch==4:
     a=int(input("Enter A:"))
     b=int(input("Enter B:"))
     c=a/b
     print("Quotient=",c)
else:
    print("Invalid Choice")'''

#checking_vowel_or_not:-

'''print("enter a character:")
c=input()
if c=='a' or c=='e' or c=='i' or c=='o' or c=='u':
    print("It is a Vowel.")
elif c=='A' or c=='E' or c=='I' or c=='O' or c=='U':
    print ("It is a vowel as well.")
else:
    print("It is not a Vowel.")'''

'''print("Enter a Character:")
c=input()
if c>='a' and c<='z':
    print("It is a small alphabet.")
elif c>='A' and c<='Z':
    print("It is a capital alphabet.")
else:
    print("it is not an alphabet.")'''

#MemberShip_Operators:-
#(in) and (2)NOt in

'''x=["apple","banana"]
print("banana" in x)'''

'''x=["apple","banana"]
print("grapes" not in x)'''

'''a=str(input("Enter a String:"))
b=str(input("Enter a substring:"))
print(b in a)'''

#The_DivMod(dividend,divisor):- provides (quotient,remainder)

'''print(divmod(15,3))'''

#Input():

'''a=23
b=56
print("A value is",a,"and","B value is",b)'''

'''i=4354
f=2107.088
d=144.077
str1="Mohit BM"
print(i,f,d,str1)
print(i,f,d,str1,sep="....",end=" HELLO")'''

#String-Modulor_Operator: %d=integer,%f=float,%x or %X for HexaDEcimal,%s for string,%<no. of digits>f=floating point number with fixed amount of digits for decimal part.

'''name="Mohit Bali"
print("Good Morning,Mohit Bali!")
print("Good Morning,%s!"%name)

a=7666
b=67687
c=5656
print("the value of a=%d,b=%d and c=%d" %(a,b,c))'''

#
'''print("Total Number of votes:%3d, Women Vote:%3d"%(480,70))'''

#LECTURE-04 ENDS HERe

#%3d means it'll be printed till 3rd character ,hence no blank space.whereas putting value more than the number of digits will lead to blank spaces.

#Formatting:- 

'''a=6663
b=3666
c=977887
print("THe value of a={},b={} and c={}".format(a,b,c))'''

'''a=67677
b=87878
c=67767
d=568900
print("The value of a={},b={},c={} and d={}".format(a,b,c,d))'''

'''a=10
print("value of a={}".format(a))
x=20
print("the value of x={0:10d}".format(x))
m=3.14
print("the value of m={0:.10f}".format(m))
d=16
print("THe value of d={0:X}".format(d))
c=16
print("the value of c={0:o}".format(c))'''

#LECTURE-05 ENDS HERE




