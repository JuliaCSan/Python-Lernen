class Farmacia:
    def __init__(self, clientes, produto):
        self.__clientes = clientes
        self.__produto = produto

    def clientes(self, nome, telefone, cpf):
        self.__nome = nome
        self.__telefone = telefone
        self.__cpf = cpf

    def produto(self, nomeProduto, preco):
        self.__nomeProduto = nomeProduto
        self.__preco = preco



def cadastrar_clientes() -> None:
    clientes = input('Deseja cadastrar um novo cliente? (S/N)')
    if clientes == "s":
        input('Digite o nome do cliente: ')
        input('Digite o telefone do cliente: ')
        input('Digite o cpf do cliente: ')
    print('Cliente cadastrado com sucesso.')
    cadastrar_clientes()

def cadastrar_produto() -> None:
    clientes = input('Deseja cadastrar um novo produto? (S/N)')
    if clientes == "s":
        input('Digite o nome do produto: ')
        int(input('Digite preço do produto: '))
    print('Produto cadastrado com sucesso.')
cadastrar_produto()
