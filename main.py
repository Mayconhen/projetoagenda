from cadastrar import cadastrar

def retornapessoa(pessoanome, pessoacelular):
    print("Nome da pessoa:{}\nCelular da pessoa:{}".format(pessoanome, pessoacelular))

def cadastrarpessoa():
    pessoanome = input("Digite o nome do contato: ")
    pessoacelular = input("Digite o telefone da pessoa: ")
    print("Pessoa cadastrada!\n")
    return pessoanome, pessoacelular

if __name__ == "__main__":

    while True:
        menu = input("1.Entrar no menu\n2.Sair do programa\n")

        if menu != '2':

            opcao = input("Escolha uma das opcoes:\n1.Cadastrar Pessoa na Agenda\n2.Alterar dados da Pessoa\n3.Listar pessoas\n")
            if opcao == '1':
                cadastrarpessoa()

            if opcao == '2':
                novonome = input("Digite o novo nome do contato: ")
                novocelular = input("Digite o novo telefone da pessoa: ")
                pessoanome = novonome
                pessoacelular = novocelular
            
            if opcao == '3':
                retornapessoa(pessoanome, pessoacelular)

        else:
            exit()
