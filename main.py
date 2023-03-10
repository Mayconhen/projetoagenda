def cadastrarpessoa():
    adclista = []
    nome = input("Digite o nome: ")
    celular = input("Digite o celular: ")
    adclista.append(nome)
    adclista.append(celular)
    listas.append(adclista)
    print("Usuário criado!")
    
def retornarpessoas(lista):
    for pessoas in lista:
        print(pessoas)
            
if __name__ == "__main__":
    listas = [[]]

    while True:
        menu = input("1.Entrar no menu\n2.Sair do programa\n")

        if menu != '2':
            opcao = input("Escolha uma das opcoes:\n1.Cadastrar Pessoa na Agenda\n2.Listar pessoas\n")

            if opcao == '1':
                cadastrarpessoa()
            if opcao == '2':
                retornarpessoas(listas[2])
        else:
            exit()
