from datetime import datetime

print("Bem-vindo ao programa de perfil!", "Por favor, insira suas informações abaixo.")

nome = input("Digite seu nome: ")
data_nascimento = input("Digite sua data de nascimento: ")
email = input("Digite seu email: ")

# Validação de entradas vazias
if not nome:
    print("Nome não pode ser vazio. Por favor, insira um nome válido.")
    nome = input("Digite seu nome: ")

if not data_nascimento:
    print("Data de nascimento não pode ser vazia. Por favor, insira uma data válida.")
    data_nascimento = input("Digite sua data de nascimento: ")

if not email:
    print("Email não pode ser vazio. Por favor, insira um email válido.")
    email = input("Digite seu email: ")

# Validação de formato de data
def validar_data(data_str, formato="%d/%m/%Y"):
    try:
        # Tenta converter a string para o formato de data
        datetime.strptime(data_str, formato)
        return True
    except ValueError:
        # Se falhar, a data é inválida (ex: 31/02/2026 ou texto errado)
        return False

if validar_data(data_nascimento) == False:
    print("Data de nascimento no formato válido, use o formato dd/mm/aaaa.")
    data_nascimento = input("Digite sua data de nascimento: ")

# Cálculo da idade
idade = datetime.now().year - datetime.strptime(data_nascimento, "%d/%m/%Y").year

# Exibição das informações do usuário
print(f"Olá, {nome}! Você nasceu em {data_nascimento}, seu email é {email} e tem {idade} anos.")