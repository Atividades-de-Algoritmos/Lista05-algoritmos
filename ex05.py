#
# 5.	O Brasil adota, assim como a maioria dos países, o calendário gregoriano como sendo o seu calendário civil.
# Nele, a maioria dos anos é composto por 365 dias. Entretanto, o tempo necessário para que a Terra orbite o sol é,
# na realidade, um pouco maior do que isso (365 dias, 5 horas, 45 minutos e 45 segundos). Para corrigir esta
# diferença, foi incluído um dia extra no mês de fevereiro (29 de fevereiro) nos anos chamados de bissextos.
# Elabore um programa que leia um ano do usuário e exibe em tela uma mensagem, informando se o ano informado é
# bissexto ou não. O ano é bissexto se ele satisfaz a alguma das condições abaixo:
#
# •	Um ano é bissexto se ele for divisível por 4 e não for divisível por 100;
# •	Um ano é bissexto se ele for divisível por 400.
#
# entrada de dados
ano = int(input("Digite um ano: ")) # Recebe o ano

# processamento
if (ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0): # Se o ano for divisível por 4 e não for divisível por 100 ou se for divisível por 400
  print(f"{ano} é bissexto") # Imprime "Ano bissexto" se o ano for bissexto
else: # Se o ano não for bissexto
  print(f"{ano} não é bissexto") # Imprime "Ano não bissexto"

print("Fim do programa") # Imprime "Fim do programa"
