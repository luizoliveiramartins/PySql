import pyodbc
import copy
provi=[]
connection=pyodbc.connect('DRIVER={SQL SERVER};server=localhost\shopcontrol9;database=S9_Real;uid=sa;pwd=Senha123')
sql=connection.cursor()
sql.execute('select p.codigo,p.nome,pr.preco from prod_serv as p inner join prod_serv_precos as pr on(p.ordem=pr.ordem_prod_serv) where ordem_tabela_preco=1')

for i in sql:
    c=copy.deepcopy(i.split(','))
    provi.append(c)
    print(c)

arquivo=open('c:/arquivo/sql.txt','w')

for i in provi:
    arquivo.write(str(i))
    arquivo.write(str('\n'))

arquivo.close()

sql.close()
connection.close()
