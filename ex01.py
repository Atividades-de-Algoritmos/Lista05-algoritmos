#
# Autores:
# Michel Silva
# Emanuel Franklyn
# Carlos Eduardo
#
# data: 27/06/2022
#
# 1.	Desenvolva um programa em Python que recebe do usuário 
# um número real e exibe em tela se este número é maior,     
# menor ou igual que zero.                                   

# Entrada de dados
numero = float(input("Digite um número real: ")) # Recebe o número real

# Processamento
if numero > 0: # Se o número real for maior que zero
  print(f"\n{numero} é maior que zero") # Imprime "{numero} é maior que zero"
elif numero < 0: # Caso contrário, se o número real for menor que zero
  print(f"\n{numero} é menor que zero") # Imprime "{numero} é menor que zero"
else: # Caso contrário, se o número real for igual a zero
  print(f"\nO número é igual a zero") # Imprime "O número é igual a zero"

print("fim do programa") # Informa ao usuário que o programa terminou
