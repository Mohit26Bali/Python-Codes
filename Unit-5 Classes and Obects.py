                                                                                                            #UNIT-05

                                                                                                    #Classes_and_objects:

#Procedure (C language) and object oreiented programming language(C++, Java,Python)

#Classes can be design/prototype of house but object is actual house. Classes are virtual but objects are real.
#Classes occupy no memory.
#Object contains Data Member(variables declosed inside a class) and Member Functions.(functions declared inside a class)


#process of creating objects from class is instatiation.

'''class demo:
    a=10 #data_member
    print(a)
d1=demo() #creating_object_of_class_demo.'''

#Addition_Of_number:

'''class mohit:
    a=10
    b=23
    c=67
    d=a+b+c
    print(d)
c=mohit()'''

#Adding_Attributes_To_The_Class: Defined by variables. Each object can have its own values for those variables.

'''class rectangle:
    l=56
    b=78
r=rectangle()
print(r.l)
print(r.b)'''

'''class rectangle:
    l=20
    b=30
r=rectangle()
r.l=6776
r.b=356
print("The Area Of Recatngle is : ",r.l*r.b)'''

'''class rectangle:
    l=45
    b=67
r=rectangle()
r2=rectangle()
r2.l=33
r2.b=77
print("The Area Of Rectangle is: ",r2.l*r2.b)'''


#Adding Methods To The Class with self parameter :-

'''class method_demo:    #Member function
    def This_Message(Self):
        print("Mohit is My Name.")
ob1=method_demo()
ob1.This_Message()'''

'''class circle:
    def calarea(self):
        r=eval(input("Enter Radius:"))
        a=3.14*r**2
        print("Area of circle:",a)
ob1=circle()
ob1.calarea()'''

#Class_Variable & Object_Variable:

#Class_Variable is shared by all objects.

'''class i:
    c=4
on=i()
on2=i()
print(on.c)
print(on2.c)'''

'''class ins:
    x=56
    def dis(self,y):
        print(y)
obj1=ins()
obj=ins()
print(obj.x)
print(obj1.x)
obj.dis(10)
obj1.dis(20)'''



'''class ins:
    x=56
    def dis(self,x):
        print(x)
        print(self.x) #calls the variable
obj1=ins()
obj=ins()
print(obj.x)
print(obj1.x)
obj.dis(10)
obj1.dis(20)'''

#The__init__() Function: - reserved methods in python classes. to iniatialise the data member of class.

'''class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
p1=Person("John",33)
print(p1.name)
print(p1.age)'''

#Modify_Object_Properties:

'''class Person:
    def __init__(self,name,age):    #Constructor_function.
        self.name=name
        self.age=age
    def myfn(self):
        print("I'm "+self.name)
p1=Person("John",36)
print(p1.name)
print(p1.age)
p1.age=32
print(p1.age)
p1.myfn()'''
'''this method is automatically called when an object is created from the class and'''

#Dynamically adding instnace variable to object :

'''class student:
    def __init__(self,name,age):    #instance Variable
        self.name=name
        self.age=age
    #create object
stud=student("Mohit",20) #create_object
print("Before")
print("Name: ",stud.name,"Age: ",stud.age)
stud.marks=97
print("After")
print("Name: ",stud.name,"Age: ",stud.age,"Marks: ",stud.marks)'''

# Delete Object Properties:

'''class person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def my_func(self):
        print("Hello My name is "+self.name)
p1=person("Mark ",36)
del p1.age
print(p1.age)  #Error because age was deleted earlier on.'''

#Example_2:
'''class student:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def myfn(self):
        print("Hello My name is "+self.name)
s1=student("Mark",20)
s2=student("Jos",21)
print(s1.name)
print(s1.age)
s1.myfn()
del s1.age
print(s2.name)
print(s2.age)
#deletion of object:
class student:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def myfn(self):
        print("Hello My Name is",self.name)
s1=student("Mohit",23)
s2=student("Rohit",22)
print(s1.age)
print(s1.name)
s1.myfn()
del s2
print(s1.name)
print(s2.name)
print(s2.age)'''

#Display_Class_Attributes

'''class demo:
    name="" #Attributes
    age="" #attribute
    def read(self):
        name=input("Enter your Name : " )
        print("Name  is  ",name)
        age=input("Enter The age : ")
        print("The Age is ",age)
obj=demo()
obj.read()'''

#Destructor_In_Python:

#Destructors are used when an object is no longer needed.

'''class destructor_demo:
    def __init__(self):
        print("Welcome ")
    def __del__(self):
        print("Destructor Running ")
obj=destructor_demo()
del obj'''

#Example 2 All Fuctions Together

'''class employee:
    def __init__(self): #initialisng
        print("Employee Created")
    def __del__(self):  #Calling_DEstructor
        print("Destructor Called")
def create_obj():
        print("Making Object ")         #Printed 2nd as object is created.
        obj=employee()
        print("Function Ends here")
        return obj
print("Callling Create_Obj() Function")         #program starts from here
obj=create_obj()
print("Program Ends ")
del obj'''

#Access Specifiers : -

# A class in Python Has three types of access Modifiers:

# Various OOP languages like C++ etc control access modifications that are used to restrict access to specific data
# Public, Protected and Private specifiers. Protected Access Modifiers can be accessed by only DERIVED class.
# Python uses '_' for determining access control for a specific data member or a member fuction.
# Access Specifiers in Python have important role in securing data.

#Public_Access_Specifiers can be easily accessed. It's open to all.

#Example: -
'''class student:
    def __init__(self,name,age):
        self.studentname=name
        self.studentage=age
    def displayage(self):
        print("Age: ",self.studentage)
obj=student("Mohit ",20)
print("Name: ",obj.studentname)
obj.displayage()'''

#Private_Access_Specifier:

'''class person:
    __name=None #Private_Members
    __bankaccno=None #Private_MEmbers
    def __init__(self): #Constructor
        self.__name="Hello"
        self.__bankaccno=1234
    def display(self): #Publlic_Member_Function
        print("Name=",self.__name)
        print("Bank Account Number is  ",self.__bankaccno)
p=person()
p.display()'''
'''print("Name : ",p.__name)
print("Salary : ",p.__bankaccno)'''

#Example_02:

'''class student:
    __name=None
    __roll=None
    __branch=None
    def __init__(self,name,roll,branch):
        self.__name=name
        self.__roll=roll
        self.__branch=branch
    def __displayDetails(self):
        print("Name: ",self.__name)
        print("Roll: ",self.__roll)
        print("Branch : ",self.__branch)
    def accessPrivateFunction(self):
        self.__displayDetails()
obj=student("Mohit","RK22SG33","IT")
obj.accessPrivateFunction()'''

#Single_UnderScore means PROTECTED.

#Method 0r Function Overloading :-  Same function that can be used multiple times with different set of parameters. This is known as function overloading.

'''def product(a,b):
    p=a*b
    print(p)
def product(a,b,c):
    p=a*b*c
    print(p)
#product(4,5) shows error as python doesnt support method overloading directly. We can only use latest defined method.
product(4,5,5)'''

#Solution For Above Issue : - *args= command line argument.


'''class demo:
    r=0
    def add(self,i=None,*args):
        if i=='int':
            self.r=0
        if i=='str':
            self.r=' '
        for j in args:
            self.r=self.r+j
        return self.r
d1=demo()
print(d1.add('int',10,20,30))
print(d1.add('str','I ',' am ',' Mohit '))'''

# Program Using INIT Method :

'''class a:
    def __init__(self,l,b,r):
        self.l=l
        self.b=b
        self.r=r
    def a_r(self):
        print("Area Of The Rectangle : ",self.l*self.b)
    def a_c(self):
        print("Area of the circle : ",3.14*(self.r**2))
p1=a(2,3,4)
p1.a_r()
p1.a_c()'''

#INHERITANCE : defining a new class with little or no change to an existing class. The new class is called derived class and other is called is Parent Class,

#Types of INheritance :

#  Single Inheritance   deriving single class from a class.

'''class P:
    def sum(self):
        a=int(input("Enter A : "))
        b=int(input("Enter B :"))
        c=int(input("Enter C : "))
        print("Sum is ",a+b+c)
class Q(P):
    def mul(self):
        a=int(input("Enter A : "))
        b=int(input("Enter B : "))
        print("Product is ",a*b)
obj=Q()
obj.sum()
obj.mul()'''

#  Multilevel Inheritance  : We can also inherit a class from a derived class. This is called multilevel inheritance. It can be of any depth in Python.

#A (Base Class) --------->B (Intermediary Class) -------->C (Derived Class)

'''class a:
    def sum(self):
        a=int(input("Enter A : "))
        b=int(input("Enter B : "))
        print("Sum is : ",a+b)
class b(a):
    def mul(self):
        a=int(input("Enter A : "))
        b=int(input("Enter B : "))
        print("Product is  : ",a*b)
class c(b):
    def sub(self):
        a=int(input("Enter A : "))
        b=int(input("Enter B : "))
        print("The Difference is ",a-b)
obj=c()
obj.sum()
obj.mul()
obj.sub()'''

# Multiple Inheritance  :  Base Classes coming together for giving derived class. A+B=C. Two classes combining to give another class.

# When a class is derived from more than one base class it is called multiple Inheritance. The derived class inherits all the features of the base class .

'''class a:
    def sum(self):
        a=int(input("Enter A : "))
        b=int(input("Enter B : "))
        print("Sum is : ",a+b)
class b:
    def mul(self):
        a=int(input("Enter A : "))
        b=int(input("Enter B : "))
        print("Product is  : ",a*b)
class c(a,b):
    def sub(self):
        a=int(input("Enter A : "))
        b=int(input("Enter B : "))
        print("The Difference is ",a-b)
obj=c()
obj.sum()
obj.mul()
obj.sub()'''
        
# Hybrid Inheritance : Hybrid Inheritance is a blend of more than one type of inheritance. The class is derived from the two classes as in the multiple inheritance. However, one of the parent classes is not the base class. It is a derived class.

# Hierarchal Inheritance :  Hierarchical Inheritance If multiple derived classes are created from the same base, this kind of Inheritance is known as hierarchical inheritance


                                                                                                            #Method_OverRiding :


#override means having two or more methods with same name but doing different task. Basically one method overrides the other. If theres any method in the superclass and a method with same name in a subclass then by executing the method of corressponding class will be executed.

'''class aff:
    def sum(self):
        a=45
        b=65
        print(a+b)
class aff2(aff):
    def sum(self):
        a=122
        b=33
        print(a+b)
        super().sum()
r=aff2()
r.sum()
p=aff()
p.sum()'''




    








































        



        







































    









































    



































































