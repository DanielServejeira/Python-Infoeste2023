import os
import re
import random

def calculadora(a, b, op):
    if op == '+':
        return a+b
    if op == '-':
        return a-b
    if op == '*':
        return a*b
    if op == '/':
        if b==0:
            return "Operação inválida\n"
        else:
            return a/b

def fatorial(a):
    resultado = a
    for i in range(1,a,1):
        resultado*=i
    return resultado

def fibonacci(a):
    resultado = 1
    k = 1
    j = 1
    if a==1 or a==2:
        return 1
    else:
        for i in range(2,a,1):
            resultado = k + j
            j = k
            k = resultado
        return resultado

def floyd(a):
    print("")
    i = 1
    j = 0
    k = 0
    while i<=a:
        j+=1
        k+=1
        print(j, end=" ")
        if i==k:
            print("")
            i+=1
            k = 0
    print("\n")

def funcao(quantidadeAlunos):
    for i in range(1,quantidadeAlunos+1,1):
        nota1 = float(input(f"Insira a primeira nota do aluno {i}\n"))
        nota2 = float(input(f"Insira a segunda nota do aluno {i}\n"))
        media = (nota1 + nota2)/2
        print(f"Média do aluno {i}: {media}\n")

# operacao = input("Insira a operação desejada\n")
# x = float(input("Insira o valor de x\n"))
# y = float(input("Insira o valor de y\n"))
# print(f"{x}{operacao}{y} = {calculadora(x, y, operacao)}\n")
#
# fat = int(input("Insira um número para calcular seu fatorial\n"))
# print(f"{fat}! = {fatorial(fat)}\n")
#
# fib = int(input("Insira uma posição para ver seu valor na Sequência de Fibonacci\n"))
# print(f"Resultado: {fibonacci(fib)}\n")
#
# trianguloFloyd = int(input("Insira o valor de linhas do Triângulo de Floyd\n"))
# floyd(trianguloFloyd)
#
# alunos = int(input("Insira a quantidade de alunos para calcular a média\n"))
# funcao(alunos)
#
padraoTelefone = r"^\(\d{2}\)\d{5}-\d{4}$"
telefone = "(18)98185-0072"
resultadoTelefone = re.match(padraoTelefone, telefone)
if resultadoTelefone:
    print("Norma de telefone correspondente.\n")
else:
    print("Norma de telefone não correspondente.\n")

padraoData = r"^\d{2}/\d{2}/\d{4}$"
data = "24/10/2023"
resultadoData = re.match(padraoData, data)
if resultadoData:
    print("Norma de data correspondente.\n")
else:
    print("Norma de data não correspondente.\n")

padraoEmail = r"^[a-zA-z0-9._]{1,}@\w{1,}.[A-Za-z]{2,}$"
email = "daniel@gmail.com"
resultadoEmail = re.match(padraoEmail, email)
if resultadoEmail:
    print("Norma de email correspondente.\n")
else:
    print("Norma de email não correspondente.\n")

cpf = "51585983236"
cpf_format = re.sub(r"(\d{3})(\d{3})(\d{3})(\d{2})", r"\1.\2.\3-\4", cpf)
print(cpf_format)

data = '03022004'
data_format = re.sub(r'(\d{2})(\d{2})(\d{4})', r'\1/\2/\3', data)
print(data_format)

fone = '18988092722'
fone_format = re.sub(r'(\d{2})(\d{5})(\d{4})', r'(\1)\2-\3', fone)
print(fone_format)

new = re.sub('abc', '000', 'ABC156 385abcuiA tsta74abc', 2, re.IGNORECASE)
print(new)
