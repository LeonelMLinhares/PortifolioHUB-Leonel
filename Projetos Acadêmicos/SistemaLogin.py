import getpass
import hashlib

usuarios = {}


def cadastrar_usuario():
    print("\n--- CADASTRO ---")
    username = input("Digite um nome de usuário: ")

    if username in usuarios:
        print("Erro: Nome de usuário já existe!")
        return

    password = getpass.getpass("Digite uma senha: ")
    confirm_password = getpass.getpass("Confirme a senha: ")

    if password != confirm_password:
        print("Erro: As senhas não coincidem!")
        return


    hash_senha = hashlib.sha256(password.encode()).hexdigest()


    usuarios[username] = {
        'senha': hash_senha,
        'tentativas': 0,
        'bloqueado': False
    }

    print("Usuário cadastrado com sucesso!")


def fazer_login():
    print("\n--- LOGIN ---")
    username = input("Nome de usuário: ")
    password = getpass.getpass("Senha: ")


    if username not in usuarios:
        print("Erro: Usuário não encontrado!")
        return False

    usuario = usuarios[username]

    if usuario['bloqueado']:
        print("Erro: Conta bloqueada devido a muitas tentativas falhas!")
        return False


    hash_senha = hashlib.sha256(password.encode()).hexdigest()

    if hash_senha == usuario['senha']:
        print(f"Bem-vindo, {username}!")
        usuario['tentativas'] = 0
        return True
    else:
        usuario['tentativas'] += 1
        print(f"Senha incorreta! Tentativas restantes: {3 - usuario['tentativas']}")


        if usuario['tentativas'] >= 3:
            usuario['bloqueado'] = True
            print("Conta bloqueada devido a muitas tentativas falhas!")

        return False


def menu_principal():
    while True:
        print("\n--- MENU PRINCIPAL ---")
        print("1. Cadastrar novo usuário")
        print("2. Fazer login")
        print("3. Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            cadastrar_usuario()
        elif opcao == '2':
            if fazer_login():

                print("Login realizado com sucesso!")
                break  
        elif opcao == '3':
            print("Saindo...")
            break
        else:
            print("Opção inválida!")


if __name__ == "__main__":
    menu_principal()