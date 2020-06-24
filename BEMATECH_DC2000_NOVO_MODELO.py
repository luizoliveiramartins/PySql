import pyodbc
import copy
import os
caminho = ('c:/inventario')
cont=0

if not os.path.exists(caminho):
    os.makedirs(caminho)

connection=pyodbc.connect('DRIVER={SQL SERVER};server=localhost\shopcontrol9;database=s9_real;uid=sa;pwd=Senha123')
sql=connection.cursor()

arquivo=open('c:/inventario/Upload_Data.txt','r')
lista=[]
esquerda=[]
direita=[]

for a in arquivo:
    lista.append(a)


filial=int(input('Filial: '))
numero=int(input('Qual Número Da Contagem? '))

for l in lista:
    c=copy.deepcopy(l.split(';'))
    esquerda.append(c[0])
    direita.append(int(c[1]))
    
sql.execute('select p.codigo,p.codigo_barras from prod_serv as p inner join Contagem_Estoque_Itens as i on(p.ordem=i.ordem_prod_serv) inner join Contagem_Estoque as c on (c.ordem=i.Ordem_Contagem) inner join filiais as f on (f.ordem=c.ordem_filial)where c.Numero=? and f.Codigo=?',numero,filial)
data=sql.fetchall()

for s in data:
    for e in esquerda:
        if s[0]==e or s[1]==e:
            pos=direita[esquerda.index(e)]
            #print(s,pos)
            sql.execute('update contagem_estoque_itens set qtde_digitada=? from contagem_estoque_itens as i inner join contagem_estoque as c on (c.ordem=i.ordem_contagem) inner join prod_serv as p on (p.ordem=i.ordem_prod_serv) inner join filiais as f on(f.ordem=c.ordem_filial) where p.codigo=? and c.numero=? and f.codigo=?',pos,s[0],numero,filial)
            connection.commit()
sql.close()
arquivo.close()
