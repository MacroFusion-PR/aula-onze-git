'''
t=('a','b','c',1,2,3)
print (t[2])
print(len(t))
print(t.index(1))
print (t.count("a"))

x=set()
x.add(1)
x.add(2)
print(x)

a=True
b=False
c=1>2
d=2>1
e=None

print(a,b,c,d,e)


dicio={"a":123,"b":[1,2,3],"c":["um","dois","tres"]}
dicio["d"]="x,y,z"
print(dicio.keys())
print(dicio.values())
print(dicio.items())
print(dicio["d"])


sor=(1,3,2,3,4,5,1,5,7,6,8,3,4)
sor=set(sor)
sot=sorted(sor)
print(sot)
'''

dic={61:"Brasucas",
     71:"Salvador",
     11:"São paulo",
     21:"Rio de chamito",
     32:"Juiz de dentro",
     19:"Campinas",
     27:"Derrota",
     31:"Belo horizonte"}

while True:
 ddd=int(input("DDD "))

 if ddd in dic:
    print(dic[ddd])
 else:
   print("DDD não cadastrado")