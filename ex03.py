#
# Autores:
# Michel Silva
# Emanuel Franklyn
# Carlos Eduardo
#
# Data: 27/06/2022
#
# 3. Considere que uma determinada lista de contatos 
# telefônicos encontre-se possua os registros apresentados na
# tabela a seguir. Desenvolva um programa em Python que 
# permite que o usuário digite o nome de um contato que
# pretende consultar e, em seguida, exibe em tela o número 
# telefônico correspondente. Caso o contato não exista na 
# lista, deve ser exibida a mensagem: “Contato não 
# encontrado!”.
#
# #---------------#-------------------#
# | Nome Contato	| Número do Contato |
# | Maria         | 9111-1111        	|
# | Joana         | 9222-2222        	|
# | Joaquim       | 9333-3333        	|
# | Pedro         | 9444-4444        	|
# #---------------#-------------------#

# Entrada de dados

nome = input("Digite o nome do contato: ") # Recebe o nome do contato

# Processamento e saída de dados

if nome == "Maria": # Se o nome do contato for "Maria"
  print("Contato: 9111-1111") # Imprime "Contato: 9111-1111"
elif nome == "Joana": # Se o nome do contato for "Joana"
  print("Contato: 9222-2222") # Imprime "Contato: 9222-2222"
elif nome == "Joaquim": # Se o nome do contato for "Joaquim"
  print("Contato: 9333-3333") # Imprime "Contato: 9333-3333"
elif nome == "Pedro": # Se o nome do contato for "Pedro"
  print("Contato: 9444-4444") # Imprime "Contato: 9444-4444"
else: # Se o nome do contato não for "Maria", "Joana", "Joaquim" ou "Pedro"
  print("Contato não encontrado!") # Imprime "Contato não encontrado!"

print("fim do programa") # Imprime "fim do programa"
