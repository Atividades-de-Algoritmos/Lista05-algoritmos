#
# Autores:
# Michel Silva
# Emanuel Franklyn
# Carlos Eduardo
#
# data: 27/06/2022
#
# 4. Crie um programa em linguagem Python que recebe do      
# usuário um valor de temperatura em graus Celsius e o       
# converta para Fahrenheit ou Kelvin. O usuário deve informar
# “F” ou “f” caso queira efetuar a conversão para Fahrenheit 
# e “K” ou “k” caso deseje converter o valor de temperatura  
# para Kelvin. Caso qualquer outra letra seja informada, deve
# ser exibida a mensagem “Opção inválida de conversão!”. A   
# seguir são apresentadas as equações para converter um valor
# de temperatura de Celsius (C) para Fahrenheit (F) e Kelvin 
# (K), respectivamente:                                      
#                                                            
# C = (F - 32) * 5/9 # Equação para converter Celsius para   
# Fahrenheit                                                 
#                                                            
# C = K - 273.15 # Equação para converter Celsius para Kelvin
#                                                            
# F = C * 9/5 + 32 # Equação para converter Fahrenheit para  
# Celsius                                                    
#                                                            
# K = C + 273.15 # Equação para converter Kelvin para Celsius

# Entrada de dados

opcao = input("Digite F para converter de Celsius para Fahrenheit ou K para converter de Celsius para Kelvin: ") # Recebe a opção de conversão
valor = float(input("Digite o valor da temperatura: ")) # Recebe o valor da temperatura

# Processamento e saída de dados

if opcao == "F" or opcao == "f": # Se a opção for F ou f
  print(f"\n{valor} Celsius é igual a {(valor - 32) * 5/9} Fahrenheit") # Imprime o valor convertido para Fahrenheit

elif opcao == "K" or opcao == "k": # Caso contrário, se a opção for K ou k
  print(f"\n{valor} Celsius é igual a {valor + 273.15} Kelvin") # Imprime o valor convertido para Kelvin

else: # Caso contrário, se a opção for qualquer outra letra
  print("Opção inválida de conversão!") # Imprime a mensagem de opção inválida

print("fim do programa") # Informa ao usuário que o programa terminou

# Versão 2.0 do código

# ---------------------------------------------------------------------------------- #

# Entrada de dados (Mesma da primeira versão)

# Processamento e saída de dados

# if opcao.lower() == 'f': # .lower() coloca toda a string em mínusculas, ex: 'CARLOS' depois do .lower() vira 'carlos'
  # print(f"\n{valor} Celsius é igual a {(valor - 32) * 5/9} Fahrenheit")

# elif opcao.lower() == 'k':  # .lower() coloca toda a string em mínusculas, ex: 'CARLOS' depois do .lower() vira 'carlos'
  # print(f"\n{valor} Celsius é igual a {valor + 273.15} Kelvin")

# else: # Caso contrário, se a opção for qualquer outra letra
  # print("Opção inválida de conversão!") # Imprime a mensagem de opção inválida

# print("fim do programa")

# ---------------------------------------------------------------------------------- #
