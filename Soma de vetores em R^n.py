'''
Este programa define uma fun��o com objetivo de somar 2 vetores de em R^N.
por favor, aprova isso mestre eu passei literalmente 6 horas tentando debugar um erro e at� agora eu n�o sei pq diabos isso estava bugando �<_`
Ele foi feito por Ruan felipe da silva e sousa.
DRE do aluno:119041454.
Vet utiliza um parametro (numero inteiro) para numerar o vetor.
sumvet n�o tem parametros, questiona o usuario quanto aos vetores que ele deseja somar e retorna o vetor resultado.
'''
def vet(a):
    d=[]
    z=0
    i=0
    k='VAISEFUDERPROGRAMABURRO'    
    while z < 10:       
        i+=1
        if i==1:
            x=input('Digite a valor da coordenada do vetor '+str(a)+' na '+str(i)+'� dimens�o. Caso o vetor '+str(a)+' n�o se expanda mais em nenhuma dimens�es al�m destas, digite a letra k como resposta para interromper o loop: ')
            if type(x)== str and type(k)== str:
                break
            else:
                d.append(float(x))
        if i!=1:
            x=input('Digite a valor da coordenada do vetor '+str(a)+' na '+str(i)+'� dimens�o: ')            
            if type(x)== str and type(k)== str:
                break
            else:
                d.append(float(x))
    return d    
def sumvet():
    a=vet(1)
    b=vet(2)
    teta=len(a)
    c=[]
    while len(a)<len(b):
        a.append(float(0))
    while len(b)<len(a):    
        b.append(float(0))
    for q in range(teta):
        alpha=a[q]
        beta=b[q]
        gamma=alpha+beta
        delta=float(gamma)
        c.append(delta)
    print('O vetor resultado vale:')
    print(c)    

            
