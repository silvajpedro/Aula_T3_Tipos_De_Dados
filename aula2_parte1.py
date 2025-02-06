# -------------------------------------------------------
# Loops: Estruturas que repetem uma ação enquanto
# uma condição não é satisfeita.
# -------------------------------------------------------

# Exemplo 1: Loop "while"
# Neste exemplo, começamos com o valor 2 para a variável 'pessoas'
# e incrementamos de 2 em 2 até que o valor seja menor que 46.
pessoas = 2
while pessoas < 46:
    print(f"A instrutoríssima Fernanda deve {pessoas} pessoas")
    pessoas += 2  # Incrementa o valor de 'pessoas' em 2 a cada iteração

# Exemplo 1.1: Loop "while" para entrada de dados (comentado)
# Caso deseje utilizar input para saber quantos alunos foram pagos, descomente o código abaixo.
# alunos = int(input("Quantos alunos a Fernanda já pagou? "))
# while alunos < 100:
#     print(f"A Fernanda pagou {alunos} alunos")
#     alunos += 1

# -------------------------------------------------------
# Exemplo 2: Loop "for" iterando sobre listas
# -------------------------------------------------------

# Lista com os nomes das pessoas que a Fernanda deve.
nomes_que_fernanda_deve = [
    "Otavio", "Jade", "Isabella", "Ana Clara", "Luciana", "Rafael", "Mariana"
]

for nome in nomes_que_fernanda_deve:
    print(f"Extra, extra! Nomes que a Fernanda deve: {nome}")

# Lista com marcas de Airfryer disponíveis.
# Note que corrigi alguns nomes (por exemplo, "Samunsg" para "Samsung")
marcas_airfryer = [
    "Brastemp", "Polishop", "Samsung", "Wallita", "Britânia", "Mondial", "Electrolux"
]

for marca in marcas_airfryer:
    print(f"Aqui estão as marcas disponíveis de Airfryer: {marca}")

# -------------------------------------------------------
# Manipulação de Strings
# -------------------------------------------------------

# Definindo uma string para manipulação.
nome = "fernanda barbie pink"

# Métodos de manipulação de strings:
print(nome.upper())       # Converte toda a string para maiúsculas.
print(nome.capitalize())  # Converte apenas a primeira letra para maiúscula e o restante para minúsculas.
print(nome.lower())       # Converte toda a string para minúsculas.
print(nome.title())       # Converte a primeira letra de cada palavra para maiúscula.

# Exemplo de verificação de string:
# Se a variável 'nome' for exatamente "fernanda barbie", uma ação é executada.
if nome == "fernanda barbie":
    print("Ação a ser executada")
