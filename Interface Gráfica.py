import PySimpleGUI as sg

#Desenvolvidos pelo Ketsuo(Nettsku) e Dougla :3

#Começo do Projeto
class InterfaceGrafica:
    def __init__(self):
            #Layout
            layout = [
                [sg.Text('Nome'),sg.Input()],
                [sg.Text('Idade'),sg.Input()],
                [sg.Text('CPF'),sg.Input()],
                [sg.Text('RG'),sg.Input()],
                [sg.Text('Telefone ou Celular'),sg.Input()],
                [sg.Text('Email'),sg.Input()],
                [sg.Text('Estado'),sg.Input()],
                [sg.Text('Cidade'),sg.Input()],
                [sg.Text('CEP'),sg.Input()],
                [sg.Text('Bairo'),sg.Input()],
                [sg.Text('Rua'),sg.Input()],
                [sg.Text('Estado Civil'),sg.Input()],
                [sg.Text('Agencia'),sg.Input()],
                [sg.Text('Cartão de Credito ou Debito?'),sg.Input()],
                [sg.Text('Numero do Cartão de Credito ou Debito'),sg.Input()],
                [sg.Button('Finalizar Cadastro')],
            ]           #Registro do individuo ao Banco

            #Interface que ira aparecer ao Usuario
            self.Interface = sg.Window('Dados do Usuário').layout(layout)

#Nettsku = Ketsuo :3
    def iniciar (self):
                while True:
                    self.button, self.values = self.Interface.Read()
                    Nome = self.value['Nome']
                    Idade = self.value['Idade']
                    CPF = self.value['CPF']
                    RG = self.value['RG']
                    Telefone_Celular = self.value['Telefone ou Celular']
                    Email = self.value["Email"]
                    Estado = self.value['Estado']
                    Cidade = self.value['Cidade']
                    CEP = self.value['CEP']
                    Bairo = self.value['Bairo']
                    Rua = self.value['Rua']
                    Estado_Civil = self.value['Estado Civil']
                    Agencia = self.value['Agencia']
                    Cartao = self.value['Credito']
                    Cartao = self.value['Debito']
                    Cartao_Numero = self.value['Numero do Cartão de Credito ou Debito']
                    print(f'Nome: [nome]')
                    print(f'Idade: [Idade]')
                    print(f'CPF: [CPF]')
                    print(f'RG: [RG]')
                    print(f'Telefone ou Celular: [Telefone ou Celular]')
                    print(f'Email: [Email]')
                    print(f'Estado: [Estado]')
                    print(f'Cidade: [Cidade]')
                    print(f'CEP: [CEP]')
                    print(f'Bairo: [Bairo]')
                    print(f'Rua: [Rua]')
                    print(f'Estado Civil: [Estado Civil]')
                    print(f'Agencia: [Agencia]')
                    print(f'Cartao: [Credito]')
                    print(f'Cartão: [Debito]')
                    print(f'Numero do Cartão: [Cartão_Numero]')

tela = InterfaceGrafica()
tela.iniciar()
