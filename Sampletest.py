#list
l1=["apple","Banana",1250,5000.23,"Kumar"]
print(l1)
l1.append("kiran")
print(l1)
l1.remove("kiran")
print(l1)
print(len(l1))
l1.reverse()
print(l1)
l1.pop(4)
print(l1)

#Tuples
t1=("Kiran",122,178.78,"Kiran",True,1234.56)
print(t1)
for t2 in t1:
    print(t2)
print(len(t1))

x=list(t1)
print(x)
x.append("John")
print(x)
y=tuple(x)
print(y)

#Sets

S1={"Kiran","Kiran","JOhn",1234.67,8989}
print(S1)
S1.add("Watson")
print(S1)

#Dictionaries

thisdict={"Name":"Kiran","Age":31,"Sex":"Male"}
print(thisdict)
print(len(thisdict))
print((thisdict.keys()))
