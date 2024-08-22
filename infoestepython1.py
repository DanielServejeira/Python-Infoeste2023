import random

# n1 = float(input("Insira o primeiro número\n"))
# n2 = float(input("Insira o segundo número\n"))
# media = (n1+n2)/2 
# print(f"Média: {media}")
#
# fat = int(input("Insira um número qualquer para ver seu fatorial\n"))
# resultFat = fat
# fatFinal = fat
# i = fat
# if (fat==0 or fat==1):
#     print(f"O fatorial de {fat} é igual a 1\n")
# else:
#     while i>=2:
#         fat = fat-1
#         resultFat*=fat
#         i-=1
# print(f"O fatorial de {fatFinal} é igual a {resultFat}\n")
#
# num = int(input("Insira  um número qualquer para calcular seu potencial:\n"))
# potencia = int(input("Insira o valor da potência:\n"))
# resultPotencia = num**potencia
# print(f"{num}^{potencia}={resultPotencia}\n")

# fib = int(input("Insira um valor qualquer para encontrar o valor da sua posição em Fibonacci\n"))
# resultFib = 0
# if(fib==1 or fib==2):
#     print(f"Fibonacci na posição {fib}: 1\n")
# else:
#     fib1 = 1
#     fib2 = 1
#     for i in range(2,fib,1):
#         resultFib = fib1+fib2
#         fib2 = fib1
#         fib1 = resultFib
# print(f"Fibonacci na posição {fib}: {resultFib}\n")

# aleatorio = random.randint(0,1000)
# valorAleatorio = int(input("Escolha um valor aleatório:\n"))
# while(aleatorio!=valorAleatorio):
#     if aleatorio>valorAleatorio:
#         print("O valor inserido é menor que o valor gerado pelo computador\n")
#     else:
#         print("O valor inserido é maior que o valor gerado pelo computador\n")
#
#     valorAleatorio = int(input("Escolha um valor aleatório:\n"))
#
# print("Parabéns! Você acertou!")

# opcoes = ['Pedra','Papel','Tesoura']
# escolhaComp = random.choice(opcoes)
# print("1 - Pedra\n")
# print("2 - Papel\n")
# print("3 - Tesoura\n")
# escolhaUsuario = int(input("Escolha alguma das opções:\n"))
# if(escolhaComp=='Pedra'):
#     print(f"Escolha do computador: {escolhaComp}\n")
#     if(escolhaUsuario==1):
#         print("Empate.\n")
#     elif(escolhaUsuario==2):
#         print("Você ganhou!\n")
#     else:
#         print("Você perdeu.\n")
# elif(escolhaComp=='Papel'):
#     print(f"Escolha do computador: {escolhaComp}\n")
#     if (escolhaUsuario == 1):
#         print("Você perdeu.\n")
#     elif (escolhaUsuario == 2):
#         print("Empate.\n")
#     else:
#         print("Você ganhou!\n")
# else:
#     print(f"Escolha do computador: {escolhaComp}\n")
#     if (escolhaUsuario == 1):
#         print("Você ganhou!.\n")
#     elif (escolhaUsuario == 2):
#         print("Você perdeu.\n")
#     else:
#         print("Empate.\n")

linhas = int(input("Insira o número de linhas do Triângulo de Floyd\n"))
print("")
i = 0 #numeração
j = 1 #linha
k = 0 #quantidade de números por linha
while j<=linhas:
    i+=1
    k+=1
    print(i, end=" ")
    if j==k:
        print("")
        j+=1
        k = 0
print("")

# numeros = [1,2,3,4,5]
# print(numeros)
# numeros.append(6)
# print(numeros)
# print(sum(numeros))