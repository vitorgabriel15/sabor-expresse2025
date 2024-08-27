import os

def mostra_titulo():
    print("""
        
    ░█████╗░░█████╗░░██████╗░█████╗░  ██████╗░░█████╗░░██████╗  ███████╗██████╗░███████╗░██████╗░█████╗░░██████╗
    ██╔══██╗██╔══██╗██╔════╝██╔══██╗  ██╔══██╗██╔══██╗██╔════╝  ██╔════╝██╔══██╗██╔════╝██╔════╝██╔══██╗██╔════╝
    ██║░░╚═╝███████║╚█████╗░███████║  ██║░░██║███████║╚█████╗░  █████╗░░██████╔╝█████╗░░╚█████╗░███████║╚█████╗░
    ██║░░██╗██╔══██║░╚═══██╗██╔══██║  ██║░░██║██╔══██║░╚═══██╗  ██╔══╝░░██╔══██╗██╔══╝░░░╚═══██╗██╔══██║░╚═══██╗
    ╚█████╔╝██║░░██║██████╔╝██║░░██║  ██████╔╝██║░░██║██████╔╝  ██║░░░░░██║░░██║███████╗██████╔╝██║░░██║██████╔╝
    ░╚════╝░╚═╝░░╚═╝╚═════╝░╚═╝░░╚═╝  ╚═════╝░╚═╝░░╚═╝╚═════╝░  ╚═╝░░░░░╚═╝░░╚═╝╚══════╝╚═════╝░╚═╝░░╚═╝╚═════╝░""")

def mostra_escolhas():
    print("1. Cadastrar cliente")
    print("2. Listar ferramentas")
    print("3. Ativar Estoque")
    print("4. Sair")

def escolher_opcao():

    def finalizar_programa():
        os.system('cls')
        print('Finalizar programa')
        
        def opcao_invalida():
            print('está é uma opção inválida, escolha outra opção')
            input('Aperte qualquer tecla para voltar')
            main()
            
        try:
            opcao_escolhida = int(input('Escolha uma opção'))

            if opcao_escolhida == 1:
                print('Você escolheu Cadastrar cliente')
            elif opcao_escolhida == 2:
                print('Você escolheu Listar ferramentas')
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