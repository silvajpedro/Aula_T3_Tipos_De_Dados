# ----------- Funções em Python -----------
# Funções ajudam a:
# 1. Organizar melhor o código
# 2. Reutilizar trechos de código
# 3. Executar ações somente quando necessário

def lista_compras():
    """Exemplo de função que imprime itens a serem comprados."""
    print("Comprar leite em pó")

# Chamando a função
lista_compras()

# ----------- Simulando Login -----------

def boas_vindas(usuario):
    """Exibe uma mensagem de boas-vindas para o usuário logado."""
    print(f"Boas-vindas, {usuario}! Aproveite a promoção de 50% no frete.")

def login_invalido():
    """Exibe mensagem de erro para login inválido."""
    print("Tente novamente, suas credenciais estão inválidas!")

# Solicitando credenciais do usuário
email = input("Digite seu e-mail: ")
senha = int(input("Digite sua senha: "))

# Verificando login
if email == "joaodascouves@gmail.com" and senha == "123":
    boas_vindas(email)
else:
    login_invalido()

# ----------- Dicionários em Python -----------

# Explicação rápida sobre tipos de coleções em Python:
# () -> Tupla: Armazena dados imutáveis (exemplo: meses do ano)
# [] -> Lista: Armazena dados sem estrutura específica (exemplo: itens aleatórios)
# {} -> Dicionário: Armazena dados organizados em pares de chave e valor (exemplo: informações de clientes)

# Criando um dicionário com nomes de clientes organizados por estado
clientes = {
    'cliente_rj': 'Kauã',
    'cliente_mg': ['Alisson', 'Isael'],
    'cliente_pb': 'Haydee',
    'cliente_pe': 'Nat',
    'cliente_ba': 'Jeferson',
    'cliente_sp': 'Leandra',
    'cliente_df': 'Karyne',
    'cliente_al': 'Camila',
    'cliente_ce1': 'Renato',  # Alterado para evitar duplicação de chave
    'cliente_ce2': 'Évila'
}

# Exibindo dicionário completo
print("\nLista de clientes:")
print(clientes)

# Alterar uma informação no dicionário
clientes['cliente_rj'] = "Aline"

# Adicionar um novo cliente
clientes['cliente_são_gonçalo'] = "Mariana"

# Exibir a lista atualizada de clientes
print("\nLista de clientes atualizada:")
print(clientes)

# Remover um cliente do dicionário
del clientes['cliente_rj']

# Adicionar um novo nome à lista de clientes de MG
clientes['cliente_mg'].append("Mônica")

# Exibir lista final de clientes
print("\nLista final de clientes:")
print(clientes)

# Exibir apenas os valores (nomes dos clientes)
print("\nLista de clientes por estado:")
for nome in clientes.values():
    print(nome)
