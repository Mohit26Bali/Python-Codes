Python Project To Display change in rank of student after updation in Marks :

Names = ["Mohan","Rahul","Rohan"]#Names
print(type(Names))
print("Names : ",Names)
Marks = [87,76,67]#Marks
print(type(Marks))
print("Marks : ",Marks)
dict1 = dict(zip(Names,Marks)) #Zip function returns an zip object(in tuple) where 1st item is paired with 1st item of other Value and Dict conveerts it into dictionary.
m1 = sorted(Marks) #Sorted_Marks.

r1 = []
for i in range(len(m1)):
    r = len(m1)-i
    r1.append(r)
d2 = dict(zip(m1,r1))
l1 = []
for i in d2:
    l = (list(dict1.keys())[list(dict1.values()).index(i)],d2[i])
    l1.append(l)
rankinorder = (l1[::-1])
sr = dict(sorted(rankinorder))
for i,j in rankinorder:
    print("Name : ",i,"","Rank : ",j)
Update = [1,20,31]             #Updates
print(type(Update))
print("Marks To Be Updated By : ",Update)
ml = list(zip(Marks,Update))
UpdatedMarks = []
for i,j in ml:
    UpdatedMarks.append(i+j)

dicr = dict(zip(Names,UpdatedMarks))
m2 = sorted(UpdatedMarks)
print("Updated Marks :  ",UpdatedMarks)

r2 = []
for i in range(len(UpdatedMarks)):
    r = len(UpdatedMarks)-i
    r2.append(r)
d3 = dict(zip(UpdatedMarks,r2))
l2 = []
for i in d3:
    l5 = (list(dicr.keys())[list(dicr.values()).index(i)],d3[i])
    l2.append(l5)
rankinorde = (l2[::-1])
st = dict(sorted(rankinorde))
for i in sr:
    print("Name : ",i,"Rank : ",st[i],"Jump : ",abs(st[i]-sr[i]))
 

    
    














    

