import csv

with open('logs.csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file)

    


users = {'nome:','nuno'}



def login():
    with open('logs.csv', 'r') as csv_file:
        csv_reader = csv.reader(csv_file)

        next(csv_reader)

    #name = users.get(input('Utilizador:'))
        name = input('utilizador:')
        senha = input('senha:')
        for line in csv_reader:
             if name == line[0]:
                print('a trabalhar')
                #if senha == line[1]:
                    #print('Pode entrar.')
                #else:
                    #print('senha errada')
             else:
                 print('nome de utilizador não registado')
                 #menu()
            
   # if name != None:
        #senha = input('Password:')
       # if senha == name:
        #    print('Pode entrar.')
    #else:
        #print('Nome de utilizador não registado.')
       # menu()

def register():
    registo = input('Introduza o nome de utilizador:')
    if users.get(registo) != None:
        print('Utilizador ja existe.')
        register()
    else:
        users[registo] = ''
        valor = input('Introduza a password:')
        valor2 = input('Repita a password:')
        if valor == valor2:
            users[registo] = valor
            print('Registado com sucesso')
            print(users)
        else:
            print('A password não é igual.')
            register()

def menu():
    escolha = input('1 - Login\n2 - Register\n>>:')
    if escolha == '1':
        login()
    elif escolha == '2':
        register()
    else:
        print('Introduza uma opção correta.')
        menu()



menu()
