                        #UNIT-4:-


                  #LIST_TUPLES_AND_DICTIONARY:-

#Array: Storing of data of similar types like integer,decimals types.

#LISTS:-  stores multiple values of different types. Represented in []. Value stored in lists are accessed using 'INDEX'. Range for INDEX is 0-n-1.

'''list1=["Mohit",26]
print(list1)'''

#empty_list:

'''mylist=[]
print(mylist)'''

'''list1=["M","o","h","i","t"]
print(list1[0]) ''' #only integers can be used for indexing. Not decimals or fraction numbers.

#LIST_SLICING:-

'''l1=[10,13,14,16,66,64]
print(l1[1:4])'''

'''m1=["hghh",52543,"fgfggh","hhjshyg",5556.55,"ftres"]
print(m1[0:6:2])'''

'''k2=[1,2,3,4,5,6,7,8,9,10]
print(k2[2:]) ''' #has a starting point but no end hence prints whole list after 2nd term.
'''print(k2[-2:0:-1])''' #starts from index value -2 i.e 9 prints till 0 index value with the gap of -1.
'''print(k2[::-1])''' #prints the whole list in reverse.

#Python_inbuilt_functions_for_list:

'''l1=[1,56,67,88,334,88]
print(len(l1))
print(max(l1))
print(min(l1))
print(sum(l1))'''

'''a=[1,2,5]
b=[4,6,7]
print(a+b)'''
'''print(a*2)'''

'''a1=[442,6776,556,567]
b1=[442,7667,556,567]
print(40 in a1)
print(442 in a1)
print(a1 is b1)'''

'''s1=[1,2,3,4,6,8]
del s1[2]
del s1[2:5]
print(s1)'''

#list_comprehension:- is used to create a new list from the existing list.

'''a1=[12,67,45,45,66]
a1=[x+10 for x in a1]
print("List with comprehension=",a1)'''

'''print("List A=",end="")
A=[x**2 for x in range (1,11)]
print(A)'''

'''print("Only even numbers from list A=",end="")
C=[x for x in range(1,11)]
print(C[1:11:2])'''

#List_Method:-

'''l1=[1,2,3,4]
l2=[7,8,9,10]
l1.extend(l2)
print(l1)'''

'''l1=[1,2,4,6,8,9]
print(l1.index(2))
l1.insert(3,40)
print(l1)'''

#List_methods(2):-

'''a1=[1,2,3,4,5]
a1.pop(2) #removes index 2.
print(a1)
a1=[1,2,3,4,5] #removes last element by default.
a1.pop()
print(a1)
a1=[1,2,3,4,5]
a1.remove(5)
print(a1) #removes element 5 not position 5.
a1=[1,2,3,4,5]
a1.reverse() #reverses the list.
print(a1)
b1=[1,2,3,6,5,4]
b1.sort() #sorts in ascending order.
print(b1)'''

#Append_Method:

'''a1=['a','b','c']
print("a1=",a1)

a1=['a','b','c']
a1.append('x')
print("a1=",a1)

a1=['a','b','c']
a1[len(a1):]='d'
print("a1=",a1)'''

#List_methods(3):-

'''a1=['red','blue','green']
print("a1=",a1)

a1=['red','blue','green']
print("a1",a1)
result=a1.count('red')
print("red occurs ",result,"times")'''

'''a1=['red','blue','green']
a2=a1.copy()
print(a2)'''

#Practice_programs:-

'''print("all the elements in celsius value")
print("celsius=",end="")
celsius=[10,20,30,31.34,56.7]
print(celsius)
print("celsius to fahrenheit conversion")
fahrenheit=[(9)/5*x+32 for x in celsius]
print(fahrenheit)'''

#List_MIxed_value_with_type_function:-

'''print("list with mixed values:")
a1=[1,2,3.7,4,'a','b']
print(a1)
print("List with only integer elements")
a2=[x for x in a1 if type(x)==int]
print(a2)'''

#Program In List:

'''def Print_list(I):
    for n in I:
        print(n,end=" ")
I=[10,20,30,40,50]
Print_list(I)'''


                              #TUPLES:-

#Tuples are enclosed in (). Tuples are immutable or its elements can not be changed, or it is read only list.

'''t=('a','b','c','d','e')
print(t)
print(t[0])
print(t[1])
print(t[0:])
print(t[0:3])'''

'''def create_tup(*args):
    print(args)
create_tup(1,2,3,4)'''

#converting_list_into_tuple:-

'''a1=[2,6,7,8,9]
print(a1)
print(type(a1))
print()
t1=tuple(a1) #converts the list to the tuple.
print("Tuple=",t1)
print(type(t1))'''



#doubt
'''a=(1,2,3,4)
print(a[-2:0])'''

#Sorting a tuple: a tuple can be sorted only after converting it into list.

'''a1=(1,2,4,3,8,9,10)
l1=list(a1)
print(type(l1))
l1.sort()
t2=tuple(l1)
print(t2)'''



                            #DICTIONARY:-

#dictionary is collection (unordered) of key and values. Dictionary has key:value pair . Keys should be unique,but values can change. Dictionaries are enclosed in {} or curly braces.

'''phonebook={"rahul":"4556365","suraj":"5665676"}
print("the phonebook is...",phonebook)'''

#Creating_dictionary_through_function:-

'''mydict=dict() #empty dictionary
print(type(mydict))
print(mydict)'''

'''mydic=dict(Delhi=30,Banglore=45) #a Dictionary with elements can be created in this manner.
print(mydic)'''

#Method 03:-

'''d3=dict(name='mohit',age=19)
print(d3)'''

#Method 04:-


#Adding_and_replacing_values:-

'''w={'a':'9873044968','b':'9311455311'}
w['c']={'8799773685'}
print(w)
w['a']={'9999976592'}
print(w)'''

#Aliasing_In_Dictionary:-
'''d1={"up":"down","bottom":"left","top":"center"}
d2=d1
d3=d1.copy()
print(d3)
#d1 and d2 refer to same object and d3 refers to fresh copy of dictionary.
d2["bottom"]="right"
print("NEW UPDATED VALUE---",d1["bottom"])
print(d2)
#if we modify d1 and d3 are unchanged
d3["bottom"]="Incorrect"
print("New Updated Value---",d1["bottom"])
print(d1)
print(d3)'''

#
'''ascii_code={"A":65,"B":66}
print("ASCII CODE ",ascii_code)
print("asciicode keys ",ascii_code.keys())
print("ascii value ",ascii_code.values())'''

#ITEMS:
'''ascii_code={"A":65,"B":66}
print(ascii_code.items())
ascii_code.clear()
print(ascii_code)'''

#get(key):

'''temp={"hfg":445,"gygy":6565}
print(temp)
print(temp.get("hfg"))'''

                            #SETS:


#SETS:A set is a mutable data type that has unordered collection of data. Every element should be unique and every element must be immutable.


'''my_set={1,2,3}
print(my_set)
dy_set={1.0,'Mohit',(1,2,3)}
print(dy_set)

cy_set={1,2,3,3,1,4,5,6,7}
print(cy_set)

py_set=set([1,2,2,3,3,4])
print(py_set)'''

#Distinguish_between_set_and_dictionary:

'''a={}
print(type(a))

a=set()
print(type(a))'''

#Set objects dont support indexing:

'''my_set={1,2,3}
print(my_set)
my_set.add(4)
print(my_set)
my_set.update([5,6,7])
print(my_set)
my_set.discard(4)
print(my_set)
my_set.remove(6)
print(my_set)
my_set.discard(8)  #8 is in not present.
print(my_set)'''


#List and for Loops:-

'''List is equivalent to arrays with being dynamic in size.
1) Using for/while loop
2) for loop and range
3) using enumerate
4) Using List comprehension'''

'''a=[1,2,3,4]
for i in a:
    print(i)
else:
    print("Finished Looping.")'''

'''b=[1,3,6,7]
l=len(b)
for i in range(l):
    print(b[i],end="  ")'''

'''s=[2,4,6,9]
l=len(s)
i=0
while i<l:
    print(s[i])
    i+=1'''

'''l=[1,2,3,4]
[print(i) for i in l]''' #List Comprehension.

'''s=[2,4,6,9]
for i, val in enumerate(s):
    print(i,",",val)''' #enumerate_()_index will be printed as well


#Passing_as_a_Argument_to_a_function:-

'''def my_fx(random):
    for x in random:
        print(x)
cesse=['gsg','hyghg','gg']
my_fx(cesse)'''

#nested_lists:-

'''l1=[1,2,3,[4,5],6]
s1=l1[3]
element=l1[3][0]
print(l1)
print(s1)
print(element)'''

#Creating_A_Matrix :-

'''Matrix=[[2,4,6],[5,7,9],[1,3,5],[3,8,9]] #Nested Lists is equal to number of rows
rows=len(Matrix)
Columns=len(Matrix[0])
print('Matrix: ',Matrix)
for i in range(0,rows):
    print(Matrix[i])
print('Elements on row 2 and column 1: ',Matrix[1][0])
print('Elements on row 3 and column 2: ',Matrix[2][1])'''


#Tuples_As_Return_Values:

#A Function can only return only 1 value but if the value is a tuple, the effect is the same as returning multiple values.

'''def f():
    s="gnn"
    x=20
    return(s,x);
s,x=f() #Assign_Returned_tuple
print(s)
print(x)
print(type(f()))'''

'''def min_max(l):
    return min(l),max(l)
a=(1,2,3,4)
b=min_max(a)
print(b)
print(type(b))'''


#SPARSE_MATRICES :-

#If most of elements of matrix have a 0 value then it is called a sparse matrix otherwise it is called a dense matrix. Benefits of sparse matrix:

#Creating_A_Sparse_Matrix: We have to use a python library.

















































































































