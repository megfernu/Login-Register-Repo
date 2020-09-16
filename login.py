
users = {"nuno":"chave"}

def login():

    name = users.get(input('Utilizador:'))
    if name != None:
        senha = input('Password:')
        if senha == name:
            print('Pode entrar.')
    else:
        print('Nome de utilizador não registado.')
        menu()

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
