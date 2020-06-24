import pyodbc
connection = pyodbc.connect('DRIVER={SQL Server};server=localhost\shopcontrol9;database=projeto;uid=sa;pwd=Senha123')
sql=connection.cursor()


def menu():
    print('')
    print('1- Cadastrar: ')
    print('2- Listar: ')
    print('3- Buscar: ')
    print('4- Sair: ')
    op=int(input('Escolha a opção: '))
    return op

def inserir():
    Name=input('Nome: ')
    Tel=input('Telefone: ')
    while True:
        Mail=input('e-mail: ')
        if '@' not in Mail:
            print('Email inválido.')
            continue
        else:
            break
    Ende=input('Endereço: ')
    Num=int(input('Número: '))
    Cep=input('CEP: ')
    Cidade=input('Cidade: ')
    Estado=input('Estado: ')
    sql.execute("insert into cliente values (?,?,?,?,?,?,?,?)",(Name.title(),Tel,Mail,Ende.title(),Num,Cep,Cidade.title(),Estado.upper()))
    connection.commit()

def buscar():
    buscar=input('Quem deseja buscar? ')
    sql.execute("select * from cliente where nome like'%'+?+'%'",buscar)
    for s in sql:
        print('\n CADASTRO')
        print(s)

def listar():
    sql.execute('select * from cliente')
    for i in sql:
        print(i)

while True:
    op=menu()
    if op==4:
        break
    elif op==1:
        inserir()
    elif op==2:
        listar()
    elif op==3:
        buscar()
sql.close()
connection.close()
