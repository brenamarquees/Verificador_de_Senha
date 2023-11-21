
import bcrypt
import getpass

class ControleSenha:
    def __init__(self):
        self.arquivo_senhas = "senhas.txt"
        self.arquivo_senhasdig = "senhasdig.txt"
        
    def valida_senha(self, senha_digitada, hash_senha):
        return bcrypt.checkpw(senha_digitada, hash_senha)

    def salvar_senha(self, senha):
        with open(self.arquivo_senhasdig, "a") as file:
            file.write(senha + "\n")

        with open(self.arquivo_senhas, "a") as file:
            hash_senha = bcrypt.hashpw(senha.encode(), bcrypt.gensalt())
            file.write(hash_senha.decode() + "\n")

    def fazer_login(self, senha):
        with open(self.arquivo_senhas, "r") as file:
            linhas = file.readlines()
            for linha in linhas:
                hash_senha_armazenada = linha.strip()
                if self.valida_senha(senha.encode(), hash_senha_armazenada.encode()):
                    print("Senha autenticada com sucesso!")
                    return
            print("Senha incorreta.")

if __name__ == '__main__':
    controle_senha = ControleSenha()
    
    while True:
        print("Escolha uma opção:")
        print("1. Fazer Login")
        print("2. Cadastrar Nova Senha")
        print("3. Sair")
        
        opcao = input("Opção: ")
        
        if opcao == '1':
            senha_login = getpass.getpass('Digite a Senha para fazer login: ')
            controle_senha.fazer_login(senha_login)
        elif opcao == '2':
            senha = getpass.getpass('Digite a Nova Senha: ')
            controle_senha.salvar_senha(senha)
            print("Senha cadastrada com sucesso!")
        elif opcao == '3':
            break
        else:
            print("Opção inválida. Tente novamente.")
