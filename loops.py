nums=range(1,10,1)

for n in nums:
    if(n<5):
     #   print(n)
        continue
    else:
        break

x=0
while x<5:
    print(x)
    x+=1
       

student={
    "name":"Avil",
    "Age":29,
    "Address":"Bangalore"
}

print(student["name"])

#handling error
try:
    student["last_name"]
except KeyError:
    print("wrong key!")

try:
    a="A"+2
except TypeError:
    print("Type Error cannot print")

try:
    last_name=student["last_name"]
    l2=last_name+2
except KeyError:
    print("wrong key!")

#Set datatype
mySet=set([1,1,2,2,3,3])
print(mySet)