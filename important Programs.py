#fibonnacci_series01
'''num=int(input("enter a term...."))
a,b,fib=0,1,0
range=num-1
while fib<range:
    print(fib)
    a=b
    b=fib
    fib=a+b'''

#fibonacci_Series02

'''range=int(input("How many Terms? "))
a,b=0,1
count,fib=0,0
while count<range:
    print(fib)
    a=b
    b=fib
    fib=a+b
    count=count+1'''

#prime_number_Program

'''num=int(input("enter a number: "))
p=0
i=2
while i<=num:
    if num%i==0:
        p=p+1
    i=i+1
if p==1:
    print("the number is prime ")
else:
    print("the entered number is not a prime number ")'''

#break_program

'''i=1
while i<6:
    print(i)
    if(i==3):
        break
    i+=1'''

#counting_digits

'''num=4565
count=0
while num!=0:
    num//=10
    count+=1
print("number of digts:",count)'''

#Program_for_armstrong_number:

'''num=int(input("Enter a number: "))
sum=0
temp=num
while temp>0:
    digit=temp%10
    sum+=digit**3
    temp//=10
if num==sum:
    print("The Entered Number is an Armstrong Number ")
else:
    print(num,"is not an armstrong number ")'''

#Palimdrome_Number_program:

'''num=int(input("enter a number: "))
temp=num
rev=0
while (num!=0):
    dig=num%10
    rev=rev*10+dig
    num=num//10
if (temp==rev):
    print("The entered number is a palindrome number")
else:
    print("The Entered number is not a palindrome number")'''

#Program_For_Factorial_Of_Number:

'''num=int(input("Enter a number: "))
factorial=1
if num<0:
    print("Sorry, No Factorial for Negative Number.")
elif num==0:
    print("The factorial of 0 is 1.")
else:
    for i in range (1,num+1):
        factorial=factorial*i
    print("The Factorial of",num,"is",factorial)'''

#Program_for_bill_calculation:

'''print("Best Billing")
tp=0
n=int(input("Total Numbers of items:"))
for i in range(n):
    print("\t\tEnter price of each item:",i)
    p=int(input("Enter amount:"))
    tp=tp+p
print("\t\t\tTotal Bill Amount:",tp)'''

#Strong_Number:-

'''sum1=0
num=int(input("Enter a number: "))
temp=num
while(num>0):
    i=1
    f=1
    r=num%10
    while(i<=r):
        f=f*i
        i=i+1
    sum1=sum1+f
    num=num//10
if(sum1==temp):
    print("Entered number is a strong number.")
else:
    print("Entered Number is not a strong number.")'''

#Password_program:-

'''for i in range(3):
    ID=int (input("Enter ID:-"))
    Password=str(input("Enter Password:-"))
    if ID==111 and Password=='xyz' :
                 print("Login")
                 break
    else:
        print("Incorrect. Please Try Again.")
else:
    print("Your three chances are over.")'''

#Program_to_add_natural_numbers:-
'''n=10
sum=0
i=1
while i<=n:
    sum=sum+i
    i=i+1
print("The sum is",sum)'''

#reverse_of_a _number:-

'''num=int(input("Please enter any number:"))
rev=0
while num>0:
    rem=num%10
    rev=rev*10+rem
    num=num//10
print("reverse of entered number is= ",rev)'''


