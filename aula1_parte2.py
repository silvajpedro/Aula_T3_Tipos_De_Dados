# Conversão de Tipos  
# O Python permite converter dados de um tipo para outro, como transformar strings de entrada em números.

# Solicita dois valores do usuário e os converte para float (números decimais)  
primeiro_valor = float(input("Digite o primeiro valor: "))  
segundo_valor = float(input("Digite o segundo valor: "))  

# Exibe a soma dos dois valores  
print(f'A soma dos valores é: {primeiro_valor + segundo_valor:.2f}')

# Simulação de um pedido em uma lanchonete  
print("Bem-vindo à Lanchonete Vai No Lanche")

# Solicita ao usuário seu pedido de lanche e bebida  
lanche_cliente = input("Digite o lanche que você gostaria: ")  
bebida_cliente = input("Digite a bebida que você gostaria: ")  

# Solicita os preços do lanche e da bebida e os converte para float  
valor_lanche = float(input("Digite o valor do lanche: "))  
valor_bebida = float(input("Digite o valor da bebida: "))  

# Exibe o valor total do pedido  
print(f'O valor total que você irá pagar é R$ {valor_lanche + valor_bebida:.2f}')

# ----------------------------------------
# Condicionais (Controle de Fluxo)
# ----------------------------------------

# Condicional Simples  
# Se a condição for verdadeira, um bloco de código é executado.

saldo = False  # Define a variável saldo como False (sem dinheiro)
if saldo == False:
    print("Tá lascado!")  # Se saldo for False, exibe essa mensagem
    print("Faço parte da estrutura do if")  # Ainda dentro do bloco do if

# Condicional Composta  
# Se a condição for verdadeira, um bloco é executado; senão, outro bloco é executado.

idade = 18  # Define a idade como 18 anos

# Verifica se a idade é maior ou igual a 18 e se o saldo é True (tem dinheiro)
if saldo == True and idade >= 18:
    print("Uhuuuuul, você pode mandar um pix aos seus instrutores!!!")
else:
    # Exibe uma mensagem indicando a restrição
    print(f'Infelizmente você não pode mandar um pix para os seus instrutores, porque ou sua idade é menor que {idade} ou o seu saldo é {saldo}!!!')

# Condicionais Aninhadas  
# Quando há várias condições que precisam ser verificadas em sequência.

jantar = "Salada de legumes"  
bebida = "Suco Verde"  

# Avalia diferentes combinações de pratos e bebidas
if jantar == "Churrasco acompanhado de fritas e farofa" and bebida == "Coca-cola":
    print("Partiuuuu Churrascada!!!")
elif jantar == "Strogonoff de Frango" and bebida == "Dolly Guaraná":
    print("Partiuuu comer Strogonoff")
elif jantar == "Batata frita com cheddar e bacon" and bebida == "Coca-cola":
    print("Arrasou!!!")
else:
    print("Deixo pra próxima!")

# ----------------------------------------
# Operadores Lógicos e de Comparação  
# ----------------------------------------

# Operadores lógicos em JavaScript vs. Python:
# JavaScript -> &, ||, !  
# Python -> and, or, not  

# Explicação dos operadores lógicos em Python:
# and (E) -> Retorna True se ambas as condições forem verdadeiras  
# Exemplo: "Eu quero Batata Frita" **e** "Coca-cola" (ambas precisam ser verdadeiras)

# or (OU) -> Retorna True se pelo menos uma das condições for verdadeira  
# Exemplo: "Ou eu quero Batata Frita" **ou** "Coca-cola" (uma das duas já basta para ser verdadeiro)

# not (Negação) -> Inverte o valor lógico da condição  
# Exemplo: Se `saldo == False`, então `not saldo` será True.

# ----------------------------------------
# Operadores de Comparação  
# ----------------------------------------
# São usados para comparar valores e retornam True ou False.

a = 10  
b = 5  

print(f'{a} > {b}:', a > b)   # True  -> Verifica se "a" é maior que "b"
print(f'{a} < {b}:', a < b)   # False -> Verifica se "a" é menor que "b"
print(f'{a} >= {b}:', a >= b) # True  -> Verifica se "a" é maior ou igual a "b"
print(f'{a} <= {b}:', a <= b) # False -> Verifica se "a" é menor ou igual a "b"
print(f'{a} == {b}:', a == b) # False -> Verifica se "a" é igual a "b"
print(f'{a} != {b}:', a != b) # True  -> Verifica se "a" é diferente de "b"

# ----------------------------------------
# Exemplo de comparação de strings
# ----------------------------------------

senha_correta = "1234"
senha_digitada = input("Digite sua senha: ")

if senha_digitada == senha_correta:
    print("Acesso permitido!")
else:
    print("Senha incorreta!")
