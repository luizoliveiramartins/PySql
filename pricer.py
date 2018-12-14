import pyodbc
import os
caminho = ('c:/arquivo/DELETE-ME')
 
if not os.path.exists(caminho):
    os.makedirs(caminho)

lista1=[]
lista2=[]
lista3=[]
lista4=[]
lista5=[]
lista6=[]

cod1='0001'
cod2='7 0'
cod3='23 0'
cod4='121 0'
normal='NORMAL'
cod5='200 0'
otugui='OTUGUI'
a='|'

connection = pyodbc.connect('DRIVER={SQL Server};server=localhost\shopcontrol9;database=S9_Real;uid=sa;pwd=Senha123')
sql=connection.cursor()
sql.execute('SELECT P.CODIGO,P.NOME,PR.PRECO FROM PROD_SERV AS P INNER JOIN PROD_SERV_PRECOS AS PR ON(P.ORDEM=PR.ORDEM_PROD_SERV)WHERE ORDEM_TABELA_PRECO=1')
data=sql.fetchall()


for i in data:
    zero='{:0>8}'.format(i[0])
    pre=str(i[2]).replace('.','')
    resultado=cod1,zero,cod2,a+str(i[1])+a,cod3,a+pre[:len(pre)-2]+a,cod4,a+str(normal)+a,cod5,a+str(otugui)+a
    troca=resultado[9].replace("|OTUGUI|","|OTUGUI|,")
    resu=resultado[0],resultado[1],resultado[2],resultado[3],resultado[4],resultado[5],resultado[6],resultado[7],resultado[8],troca
    lista1.append(resu)
arquivo=open('c:/arquivo/DELETE-ME/DELETE-ME.txt','w')

for i in lista1:
    arquivo.write(str(i))
    arquivo.write(str('\n'))

arquivo.close()

arquivo1=open('c:/arquivo/DELETE-ME/DELETE-ME.txt','r')

for i in arquivo1:
    troca1=i.replace("(","")
    lista2.append(troca1)

arquivo1.close()

for i in lista2:
    troca2=i.replace(")","")
    lista3.append(troca2)

for i in lista3:
    troca3=i.replace("'","")
    lista4.append(troca3)

for i in lista4:
    troca4=i.replace(",","")
    lista5.append(troca4)

for i in lista5:
    troca5=i.replace("|OTUGUI|","|OTUGUI|,")
    lista6.append(troca5)
del lista1
del lista2
del lista3
del lista4
del lista5

arquivo_novo=open('c:/arquivo/PRICER.txt','w')

for i in lista6:
    arquivo_novo.write(str(i))
arquivo_novo.close()
