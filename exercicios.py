# #### Inteiros (`int`)
'''
# 1. Escreva um programa que soma dois números inteiros inseridos pelo usuário.
numero_01 = int(input("Escreva um Numero inteiro: "))
numero_02 = int(input("Escreva um outro Numero inteiro: "))
resultado = numero_01 + numero_02
print(f"O {numero_01} mais o número {numero_02} é igual a {resultado}")

# 2. Crie um programa que receba um número do usuário e calcule o resto da divisão desse número por 5.
numero_01 = int(input("Escreva um Numero inteiro: "))
resultado = numero_01  % 5
print(f"O {numero_01} dividido pelo número 5 tem como resto o número {resultado}")


# 3. Desenvolva um programa que multiplique dois números fornecidos pelo usuário e mostre o resultado.
numero_01 = int(input("Escreva um Numero inteiro: "))
numero_02 = int(input("Escreva um outro Numero inteiro: "))
resultado = numero_01 * numero_02
print(f"O {numero_01} multiplicado pelo número {numero_02} é igual a {resultado}")

# 4. Faça um programa que peça dois números inteiros e imprima a divisão inteira do primeiro pelo segundo.
numero_01 = int(input("Escreva um Numero inteiro: "))
numero_02 = int(input("Escreva um outro Numero inteiro: "))
resultado = numero_01 // numero_02
print(f"O {numero_01} dividido pelo número {numero_02} é igual a {resultado}")

# 5. Escreva um programa que calcule o quadrado de um número fornecido pelo usuário.
numero_01 = int(input("Escreva um Numero inteiro: "))
resultado = numero_01 ** 2
print(f"O quadrado do número {numero_01} é {resultado}")

# #### Números de Ponto Flutuante (`float`)

# 6. Escreva um programa que receba dois números flutuantes e realize sua adição.
numero_01 = float(input("Escreva um Numero inteiro: "))
numero_02 = float(input("Escreva um outro Numero inteiro: "))
resultado = numero_01 + numero_02
print(f"O {numero_01} mais o número {numero_02} é igual a {resultado}")

# 7. Crie um programa que calcule a média de dois números flutuantes fornecidos pelo usuário.
numero_01 = float(input("Escreva um Numero inteiro: "))
numero_02 = float(input("Escreva um outro Numero inteiro: "))
media = (numero_01 + numero_02) / 2
print(f"A média de  {numero_01} e {numero_02} é igual a {resultado}")

# 8. Desenvolva um programa que calcule a potência de um número (base e expoente fornecidos pelo usuário).
base = float(input("Digite a base: "))
expoente = float(input("Digite o expoente: "))
resultado = base ** expoente
print(f"{base} elevado a {expoente} é {resultado:.2f}")

# 9. Faça um programa que converta a temperatura de Celsius para Fahrenheit.
celsius = float(input("Digite a temperatura em Celsius: "))
fahrenheit = celsius * 9 / 5 + 32
print(f"{celsius:.2f}°C equivale a {fahrenheit:.2f}°F")

# 10. Escreva um programa que calcule a área de um círculo, recebendo o raio como entrada.
import math
raio = float(input("Digite o raio do círculo: "))
area = math.pi * (raio ** 2)
print(f"A área do círculo com raio {raio:.2f} é {area:.2f}")
'''
# #### Strings (`str`)

# 11. Escreva um programa que receba uma string do usuário e a converta para maiúsculas.
nome = input("Digite o nome: ")
print(nome.upper())

# 12. Crie um programa que receba o nome completo do usuário e imprima o nome com todas as letras minúsculas.
nome = input("Digite o nome Completo: ")
print(nome.lower())
# 13. Desenvolva um programa que peça ao usuário para inserir uma frase e, em seguida, imprima esta frase sem espaços em branco no início e no final.
frase = input("Digite uma frase: ")
frase_sem_espacos = frase.strip()
print(f"Frase sem espaços: '{frase_sem_espacos}'")

# 14. Faça um programa que peça ao usuário para digitar uma data no formato "dd/mm/aaaa" e, em seguida, imprima o dia, o mês e o ano separadamente.
data = input('Insira uma data no formato dd/mm/aaaa')
data = data.split('/')
print(f"Dia: {data[0]} Mês: {data[1]} ano: {data[2]}")


# 15. Escreva um programa que concatene duas strings fornecidas pelo usuário.
string1 = input("Digite uma string: ")
string2 = input("Digite outra string: ")
resultado = string1 + string2
print(f"A concatenação das strings é: '{resultado}'")

# #### Booleanos (`bool`)

# 16. Escreva um programa que avalie duas expressões booleanas inseridas pelo usuário e retorne o resultado da operação AND entre elas.
# 17. Crie um programa que receba dois valores booleanos do usuário e retorne o resultado da operação OR.
# 18. Desenvolva um programa que peça ao usuário para inserir um valor booleano e, em seguida, inverta esse valor.
# 19. Faça um programa que compare se dois números fornecidos pelo usuário são iguais.
# 20. Escreva um programa que verifique se dois números fornecidos pelo usuário são diferentes.

# #### try-except e if

# 21: Conversor de Temperatura
# 22: Verificador de Palíndromo
# 23: Calculadora Simples
# 24: Classificador de Números
# 25: Conversão de Tipo com Validação