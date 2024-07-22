def cadastrar_carro(lista_carros):
    marca_carro = input("Digite a marca do carro: ")
    modelo_carro = input("Digite o modelo do carro: ")
    ano_carro = input("Digite o ano do carro: ")
    cor_carro = input("Digite a cor do carro: ")
    novo_carro = {"marca": marca_carro, "modelo": modelo_carro, "ano do carro": ano_carro, "cor": cor_carro}
    
    lista_carros.append(novo_carro)
    print("Carro cadastrado com sucesso!")

lista_carros = []

def listar_carros(lista_carros):
    print("\n=== Lista de Carros ===")
    for i, carro in enumerate(lista_carros, start=1):
        print(f"{i}. Marca: {carro['marca']}, Modelo: {carro['modelo']}, Ano: {carro['ano do carro']}, Cor: {carro['cor']}")

def procurar_carro(lista_carros, busca):
    lista_carros_encontrados = []  

    for carro in lista_carros:
        if busca.lower() in carro['marca'].lower() or busca.lower() in carro['modelo'].lower():
            lista_carros_encontrados.append(carro)

    if lista_carros_encontrados:
        print("\nCarros encontrados:")
        for i, carro_encontrado in enumerate(lista_carros_encontrados, start=1):
            print(f"{i}. Marca: {carro_encontrado['marca']}, Modelo: {carro_encontrado['modelo']}, Ano: {carro_encontrado['ano do carro']}, Cor: {carro_encontrado['cor']}")
    else:
        print("\nNenhum carro correspondente encontrado.")

while True:
    print("\n=== Menu ===")
    print("1. Cadastrar carro")
    print("2. Listar carros")
    print("3. Procurar dados de um carro")
    print("5. Sair do sistema")

    escolha = input("Escolha uma opção: ")

    if escolha == "1":
        cadastrar_carro(lista_carros)
    elif escolha == "2":
        listar_carros(lista_carros)
    elif escolha == "3":
        busca_usuario = input("Digite a marca ou modelo do carro que deseja procurar: ")
        procurar_carro(lista_carros, busca_usuario)
    elif escolha == "5":
        print("Encerrando o sistema. Até mais!")
        break
    else:
        print("Opção inválida. Tente novamente.")
