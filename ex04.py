#
# 	Crie um programa em linguagem Python que recebe do usuário um valor de temperatura em graus Celsius e o converta
# 	para Fahrenheit ou Kelvin. O usuário deve informar “F” ou “f” caso queira efetuar a conversão para Fahrenheit
# 	e “K” ou “k” caso deseje converter o valor de temperatura para Kelvin. Caso qualquer outra letra seja informada,
# 	deve ser exibida a mensagem “Opção inválida de conversão!”. A seguir são apresentadas as equações para converter
# 	um valor de temperatura de Celsius (C) para Fahrenheit (F) e Kelvin (K), respectivamente:
# #
# # C = (F - 32) * 5/9 # Equação para converter Celsius para Fahrenheit
# # C = K - 273.15 # Equação para converter Celsius para Kelvin
# # F = C * 9/5 + 32 # Equação para converter Fahrenheit para Celsius
# # K = C + 273.15 # Equação para converter Kelvin para Celsius
# #
# # entrada de dados
opcao = input("Digite F para converter de Celsius para Fahrenheit ou K para converter de Celsius para Kelvin: ") # Recebe a opção
valor = float(input("Digite o valor da temperatura: ")) # Recebe o valor da temperatura

# processamento
if opcao == "F" or opcao == "f":
  print(f"{valor} Celsius é igual a {(valor - 32) * 5/9} Fahrenheit") # Imprime o valor convertido
elif opcao == "K" or opcao == "k":
  print(f"{valor} Celsius é igual a {valor + 273.15} Kelvin")
else:
  print("Opção inválida de conversão!")

print("Fim do programa")

