
# Autores:
# Michel Silva
# Emanuel Frank
# Carlos Eduardo
# data: 26/06/2022
#
#
# 1.	Desenvolva um programa em Python que recebe do usuário um número real e exibe em tela se este número é maior,
# menor ou igual que zero.
#
# entrada de dados
numero = float(input("Digite um número real: ")) # Recebe o número

# processamento
if numero > 0:
  print(f"{numero} é maior que zero") # Imprime "Maior que zero"
elif numero < 0:
  print(f"{numero} é menor que zero") # Imprime "Menor que zero"
else:
  print(f"{numero} é igual a zero") # Imprime "Igual a zero"

print("Fim do programa")