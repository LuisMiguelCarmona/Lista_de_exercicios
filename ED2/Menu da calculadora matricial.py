import os

def menu():
    '''Menu inicial da calculadora matricial'''
    q='''
          _______ _______        _______ _     _        _______ ______   _____   ______ _______      _______ _______ _______  ______ _____ _______ _____ _______                
 ___      |       |_____| |      |       |     | |      |_____| |     \ |     | |_____/ |_____|      |  |  | |_____|    |    |_____/   |   |         |   |_____| |           ___
          |_____  |     | |_____ |_____  |_____| |_____ |     | |_____/ |_____| |    \_ |     |      |  |  | |     |    |    |    \_ __|__ |_____  __|__ |     | |_____         
     Informe o que você deseja fazer: (Recomenda-se ao iniciar pela primeira vez ir na primeira opção para definir uma matriz, já que a lista começa vazia)
     1 - Manipular lista de matrizes
     2 - realizar operações com matrizes
     3 - alterar configurações do programa
     '''
    z = input(q)
    if z == '1':
        return manlist()
    if z == '2':
        return opmatriz()
    if z == '3':
        return altconfig()

def manlist():
    '''Lista usada para manipular as matrizes'''
    z=0
    if not os.path.exists('./matrizes'):
        os.makedirs('./matrizes')
    if not os.path.exists('./matrizes/backup'):
        os.makedirs('./matrizes/backup')    
    arquivos = os.listdir("."+'/matrizes')
    rmarquivos=[]
    for i in arquivos:
        if i[-4:] != '.txt' : 
            rmarquivos.append(i)
        else:
            pass
    for i in rmarquivos:
        arquivos.pop(arquivos.index(i))
    if arquivos == []:
        print('1 - Criar uma nova matriz')
        print('2 - Ler backup (Acrescentar ou substituir)')
        print('3 - Inserir matriz identidade NxN')
        q=input('\nO que você deseja fazer? ')
        if q == '1':
              return criar_matriz()
        if q == '2':
              return ler_backup()
        if q == '3':
              return identidade()           
    print('Matrizes disponíveis para a visualização:')    
    for i in arquivos:
        c=str(arquivos.index(i)+1)+' - '+i
        print(c[:-4])
        z=arquivos.index(i)+1
    print('~ Outras opções ~')
    print(str(z+1)+' - Criar uma nova matriz')
    print(str(z+2)+' - Deletar matriz da lista')
    print(str(z+3)+' - Fazer backup da lista atual')
    print(str(z+4)+' - Zerar a lista de matriz')
    print(str(z+5)+' - Ler backup (Acrescentar ou substituir)')
    print(str(z+6)+' - Inserir matriz identidade NxN')
    c=input('\nO que você deseja fazer?: ')    
    if c==str(z+1):
        return criar_matriz()
    if c==str(z+2):
        print('Matrizes disponíveis para remoção:')    
        for i in arquivos:
            c=str(arquivos.index(i)+1)+' - '+i
            print(c[:-4])
        c=input('\nQual matriz você deseja remover?: ')   
        try:
            x=[arquivos[arquivos.index(c)]]
            return limpar_lista(x)
        except:
            print('\n Por favor, selecione um valor dentro da lista')
            return manlist()        
    if c==str(z+3):             
        return backup_matriz(arquivos)
    if c==str(z+4):
        return limpar_lista(arquivos)
    if c==str(z+5):
        return ler_backup()
    if c==str(z+6):
        return identidade()
    return alterar_matriz(arquivos[int(c)-1])     

def backup_matriz(a):    
    '''Recebe uma lista com os nomes de matrizes, e então faz backup dessas matrizes em uma pasta'''
    u=input('Digite o nome do backup que você deseja fazer:   ')
    xy=input('Você deseja deletar os arquivos originais? y/n: ')
    if not os.path.exists('./matrizes/backup/'+u):
        os.makedirs('./matrizes/backup/'+u)
    for i in a:
        x=open('./matrizes/'+i,'r')
        z=x.read()
        q=open('./matrizes/backup/'+u+'/'+i,'w')
        q.write(z)
        x.close()
        q.close()
    if xy == 'y':
        for i in a:
            os.remove('./matrizes/'+i)
        print('\nArquivos removidos com sucesso\n')        
    print('\n Backup realizado com sucesso!\n')        
    return menu()

def limpar_lista(a):
    ''' Recebe uma lista de matrizes, e remove elas da pasta de arquivos.'''
    arquivos = os.listdir("."+'/matrizes')
    rmarquivos=[]
    for i in arquivos:
        if i[-4:] != '.txt' : 
            rmarquivos.append(i)
        else:
            pass
    for i in rmarquivos:
        arquivos.pop(arquivos.index(i))
        
    if arquivos == []:
        print('A lista já está vazia.')
        return menu()    
    p=input('Você tem certeza que deseja fazer isso? y/n: ')    
    if p=='y':
        for i in a:
            os.remove('./matrizes/'+i)    
        print('\nArquivo removidos com sucesso com sucesso.\n')
        return menu()
    else:
        return manlist()
    
def ler_backup():
    '''Abre o backup feito na pasta'''
    arquivos = os.listdir("."+'/matrizes/backup')  
    if arquivos == []:
        print('Não parecem haver backups para serem lidos.')
        return manlist()
    print('Backups disponíveis para leitura: ')    
    for i in arquivos:
        c=str(arquivos.index(i)+1)+' - '+i
        print(c)
    c=input('Qual dos backups você deseja que seja lido?: ')
    p=input('Você deseja substituir em vez de adicionar a lista atual? y/n : ')
    if p == 'y':
        arquipos= os.listdir('./matrizes')
        limpar_lista(arquipos)
    try:
        arquivos = os.listdir('./matrizes/backup'+arquivos[c-1])
        for i in arquivos:
            x=open('./matrizes/backup/'+i,"r")            
            z=x.read().split('\n')
            p=open('./matrizes/'+i,'w')
            p.write(z)
            x.close()
            p.close()
        return manlist()
    except: #caso algo dê errado, a função vai executar esse bloco de código.
        print('Por favor, digite um numero.válido \n')
        return ler_backup()
    
def ver_matriz(a):
    '''Printa uma matriz recebida, perguntando se o ususario deseja alterar ela'''
    z=open('./matrizes/'+a,'r')
    x=z.read()
    print(x)
    x=x.split('\n')
    q=input('Você deseja fazer alguma alteração a essa matriz? y/n: ')
    if q == 'y':
        return alterar_matriz(x)
    else:
        return manlist()
    
def alterar_matriz(x):    
    '''Recebe uma matriz e altera ela'''
    p=input('Você deseja fazer uma alteração a qual linha?   ')
    if p>len(x):
        print('Por favor, selecione uma linha válida.')
        return alterar_matriz(x)
    y=input('Você deseja fazer uma alteração a qual elemento?  ')
    if y>len(x[1]):
        print('Por favor, selecione uma coluna válida ')
        return alterar_matriz(x)
    c=input('Defina o novo valor do elemento: ')
    x[p][y]=int(c)
    q=input('Você deseja realizar mais alguma alteração? y/n:  ')
    if q == 'y':
        return alterar_matriz(x)
    return manlist()

def salvarmatriz(a):
    b=input('Digite o nome da matriz que você deseja salvar: ')#Capta o nome da matriz
    if b == '':
        print('\nPor favor, dê um nome a sua matriz.\n')
        return salvarmatriz(a)
    x=open('./matrizes/'+b+'.txt','w')#Comando informando ao python que vamos criar/nomear um objeto
    try:
        for i in a:#a é uma lista, e portanto, vamos salvar cada "linha" dentro dela separadamente.
            x.write(i)#Escreve os elementos de a no arquivo.
        x.close()#Fecha o objeto que abrimos, encerrando a função
        return
    except:
        print('A matriz para ser salva está com algum problema. Por favor, tente novamente.\n')
        
def lermatriz():
    arquivos = os.listdir("."+'/matrizes')#lê todos os arquivos contidos onde o programa está.
    rmarquivos=[]
    for i in arquivos:
        if i[-4:] != '.txt' : 
            rmarquivos.append(i)#Salva o nome de todos os arquivos que NÃO são .txt
        else:
            pass
    for i in rmarquivos:
        arquivos.pop(arquivos.index(i))#Remove os arquivos que não são .txt

    if arquivos == []:
        print('Não parecem haver matrizes para serem lidas.')
        return
    print('Matrizes disponíveis para a leitura:')    
    for i in arquivos:
        c=str(arquivos.index(i)+1)+' - '+i
        print(c[:-4]) #Printa uma lista com todos os arquivos.
    c=input('Qual das matrizes você deseja que seja lida?: ')
    try:
        x=open('.'+str('/matrizes/'+arquivos[int(c)-1]),"r")
        z=x.read().split('\n')#lê a matriz de dentro da pasta.
        x.close()#fecha o que abrimos.
        return z #a matriz que desejamos está ai.
    except: #caso algo dê errado, a função vai executar esse bloco de código.
        print('Por favor, digite um numero.\n')
        return lermatriz()
