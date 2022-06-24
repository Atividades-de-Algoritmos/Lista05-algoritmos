#
# 2.	Elabore um programa em linguagem Python que tem como saída o nome do time vencedor de uma partida de futebol.
# O seu programa deve receber os nomes dos dois times da partida e o número de gols marcados por cada um deles.
# Vence a partida aquele time que marcar o maior número de gols. Exiba a mensagem “EMPATE”, caso a partida não tenha
# tido um vencedor.
#
# entrada de dados
time1 = input("Digite o nome do time 1: ")  # Recebe o nome do time 1
time2 = input("Digite o nome do time 2: ")  # Recebe o nome do time 2
gols1 = int(input("Digite o número de gols do time 1: "))  # Recebe o número de gols do time 1
gols2 = int(input("Digite o número de gols do time 2: "))  # Recebe o número de gols do time 2

# processamento
if gols1 > gols2: # Se o número de gols do time 1 for maior que o do time 2
  print(f"{time1} venceu") # Imprime "Time 1 venceu"
elif gols2 > gols1: # Se o número de gols do time 2 for maior que o do time 1
  print(f"{time2} venceu") # Imprime "Time 2 venceu"
else: # Se os números de gols forem iguais
  print("EMPATE") # Imprime "EMPATE"



