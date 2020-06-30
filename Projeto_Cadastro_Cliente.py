import PySimpleGUI as tela
import pyodbc
connection = pyodbc.connect('DRIVER={SQL Server};server=localhost\sqlexpress;database=CADASTRO;uid=sa;pwd=Senha123')
sql=connection.cursor()

layout=[
    [tela.Text('Nome',size=(7,0)),tela.Input(),tela.Text('Endereço',size=(7,0)),tela.Input()],
    [tela.Text('Número',size=(7,0)),tela.Input(size=(10,0)),tela.Text('Telefone',size=(7,0)),tela.Input(size=(12,0)),tela.Text('E-Mail',size=(7,0)),tela.Input()],
    [tela.Text('Cidade',size=(7,0)),tela.Input(),tela.Text('Estado',size=(7,0)),tela.Input(size=(3,0))],
    [tela.Text('Cep',size=(7,0)),tela.Input(size=(8,0))],
    [tela.Button('Salvar'),tela.Button('Limpar'),tela.Button('Buscar'),tela.Button('Fechar')],
    [tela.Output(size=(120,20),key='Output')]
    ]
    
window=tela.Window('CADASTRO DE CLIENTE',layout)

limpa=''

while True:    
    event,values=window.read()
    if event=='Salvar':
        sql.execute("INSERT INTO CLIENTE VALUES (?,?,?,?,?,?,?,?)",(values[0].title(),values[1].title(),values[2],\
        values[3],values[4].lower(),values[5].title(),values[6].upper(),values[7]))
        connection.commit()
        window[0].update(limpa)
        window[1].update(limpa)
        window[2].update(limpa)
        window[3].update(limpa)
        window[4].update(limpa)
        window[5].update(limpa)
        window[6].update(limpa)
        window[7].update(limpa)

    elif event=='Limpar':
        window[0].update(limpa)
        window[1].update(limpa)
        window[2].update(limpa)
        window[3].update(limpa)
        window[4].update(limpa)
        window[5].update(limpa)
        window[6].update(limpa)
        window[7].update(limpa)
        window.FindElement('Output').update(limpa)

    elif event=='Buscar':
        sql.execute("SELECT * FROM CLIENTE WHERE NOME LIKE '%'+?+'%'",values[0])
        for s in sql:
            print(s)

    elif event=='Fechar':
        break

sql.close()
window.close()

