#question 1
print("<--------------solution 1------------------>")

year=int(input("enter the year"))
if(year%4==0):
    print("leap year")
else:
    print("not a leap year")

#question 2
print("<--------------solution 2------------------>")

l=int(input("enter the length"))
b=int(input("enter the breadth"))
if(l==b):
    print("dimensions are of square")
else:
    print("dimensions are of rectangle")

#question 3
print("<--------------solution 3------------------>")

a=int(input("enter the age of person 1 "))
b=int(input("enter the age of person 2 "))
c=int(input("enter the age of person 3 "))
if(a<b and a<c):
    print("a is youngest")
elif(b<a and b<c):
    print("b is youngest")
else:
    print("c is youngest")
if(a>b and a>c):
    print("a is oldest")
elif(b>a and b>c):
    print("b is oldest")
else:
    print("c is oldest")


#question 4
print("<--------------solution 4------------------>")

age=int(input("enter the age"))
sex=input("enter sex(M or F) ")
ms=input("enter marital status(Y or N) ")
if(sex=='F' or sex=='f'):
    print("She will work only in urban areas")
elif(sex=='M' or sex=='m'and age >=20 and age <=40):
    print("He may work in anywhere ")
elif(sex=='M' or sex=='m' and age>40 and age<=60):
    print("He will work in urban areas only.")
else:
    print("ERROR")

#question 5
print("<--------------solution 5------------------>")

q=int(input("enter quantity"))
if(q>1000):
    cost=q*100
    dis=cost*0.10
    tcost=cost-dis
    print(tcost)
else:
    tcost=q*100
    print(tcost)

#question 6
print("<--------------solution 6------------------>")

l=[]
for i in range (10):
   num=int(input("enter number "))
   l.append(num)
print(l)

#question 7
print("<--------------solution 7------------------>")

while True:
    print("infinte")

#question 8
print("<--------------solution 8------------------>")

l1=[]
l2=[]
n=int(input("enter the number of elements in a list"))
for i in range (n):
    num=int(input("enter number "))
    l1.append(num)
    l2.append(num*num)
print(l2)

#question 9
print("<--------------solution 9------------------>")


list=[1,2,"prikshit",12,"singla",3,4,55,1.23,0.112,98.8976]
list_int=[]
list_str=[]
list_float=[]
for i in list:
    if(isinstance(i,int)):
        list_int.append(i)
    elif(isinstance(i,str)):
         list_str.append(i)
    elif(isinstance(i,float)):
         list_float.append(i)
print(list_int)
print(list_str)
print(list_float)



#question 10
print("<--------------solution 10------------------>")

l3=[]
for i in range(1,101):
    count=0
    for j in range(2, int(i/2)) :
        if(i%j==0):
            count+=1
    if(count==0):
        l3.append(i)
print(l3)

#question 11
print("<--------------solution 11------------------>")

for i in range (0,4):
      for j in range (0,i+1):
          print("*" , end="")
      print()


#question 12
print("<--------------solution 12------------------>")

list=[]

for i in range (1,11):
    num=int(input("Enter Elements :- "))
    list.append(num)
print("List Before Deletion\n",list)
x=int(input("Enter Element to be Searched and deleted :- "))
for i in list:
    if(x==i):
        list.remove(i)
else:
    print("List after Deletion\n",list)
