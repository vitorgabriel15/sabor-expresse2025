import os

ferramentas = [{"nome":"marreta1", "quantidade":"20", "ativo":True}]
       

def mostra_titulo():
    print("""
        
    ░█████╗░░█████╗░░██████╗░█████╗░  ██████╗░░█████╗░░██████╗  ███████╗██████╗░███████╗░██████╗░█████╗░░██████╗
    ██╔══██╗██╔══██╗██╔════╝██╔══██╗  ██╔══██╗██╔══██╗██╔════╝  ██╔════╝██╔══██╗██╔════╝██╔════╝██╔══██╗██╔════╝
    ██║░░╚═╝███████║╚█████╗░███████║  ██║░░██║███████║╚█████╗░  █████╗░░██████╔╝█████╗░░╚█████╗░███████║╚█████╗░
    ██║░░██╗██╔══██║░╚═══██╗██╔══██║  ██║░░██║██╔══██║░╚═══██╗  ██╔══╝░░██╔══██╗██╔══╝░░░╚═══██╗██╔══██║░╚═══██╗
    ╚█████╔╝██║░░██║██████╔╝██║░░██║  ██████╔╝██║░░██║██████╔╝  ██║░░░░░██║░░██║███████╗██████╔╝██║░░██║██████╔╝
    ░╚════╝░╚═╝░░╚═╝╚═════╝░╚═╝░░╚═╝  ╚═════╝░╚═╝░░╚═╝╚═════╝░  ╚═╝░░░░░╚═╝░░╚═╝╚══════╝╚═════╝░╚═╝░░╚═╝╚═════╝░""")

def mostra_escolhas():
    print("1. Cadastrar ferramentas")
    print("2. Listar ferramentas")
    print("3. Ativar Estoque")
    print("4. Sair")

def escolher_opcao():

    def exibir_subtitulo(texto):
        os.system("cls")
        print(texto)
        print("")

    def retorna_menu():
        input(" Digite uma tecla para voltar ao menu principal ")
        main()

    def cadastrar_ferramentas():
        exibir_subtitulo("Cadastrar ferramentas")
        nome_ferramentas = input("Digite o nome do produto que deseja cadastrar")
        ferramentas.append(nome_ferramentas)
        print(f" O produto {nome_ferramentas} foi cadastrado com sucesso\n")
        retorna_menu()

    def listar_ferramentas():
        exibir_subtitulo("Lista de ferramentas cadastrados\n")
        for ferramenta in ferramentas:
            nome_ferramenta = ferramenta["nome"]
            categoria_ferramenta = ferramenta["quantidade"]
            ativo = ferramenta["ativo"]
            print(f" - {nome_ferramenta} | {categoria_ferramenta} | {ativo}")
        retorna_menu()

        

    def finalizar_programa():
        os.system('cls')
        print('Finalizar programa\n')
        
    def opcao_invalida():
        print('está é uma opção inválida, escolha outra opção')
        input('Aperte qualquer tecla para voltar')
        main()
            
    try:
        opcao_escolhida = int(input('Escolha uma opção'))

        if opcao_escolhida == 1:
            cadastrar_ferramentas()
        elif opcao_escolhida == 2:
            listar_ferramentas()
        elif opcao_escolhida == 3:
            print('Você escolheu Ativar Estoque')
        elif opcao_escolhida == 4:
            finalizar_programa()
        else:
            opcao_invalida()
    except:
        opcao_invalida()
        
def main():
    mostra_titulo()
    mostra_escolhas()
    escolher_opcao()
    
if __name__ == '__main__':
    main()