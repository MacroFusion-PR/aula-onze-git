'''
n1=10
n2=20
tx1="texto1"
tx2="texto2"

print (n1 * 5 == n2)
print (tx1==tx2)

print(n1!=n2)
print (tx1!=tx2)

print(n1>n2)
print(tx1>tx2)

print(n1<n2)
print(tx1<tx2),

print(n1<=n2)
print(tx1<=tx2)

print(n1>=n2)
print(tx1>=tx2)

print("um">"dois")
print("tres">"dois")



n1=10
n2=20
n3=50

print(n1<n2!=n3)



n1=int(input())
n1=n1*2



n1=3

if n1>=6:
    print("aprovado")
elif n1>5<3:
    print("recuperação")
else:
    print("reprova")


print("\n\n\n\n")

mes=int(input("1 -- 12 = \n"))



if mes==1:
    print("\nJanuary")
elif mes==2:
    print("\nFebruary")
elif mes==3:
    print("\nMarch")
elif mes==4:
    print("\nApril")
elif mes==5:
    print("\nMay")
elif mes==6:
    print("\nJune")
elif mes==7:
    print("\nJuly")
elif mes==8:
    print("\nAugust")
elif mes==9:
    print("\nSeptember")
elif mes==10:
    print("\nOctober")
elif mes==11:
    print("\nNovember")
elif mes==12:
    print("\nDecember")
else:
    print("\nIncorrect")

  
#aula 5 

n=[1,2,3,4,5,6,7,8,9,10]

for m in range(1,11):
    if (m %2 <=0):
        print(m)

for s in "ss":
    print(s)


x=0
y=range(1,1000)
z=0

while x <100:
    x+=y[z]
    z+=24
print(x)
 elif opcao == "2"  
soma=0
x=0
while x <1000:
    x+=1
    if x%3==0:
        print(x)
        soma+=x
    else:
        if x%5==0:
            pass
        else:
            print("...")
            continue
    if soma>300:
        print(soma)
        break

while True:
    print("laço do repeater")
    print()
    opcao=input("numero random ")
    if opcao=="1":
        print("ola mundo")
    elif opcao=="2":
        print("hello")
    elif opcao=="3":
        print("break")
        break
    else:

x=0
numero= int(input("numero de 1 a 10 \n \n"))
for x in range(1,11):
    if numero >=1 and numero<=10:
        tabuada=numero*x
    print(x, "x",numero,"=",tabuada)
else:
    print("invalido")

'''

f=str(input("N= "))
n=int(input("time= "))
v=float(input("valor"))


print("funcionario Numero = ",f)
x=n*v
print("valor= ",x:.2f)
