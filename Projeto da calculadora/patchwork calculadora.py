import math
x=3 #tamanho comum do vetor. Utilizar isso em while loops,e alterar utilizando as opções.
z=2 #Numero que indica se o programa guarda o resultado da ultima conta ou não. (1 = ligado, 2 = desligado, 3 = guarda o resultado da ultima conta e soma ao resultado anterior.)
resultadof='' #Variavel global que armazena o resultado da ultima conta, e utiliza para realizar outras operações.

def menu():
     s=str(input(
         '''
              _________        .__               .__              .___                                  __               .__       .__             
          \_   ___ \_____  |  |   ____  __ __|  | _____     __| _/________________    ___  __ _____/  |_  ___________|__|____  |  |            
  ______  /    \  \/\__  \ |  | _/ ___\|  |  \  | \__  \   / __ |/  _ \_  __ \__  \   \  \/ // __ \   __\/  _ \_  __ \  \__  \ |  |     ______ 
 /_____/  \     \____/ __ \|  |_\  \___|  |  /  |__/ __ \_/ /_/ (  <_> )  | \// __ \_  \   /\  ___/|  | (  <_> )  | \/  |/ __ \|  |__  /_____/ 
           \______  (____  /____/\___  >____/|____(____  /\____ |\____/|__|  (____  /   \_/  \___  >__|  \____/|__|  |__(____  /____/          
                  \/     \/          \/                \/      \/                 \/             \/                          \/                
    Bem vindo a calculadora vetorial! Escolha uma opção para continuar, ou digite SAIR para sair!
    1) Operações vetoriais 
    2) Configurações da calculadora '''))
     
    if type(s)== type(''):
        s=str.lower(s)
        
    if s not in ['2','1','sair']:
        print('\nOpção inválida, tente novamente.')
        menu() # Recursão para reiniciar o programa.
        
    if s == '1':        
        opv()
        
    if s == '2':
        opc()
        
    if s == 'sair':
        print('Programa encerrando.')
        return


''' Função Criar vetor - Essa função utiliza uma parametro N para criar um vetor de N coordenadas.
O resultado é uma lista.'''
def cvec1(x):
    l=[]
    p=1
    while p != x:
          p+=1
          l.append(int(input('Digite o valor da '+str(X)+'° coordenada do 1° vetor.')))
    return l       
def cvec2(x):
    c=[]
    p=1
    while p != x:
          p+=1
          l.append(int(input('Digite o valor da '+str(X)+'° coordenada do 2° vetor.')))
    return c

'''Menu de configurações da calculadora. '''
def opc():
    #Menu de configuração das calculadoras.
    opc=input('~~Configuração da calculadora~~ \n1) Alterar a dimensão padrão dos vetores \n2) Memorizar resultados anteriores \n3) Acumular resultado vetorial')
    if opc not in ['1','2','3']:
        print('\nOpção invalida, tente novamente.')
        opc()# Recursão para reinciar o programa.
    if opc == '1':
        p=input('\nDefina o tamanho padrão dos vetores: \n')
        global x
        x=p
        menu()
    if opc == '2':
        if z == 1:
            print('\nMemorização de resultados anteriores desligada.')
            global z
            z = 2
            menu()
        if z == 2:
            print('\nMemorização de resultados anteriores ligada.')
            global z
            z = 1
            menu()
        else:
            print('\nMemorização de resultados anteriores ligada, e acumulo vetorial desligado.')
            global z
            z = 1
            menu()               
    if opc == '3':
            print('\nAcumulo de resultado vetorial ligado, junto com memorização de resultados anteriores.')
            global z
            z=3
            menu()    

'''Módulo das operações''' 

def escmult():     #Multiplica um vetor por um numero escalar qualquer
     if resultadof != '':
          if type(resultadof)=type([]):
               z=resultadof
               c=int(input(Defina aqui o numero pelo qual você deseja multiplicar o vetor: ))
               for i in z:
                    z[i]*=c
               return z
          else:
               z=cvec1(N)
               c=resultadof
               for i in z:
                    z[i]*=c
               return z   
     else:          
          z=cvec1(N)
          c=int(input(Defina aqui o numero pelo qual você deseja multiplicar o vetor: ))
          for i in z:
               z[i]*=c
          return z

def prodint(z1,z2): #Calcula o produto interno entre 2 vetores.   
    z3=[]
    resul=0    
    for i in range(N):
        z3[i]=z1[i]*z2[i]
        resul+=z3[i]
    return resul

def sumvet(): #Calcula a soma vetorial de 2 vetores
     zr=[]
     if resultadof != '' and z==1:
          if type(resultadof)==type([]):
               z1=resultadof
               z2=cvec2(N)
               for i in range(N):
                    zr[i]=z1[i]+z2[i]
               return zr
          else:
               print('Não podemos realizar soma vetorial com um valor escalar.')
               menu()          
     else:
          z1=cvec1(N)
          z2=cvec2(N)    
          for i in range(N):
               zr[i]=z1[i]+z2[i]
          return zr       
def modvet(z1): #Calcula o módulo de 1 vetor.
     p=0
     if resultadof != '' and z==1:
          if type(resultadof)==type([]):
               z2=resultadof
               for i in range(N):
                    z2[i]=z2[i]**2
                    p+=z2[i]
                    return math.sqrt(p)
          else:
               return resultadof
     else:          
          for i in range(N):
               z1[i]=z1[i]**2
               p+=z1[i]
               return math.sqrt(p)
     

def angevet():#Calcula o angulo entre 2 vetores,e retorna em radianos.
     if resultadof != '' and z==1:
          if type(resultadof)==type([]):
               z1=resultadof
               z2=cvec2(N)
               p=prodint(z1,z2)
               q=modvet(z1)+modvet(z2)
               teta= math.acos(p/q)
               return teta
          else:
               z1=[0]*N
               z1[0]=resultadof               
               z2=cvec2(N)
               p=prodint(z1,z2)
               q=modvet(z1)+modvet(z2)
               teta= math.acos(p/q)
               return teta
     else:
          z1=cvec1(N)
          z2=cvec2(N)
          p=prodint(z1,z2)
          q=modvet(z1)+modvet(z2)
          teta= math.acos(p/q)
          return teta

def disvet():#calcula a distância entre 2 vetores.
     z3=[]
     r=0
     if resultadof != '' and z==1:
          if type(resultadof)==type([]):
               z1=resultadof
               z2=cvec2(N)               
               for i in range(N):
                    z3[i]=z1[i]-z2[i]
                    z3[i]=z3[i]**2
                    r+=z3[i]
               return math.sqrt(r)
          else:
               z1=[0]*N
               z1[0]=resultadof
               z2=cvec2(N)
               z3=[]
               r=0
               for i in range(N):
                    z3[i]=z1[i]-z2[i]
                    z3[i]=z3[i]**2
                    r+=z3[i]         
               return math.sqrt(r)
     else:
          z1=cvec1(N)
          z2=cvec2(N)          
          for i in range(N):
               z3[i]=z1[i]-z2[i]
               z3[i]=z3[i]**2
               r+=z3[i]
               return math.sqrt(r)
          
def comblin(): #realiza a combinação linear de 2 vetores:
     z3=[]
     if resultadof != '' and z==1:
          if type(resultadof)==type([]):
               z1=resultadof
               z2=cvec2(N)
               for i in range(N):
                    z3[i]=z1[i]*z2[i]
               return z3
          else:               
               z1=[0]*N
               z1[0]=resultadof
               z2=cvec2(N)
               for i in range(N):
                    z3[i]=z1[i]*z2[i]
               return z3
     else:
          z1=cvec1(N)
          z2=cvec2(N)
          for i in range(N):
               z3[i]=z1[i]*z2[i]
          return z3    
    
def opv():
    opv=input('''
~~Operações vetoriais~~
1) Soma vetorial
2) Multiplicação de vetor por numero escalar
3) Combinação linear de 2 vetores
4) Norma Vetorial
5) Produto interno
6) Angulo entre os vetores''')
    
    if opv == 1:
     q=sumvet()
     print('O resultado da operação é: '+str(q))
     global resultadof
     resultadof=q
     menu() 
     
    if opv == 2:     
     q=escmult()
     print('O resultado da operação é: '+str(q))
     global resultadof     
     resultadof=q
     menu()  
    
    if opv == 3:          
     q=comblin()
     print('O resultado da operação é: '+str(q))
     global resultadof
     resultadof=q
     menu()
          
    if opv == 4:
     z1=cvec1(N)
     q=normvet(z1)
     print('O resultado da operação é: '+str(q))
     global resultadof
     resultadof=q
     menu()
     
    if opv == 5:     
     if resultadof!='' and z1==1:
          if type(resultadof)==type([]):
               z1=resultadof
               z2=cvec2(N)
               q=prodint(z1,z2)
               global resultadof
               resultadof=q
               print('O resultado da operação é: '+str(q))
               menu()
          else:
               z1=[0]*N
               z1[0]=resultadof
               z2=cvec2(N)
               q=prodint(z1,z2)
               global resultadof
               resultadof=q
               print('O resultado da operação é: '+str(q))
               menu()
     else:
          z1=cvec1()
          z2=cvec2()
          q=prodint(z1,z2)
          global resultadof
          resultadof=q
          print('O resultado da operação é'+str(q))
          menu()                
    if opv == 6:
     q=angevet()
     print('O resultado da operação é: '+str(q))
     global resultadof
     resultadof=q
     menu()        

        