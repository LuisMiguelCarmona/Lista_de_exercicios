'''Exercício 4 lista 3 top de mat apl A'''
import os
def csva(x='.'):
    arquivos=os.listdir(x)
    listacsv=[]
    for csv in arquivos:
        if csv[-4:]=='.csv':#Verifica se os ultimos 4 digitos no path do arquivo são .csv!
            listacsv.append(csv)#Cria uma lista com o nome de todos os arquivos .csv
        else:
            pass
    linhasdocsv=0
    y=0
    for i in listacsv:#Pega os arquivos CSV        
        arquivo=open(i,'r')
        q=arquivo.read() #Lê os arquivos, formando uma grande string com as palavras dele.        
        x=q.count('\n') #Conta o numero de linhas do arquivo.        
        linhasdocsv+=x #Soma o numero de linhas no total.
        n=q.split('\n')[4]#seleciona uma linha aleatória para contar o numero de colunas, depois de ter separado todas as linhas do programa (O que deve ser muito ineficiente, mas eu não sei como fazer sem ser assim)
        z=n.split(';')#Separa os campos de uma linha.
        y+=len(z)#O numero de colunas é igual a quantidade de campos que foram separados no exemplo interior.
    c='Os arquivos tem: '+str(x - 1)+' linhas no total, e '+str(y)+' colunas unicas.'   
    return c
