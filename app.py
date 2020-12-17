# Importar bibliotecas
import PySimpleGUI as sg
from faker import Faker
import os

sg.theme('Dark')

# Layout do app (esqueleto)
layout = [
    [sg.Button('Gerar Nome', size=(20,0)), 
    sg.Input(key='nome', size=(60, 0))],

    [sg.Button('Gerar Profissão', size=(20,0)), 
    sg.Input(key='profissao', size=(60, 0))],

    [sg.Button('Gerar Endereço', size=(20,0)), 
    sg.Input(key='endereço', size=(60, 0))],

    [sg.Button('Gerar Placa', size=(20,0)), 
    sg.Input(key='placa', size=(60, 0))],

    [sg.Button('Gerar Cartão de Crédito', size=(20,0)), 
    sg.Input(key='cartao_credito', size=(60, 0))],

    [sg.Button('Gerar Telefone', size=(20,0)), 
    sg.Input(key='telefone', size=(60, 0))],

    [sg.Output(size=(85, 20))],
    [sg.Button('Imprimir Perfil Completo'), 
    sg.Button('Salvar Perfil em Arquivo')]
]

# Criando a janela, usando o layout que foi definido
janela = sg.Window('Faker - Gerador de Dados para Teste', layout=layout)

# Lendo os eventos da tela e gerar os dados fakes
# fake = Faker() -> dados em inglês
fake = Faker('pt_BR')
Faker.seed(0)
while True:
    event, valores = janela.Read()
    if event == sg.WIN_CLOSED:
        break

    if event == 'Gerar Nome':
        janela['nome'].update(fake.name())

    elif event == 'Gerar Profissão':
        janela['profissao'].update(fake.job())

    elif event == 'Gerar Endereço':
        janela['endereço'].update(fake.address())

    elif event == 'Gerar Placa':
        janela['placa'].update(fake.license_plate())

    elif event == 'Gerar Cartão de Crédito':
        janela['cartao_credito'].update(fake.credit_card_full())

    elif event == 'Gerar Telefone':
        janela['telefone'].update(fake.phone_number())

    elif event == 'Imprimir Perfil Completo':
        # os.linesep -> quebra de linha
        print(f'NOME: {fake.name()}{os.linesep}PROFISSÃO: {fake.job()}{os.linesep}ENDEREÇO: {fake.address()}{os.linesep}PLACA: {fake.license_plate()}{os.linesep}CARTÃO DE CRÉDITO: {fake.credit_card_full()}TELEFONE: {fake.phone_number()}{os.linesep}')

    elif event == 'Salvar Perfil em Arquivo':
        with open('dados_falsos.txt', 'a',encoding='utf-8',newline='') as arquivo:
            arquivo.write(f'NOME: {fake.name()}{os.linesep}PROFISSÃO: {fake.job()}{os.linesep}ENDEREÇO: {fake.address()}{os.linesep}PLACA: {fake.license_plate()}{os.linesep}CARTÃO DE CRÉDITO: {fake.credit_card_full()}TELEFONE: {fake.phone_number()}{os.linesep}')


    


