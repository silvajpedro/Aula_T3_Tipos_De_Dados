# 2015 -> Relatório IDC (International Data Corporation) patrocinado pela Seagate
# Em 2015, foi informado que cada pessoa na Terra com acesso à internet,
# seja por redes sociais, mecanismos de pesquisa, interações na web ou ligações via internet,
# produzia cerca de 1,3 GB de dados por dia.

# Arrays (Listas em Python)
# São estruturas que armazenam uma grande quantidade de informações,
# porém de forma não necessariamente organizada.

lista_dos_sonhos = [
    "Subitamente receber uma quantia inigualável de papel moeda na conta.",
    "PC Gamer com luzinha e tudo.",
    "Um emprego no Google",
    "Mark Zuckerberg",
    "Trabalhar para o Elon Musk",
    "Meu sonho é aposentar sem calvície"
]

# Exibindo a lista completa
print(lista_dos_sonhos)

# Acessando elementos específicos da lista
print(lista_dos_sonhos[0], lista_dos_sonhos[3])  # Primeiro e quarto elemento

# Verificando o tipo de dado da lista e de um item específico
print(type(lista_dos_sonhos))  # Retorna 'list'
print(type(lista_dos_sonhos[0]))  # Retorna 'str'

# Indexação Negativa -> Acessando elementos de trás para frente
print(lista_dos_sonhos[-1])  # Último elemento
print(lista_dos_sonhos[-2])  # Penúltimo elemento

# Métodos de Listas

# insert -> Adiciona um item em uma posição específica
lista_dos_sonhos.insert(0, "Que a Fernanda pague todo mundo que deve!!!")
print(lista_dos_sonhos)

# append -> Adiciona um item ao final da lista
lista_dos_sonhos.append("Viajar o mundo")
lista_dos_sonhos.append("Dodge Ram")
print(lista_dos_sonhos)

# sort -> Ordena a lista em ordem alfabética (crescente ou decrescente)
nomes = ["Plinio", "Camila", "Julia", "Alisson", "Luis Otavio", "Plinio", "George", "Evila", "Renato"]

nomes.sort()  # Ordem crescente (A-Z)
print(nomes)

nomes.sort(reverse=True)  # Ordem decrescente (Z-A)
print(nomes)

# remove -> Remove um item específico da lista (somente a primeira ocorrência encontrada)
nomes.remove("Plinio")  # Remove apenas o primeiro "Plinio" encontrado
nomes.remove("Evila")
print(nomes)

# pop -> Remove um item pelo índice informado
nomes.pop(0)  # Remove o primeiro elemento
nomes.pop(-1)  # Remove o último elemento
print(nomes)

# index -> Retorna o índice de um item na lista
comidas_do_sextou = ["Pizza", "Churrasco", "Caixa de Salgados", "Comida Japonesa", "Comida Chinesa", "Cachorro Quente", "Comida Indiana", "Pastel", "Tapioca"]

print(comidas_do_sextou.index("Comida Indiana"))  # Retorna a posição de "Comida Indiana"

# Removendo um item com pop utilizando o índice retornado
comidas_do_sextou.pop(comidas_do_sextou.index("Comida Indiana"))
print(comidas_do_sextou)

# Simulando um sistema de pedidos
print("Bem-vindo ao Vai No Lanche")

pedidos = []
qntd_pedidos = int(input("Boa noite, caro(a) cliente. Quantos pedidos deseja fazer? "))

# Solicitando os pedidos do cliente
while len(pedidos) < qntd_pedidos:
    pedidos.append(input("Digite o seu pedido: "))

# Exibindo os pedidos realizados
print(f"Seus pedidos foram: {pedidos}")
