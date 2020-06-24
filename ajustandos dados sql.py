import pyodbc
comparar=[]
nome=[]
connection=pyodbc.connect('DRIVER={SQL SERVER};server=localhost\sqlexpress;database=projeto;uid=sa;pwd=Senha123')
sql=connection.cursor()

sql.execute('SELECT * FROM CLIENTE')
data=sql.fetchall()


for d in data:
    nome.append(d[1])
    comparar.append(d[1])
    for c in comparar:
        if d[1]==c:
            pos=nome[comparar.index(c)]
            sql.execute('UPDATE CLIENTE SET NOME=? \
            WHERE NOME=?',pos.title(),d[1])
            connection.commit()
sql.close()

print('Dados ajustados')
quit()
