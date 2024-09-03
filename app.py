import os

ferramentas = []

def mostra_titulo():
    print("""
        
    ░█████╗░░█████╗░░██████╗░█████╗░  ██████╗░░█████╗░░██████╗  ███████╗██████╗░███████╗░██████╗░█████╗░░██████╗
    ██╔══██╗██╔══██╗██╔════╝██╔══██╗  ██╔══██╗██╔══██╗██╔════╝  ██╔════╝██╔══██╗██╔════╝██╔════╝██╔══██╗██╔════╝
    ██║░░╚═╝███████║╚█████╗░███████║  ██║░░██║███████║╚█████╗░  █████╗░░██████╔╝█████╗░░╚█████╗░███████║╚█████╗░
    ██║░░██╗██╔══██║░╚═══██╗██╔══██║  ██║░░██║██╔══██║░╚═══██╗  ██╔══╝░░██╔══██╗██╔══╝░░░╚═══██╗██╔══██║░╚═══██╗
    ╚█████╔╝██║░░██║██████╔╝██║░░██║  ██████╔╝██║░░██║██████╔╝  ██║░░░░░██║░░██║███████╗██████╔╝██║░░██║██████╔╝
    ░╚════╝░╚═╝░░╚═╝╚═════╝░╚═╝░░╚═╝  ╚═════╝░╚═╝░░╚═╝╚═════╝░  ╚═╝░░░░░╚═╝░░╚═╝╚══════╝╚═════╝░╚═╝░░╚═╝╚═════╝░
    """)

def mostra_escolhas():
    print("1. Cadastrar ferramentas")
    print("2. Listar ferramentas")
    print("3. Ativar estoque")
    print("4. Finalizar programa")

def escolher_opcao():

    def exibir_subtitulo(texto):
        print(texto)
        print("")

    def retorna_menu():
        input("\nPressione qualquer tecla para voltar ao menu principal.")
        main()

    def cadastrar_ferramentas():
        exibir_subtitulo("Cadastrar ferramentas")
        
        nome_ferramentas = input("Digite o nome da ferramenta que deseja cadastrar: ")
        quantidade_ferramentas = input("Digite a quantidade da ferramenta: ")
        dados_da_ferramenta = {"nome": nome_ferramentas, "quantidade": quantidade_ferramentas, "ativo": True}
        ferramentas.append(dados_da_ferramenta)
        print(f"\nA ferramenta '{nome_ferramentas}' foi cadastrada com sucesso!\n")
        
        retorna_menu()

    def listar_ferramentas():
        exibir_subtitulo("Lista de ferramentas cadastradas")
        if ferramentas:
            for ferramenta in ferramentas:
                nome_ferramenta = ferramenta["nome"]
                quantidade_ferramenta = ferramenta["quantidade"]
                ativo = "Ativo" if ferramenta["ativo"] else "Inativo"
                print(f" - {nome_ferramenta} | Quantidade: {quantidade_ferramenta} | Status: {ativo}")
        else:
            print("Nenhuma ferramenta cadastrada.")
        retorna_menu()

    def ativar_estoque():
        exibir_subtitulo("Ativar Estoque")
        ferramenta_nome = input("Digite o nome da ferramenta que deseja ativar: ")
        ferramenta_encontrada = False
        
        for ferramenta in ferramentas:
            if ferramenta["nome"].lower() == ferramenta_nome.lower():
                ferramenta["ativo"] = True
                print(f"A ferramenta '{ferramenta_nome}' foi ativada com sucesso!")
                ferramenta_encontrada = True
                break
        
        if not ferramenta_encontrada:
            print(f"Ferramenta '{ferramenta_nome}' não encontrada.")
        
        retorna_menu()

    def finalizar_programa():
        print("\nFinalizando o programa...\n")
        exit()

    def opcao_invalida():
        print("\nOpção inválida, escolha outra opção.")
        input("\nPressione qualquer tecla para voltar ao menu principal.")
        main()

    try:
        opcao_escolhida = int(input("Escolha uma opção: "))

        if opcao_escolhida == 1:
            cadastrar_ferramentas()
        elif opcao_escolhida == 2:
            listar_ferramentas()
        elif opcao_escolhida == 3:
            ativar_estoque()
        elif opcao_escolhida == 4:
            finalizar_programa()
        else:
            opcao_invalida()
    except ValueError:
        opcao_invalida()
        
def main():
    while True:
        mostra_titulo()
        mostra_escolhas()
        escolher_opcao()
    
if __name__ == '__main__':
    main()
