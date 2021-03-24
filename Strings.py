st1="Hello \n \"python\""

print(st1)

st2 ="This is the python world"

print(len(st2))

print(st2.upper())
print(st2.lower())

print(st2[-1::1])
revs=reversed(st2)
print("".join(revs))

st3 = "kiran kumar"
st4=list(st3.split(" "))


def my_string(x):
    return x[::-1]
string=my_string("kiran kumar")
print(string)

s=" this python program"
def loppstring(s):
    str=""
    for i in s:
        str=i+str
    return str
print(loppstring(s))

st5="venkata kumar"
st7=st5[0:8]
print(st7)
st8=st5[8:14]
rev1=reversed(st8)
rev2="".join(rev1)
print(st7+" "+rev2)
#method1
list=["kiran","kumar","venkata"]
l1=list.reverse()
print(list)
#method 2

reversed_list=list[::-1]
#method 3
print(reversed_list)
list1=["kiran","kumar","venkata"]
for rev in reversed(list1):
    print(rev)


