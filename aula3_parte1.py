# 📌 Tuplas -> São listas imutáveis, ou seja, não podem ser alteradas, adicionadas ou removidas após a criação.

# Exemplo de tupla com personagens
personagens = ("Kauã Baconzito", "Grazi Moranguinho", "Fêrapeuta", "Felipe do Parabéns", "Fê Da Páscoa")

# Criando uma tupla com informações de um usuário
usuaria = ("Carol Instrutora", 3216549876, "09/02/2025")

# Criando uma tupla vazia e verificando seu tipo
cliente_vai_no_banco = ()
print("📌 Tipo da variável cliente_vai_no_banco:", type(cliente_vai_no_banco))  # Saída: <class 'tuple'>

# Convertendo uma tupla vazia para lista, adicionando dados e reconvertendo para tupla
dados_cliente = ()
dados_cliente = list(dados_cliente)  # Convertendo para lista

# Adicionando dados ao cliente
dados_cliente.append("Tulani Souza")
dados_cliente.append("08/02/2025")
dados_cliente.append(1234567891)

# Convertendo de volta para tupla
dados_cliente = tuple(dados_cliente)

print("\n📌 Dados do cliente cadastrados:", dados_cliente)
print("📌 Tipo da variável dados_cliente:", type(dados_cliente))  # Saída: <class 'tuple'>

# 📌 Funções -> São blocos de código reutilizáveis que realizam uma tarefa específica.

# 🔹 Exemplo de função simples
def saudacao():
    print("Função que exibe uma mensagem de boas-vindas.")
    print("\n👋 Olá! Seja bem-vindo ao curso de Python!")

# Chamando a função
saudacao()
