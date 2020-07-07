import PySimpleGUI as tela


layout=[
    [tela.Text('01º Lançamento'),tela.Input('0',size=(7,0)),tela.Text('kWh')],
    [tela.Text('02º Lançamento'),tela.Input('0',size=(7,0)),tela.Text('kWh')],
    [tela.Text('03º Lançamento'),tela.Input('0',size=(7,0)),tela.Text('kWh')],
    [tela.Text('04º Lançamento'),tela.Input('0',size=(7,0)),tela.Text('kWh')],
    [tela.Text('05º Lançamento'),tela.Input('0',size=(7,0)),tela.Text('kWh')],
    [tela.Text('06º Lançamento'),tela.Input('0',size=(7,0)),tela.Text('kWh')],
    [tela.Text('07º Lançamento'),tela.Input('0',size=(7,0)),tela.Text('kWh')],
    [tela.Text('08º Lançamento'),tela.Input('0',size=(7,0)),tela.Text('kWh')],
    [tela.Text('09º Lançamento'),tela.Input('0',size=(7,0)),tela.Text('kWh')],
    [tela.Text('10º Lançamento'),tela.Input('0',size=(7,0)),tela.Text('kWh')],
    [tela.Text('11º Lançamento'),tela.Input('0',size=(7,0)),tela.Text('kWh')],
    [tela.Text('12º Lançamento'),tela.Input('0',size=(7,0)),tela.Text('kWh')],
    [tela.Button('Calcular',button_color=('white','green')),\
     tela.Button('Limpar',button_color=('white','blue')),\
     tela.Button('Sair',button_color=('white','red'))],
    [tela.Output(key='Output')]
    ]
window=tela.Window('Média Cosumo kWh',layout)


while True:
    lista=[]
    event,values=window.read()
    if event=='Calcular':
        for v in values:
            convert=values[v].replace(',','.')
            if float(convert)>0:            
                lista.append(float(convert))
                soma=sum(lista)/len(lista)
        print('Média consumo Kwh entre',len(lista),'meses: %.2f'%soma+'kWh')
        del(lista)
    if event=='Limpar':
        window[0].update('0')
        window[1].update('0')
        window[2].update('0')
        window[3].update('0')
        window[4].update('0')
        window[5].update('0')
        window[6].update('0')
        window[7].update('0')
        window[8].update('0')
        window[9].update('0')
        window[10].update('0')
        window[11].update('0')
        window.FindElement('Output').update('')
    if event=='Sair':
        break
window.close()
