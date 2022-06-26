
# Autores:
# Michel Silva
# Emanuel Frank
# Carlos Eduardo
# data: 26/06/2022
#
#
# 3.	Considere que uma determinada lista de contatos telefônicos encontre-se possua os registros apresentados
# na tabela a seguir. Desenvolva um programa em Python que permite que o usuário digite o nome de um contato que
# pretende consultar e, em seguida, exibe em tela o número telefônico correspondente. Caso o contato não exista na
# lista, deve ser exibida a mensagem: “Contato não encontrado!”.
#####################################
# nome contato	# número do contato #
# Maria         # 9111-1111        	#
# Joana         # 9222-2222        	#
# Joaquim       # 9333-3333        	#
# Pedro         # 9444-4444        	#
#####################################

# entrada de dados
nome = input("Digite o nome do contato: ") # Recebe o nome do contato

# processamento
if nome == "Maria": # Se o nome do contato for "Maria"
  print("9111-1111") # Imprime "9111-1111"
elif nome == "Joana": # Se o nome do contato for "Joana"
  print("9222-2222") # Imprime "9222-2222"
elif nome == "Joaquim": # Se o nome do contato for "Joaquim"
  print("9333-3333") # Imprime "9333-3333"
elif nome == "Pedro": # Se o nome do contato for "Pedro"
  print("9444-4444") # Imprime "9444-4444"
else: # Se o nome do contato não for "Maria", "Joana", "Joaquim" ou "Pedro"
  print("Contato não encontrado!") # Imprime "Contato não encontrado!"

print("Fim do programa") # Imprime "Fim do programa"