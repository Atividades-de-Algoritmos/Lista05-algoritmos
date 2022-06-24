#
# 6.	Implemente um programa em linguagem Python que seja capaz de realizar as operações aritméticas de adição,
# subtração, multiplicação e divisão entre dois números dados. Inicialmente, o usuário deve informar os valores de
# dois números e em seguida selecionar uma das operações aritméticas citadas. Para isto, ele deve digitar “+” para
# adição, “-” para subtração, “*” para multiplicação e “/” para divisão. O programa deve apresentar como saída o
# resultado da operação desejada. Observação. A divisão por zero deve ser evitada, uma vez que esta operação gera um
# erro em tempo de execução do programa. Desta maneira, caso o divisor da operação de divisão for igual a zero,
# deve-se apresentar uma mensagem de erro, “ERRO: divisão por zero!”, e NÃO EFETUAR a operação de divisão.
#
# entrada de dados
num1 = float(input("Digite o primeiro número: ")) # Recebe o primeiro número
num2 = float(input("Digite o segundo número: ")) # Recebe o segundo número
opcao = input("Digite + para adição, - para subtração, * para multiplicação ou / para divisão: ") # Recebe a opção

# processamento
if opcao == "+": # Se a opção for adição
  print(f"{num1} + {num2} = {num1 + num2}") # Imprime o resultado da adição
elif opcao == "-": # Se a opção for subtração
  print(f"{num1} - {num2} = {num1 - num2}") # Imprime o resultado da subtração
elif opcao == "*": # Se a opção for multiplicação
  print(f"{num1} * {num2} = {num1 * num2}") # Imprime o resultado da multiplicação
elif opcao == "/": # Se a opção for divisão
  if num2 == 0: # Se o divisor for zero
    print("ERRO: divisão por zero!")   # Imprime erro
  else: # Senão
    print(f"{num1} / {num2} = {num1 / num2}") # Imprime o resultado da divisão
else: # Senão
  print("Opção inválida de conversão!") # Imprime erro

print("Fim do programa") # Imprime fim do programa
