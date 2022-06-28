#
# Autores:
# Michel Silva
# Emanuel Franklyn
# Carlos Eduardo
#
# data: 27/06/2022
#
# 6. Implemente um programa em linguagem Python que seja     
# capaz de realizar as operações aritméticas de adição,      
# subtração, multiplicação e divisão entre dois números dados
# Inicialmente, o usuário deve informar os valores de dois   
# números e em seguida selecionar uma das operações          
# aritméticas citadas. Para isto, ele deve digitar “+” para  
# adição, “-” para subtração, “*” para multiplicação e “/”   
# para divisão. O programa deve apresentar como saída o      
# resultado da operação desejada. Observação. A divisão por  
# zero deve ser evitada, uma vez que esta operação gera um   
# erro em tempo de execução do programa. Desta maneira, caso 
# o divisor da operação de divisão for igual a zero, deve-se 
# apresentar uma mensagem de erro, “ERRO: divisão por zero!”,
# e NÃO EFETUAR a operação de divisão.                       

# Entrada de dados

num1 = float(input("Digite o primeiro número: ")) # Recebe o primeiro número
num2 = float(input("Digite o segundo número: ")) # Recebe o segundo número
opcao = input("Digite + para adição, - para subtração, * para multiplicação ou / para divisão: ") # Recebe a opção

# Processamento de dados

if opcao == "+": # Se a opção for igual ao símbolo "+" representando a adição
  print(f"{num1} + {num2} = {num1 + num2}") # Imprime o resultado da adição entre os dois números informados

elif opcao == "-": # Se a opção for igual ao símbolo "-" representando a subtração
  print(f"{num1} - {num2} = {num1 - num2}") # Imprime o resultado da subtração entre os dois números informados

elif opcao == "*": # Se a opção for igual ao símbolo "*" representando a multiplicação
  print(f"{num1} * {num2} = {num1 * num2}") # Imprime o resultado da multiplicação entre os dois números informados

elif opcao == "/": # Se a opção for igual ao símbolo "/" representando a divisão
  
  if num2 == 0: # Se o dividendo ou segundo valor informado for igual a zero
    print("ERRO: divisão por zero!") # Imprime um erro no terminal
  
  else: # Caso contrário
    print(f"{num1} / {num2} = {num1 / num2}") # Imprime o resultado da divisão

else: # Caso a opção informada não seja nenhum dos símbolos de operação
  print("Opção inválida de conversão!") # Imprime erro no terminal

print("fim do programa") # Informa ao usuário que o programa terminou
