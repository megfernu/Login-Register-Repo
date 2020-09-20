import csv

def menu():
    opcao = input('1 - Login\n2 - Registar\n>>>')
    if opcao == '1':
        login()
    elif opcao == '2':
        register()
    else:
        print('Escolha uma opção válida.')
        menu()



def login():
    with open('logs.csv', 'r') as csv_file:
        csv_reader = csv.reader(csv_file)

        next(csv_reader)
        nome = input('nome:')
        temp = False
        
        for line in csv_reader:
             if nome == line[0]:
                temp = True
                print('muito bom')
                senha = input('senha:')
                if senha == line[1]:
                    print('pass correta')
                else:
                    print('Pass errada')
                    menu()
        if temp == False:
            print('Utilizador nao regitado')
            menu()
               

def register():
    with open('logs.csv', 'r') as csv_file:
        csv_reader = csv.reader(csv_file)

        next(csv_reader)
        registo = input('Introduza o nome de utilizador:')
        for line in csv_reader:
            if registo == line[0]:
                print('utilizador ja registado')
                register()
                

        senha = input('Introduza a password:')
        lista = [registo, senha]
        with open(r'logs.csv', 'a') as csv_file:
            csv_writer = csv.writer(csv_file)
            csv_writer.writerow(lista)
            csv_file.close()
            menu()



menu()




