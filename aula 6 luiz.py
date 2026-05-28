'''
def filme(x):
    print("meu filme favorito é",x)

x="Senhor dos Anéis"
filme(x)


def velocidade(tempo, distancia=1000):
    print(distancia/tempo)

velocidade(25)



def menor(a, b):
    if a>=b:
        return a
    else:
        return b
    
a=99
b=5
print("o menor valor entre ",a,"e", b,"é",menor(a,b))



def acai(*ingredientes, tamanho="Sem Nada"):
    print("\n Preparando um Açaí", tamanho, "com os seguintes ingredientes;")
    for ingredientes in ingredientes:
        print(" - ", ingredientes)
acai("banana","granola")
acai("morango","kiwi","leite em pó", tamanho="grande")
acai("banana", tamanho="pequeno")
acai("Nada ")



def menor(lista):
    menorvalor=lista[0]
    for x in lista:
        if (x<menorvalor):
            menorvalor=x
    return menorvalor
def maior(lista):
    maiorvalor=lista[0]
    for x in lista:
        if (x>maiorvalor):
            maiorvalor=x
    return maiorvalor

def maioremenor(lista):
    print("maior:",maior(lista))
    print("menor:",menor(lista))

maioremenor([1,2,3,45,6,7,8,8,9,9,8,7,6,55,4,3,3,2,])

'''

def dobralençol(lençol, gaveta):
    if (lençol<gaveta):
        return 0
    else:
        return+dobralençol(lençol/2, gaveta)
print(dobralençol(200,25))