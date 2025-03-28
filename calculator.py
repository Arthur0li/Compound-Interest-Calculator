"""Compound Interest Calculator / Calculadora de Juros Compostos

English:
This module calculates the compound interest based on user inputs.
It supports both English and Portuguese languages.
Inputs:
    - Capital: float - the initial amount of money.
    - Tax: float - the monthly interest rate in percentage (which is converted to a decimal).
    - Months: int - the number of months for the calculation.
Calculation:
    The final amount is computed using the formula:
        amount = capital * (1 + tax) ** months
Usage:
    Run the script and follow the prompts for language selection and data input.

Português:
Este módulo calcula os juros compostos com base nas entradas do usuário.
Ele suporta os idiomas inglês e português.
Entradas:
    - Capital: float - o valor inicial de dinheiro.
    - Tax: float - a taxa de juros mensal em porcentagem (que é convertida para decimal).
    - Months: int - o número de meses para o cálculo.
Cálculo:
    O valor final é calculado usando a fórmula:
        amount = capital * (1 + tax) ** months
Uso:
    Execute o script e siga as instruções para selecionar o idioma e inserir os dados.
"""


from math import pow

print('This is a compound interest calculator. / Esta é uma calculadora de juros compostos.')

language = input('Type "en" for English or "pt" for Portuguese / Digite "en" para inglês ou "pt" para português: ').lower()
while language not in ['en', 'pt']:
    print('Invalid option / Opção inválida.')
    language = input('Type "en" for English or "pt" for Portuguese / Digite "en" para inglês ou "pt" para português: ').lower()

if language == 'en':
    msg_capital = "Enter the amount of your capital: "
    msg_tax = "Enter the monthly interest rate (in percentage): "
    msg_months = "Enter the number of months: "
    msg_invalid = "You entered an invalid number, please enter a value greater than 0: "
    msg_result = "This is the return: "
else:
    msg_capital = "Digite o valor do seu capital: "
    msg_tax = "Digite a taxa de juros mensal (em porcentagem): "
    msg_months = "Digite o número de meses: "
    msg_invalid = "Você inseriu um número inválido, insira um valor maior que 0: "
    msg_result = "Este é o retorno: "

capital = float(input("\n" + msg_capital))
while capital <= 0:
    capital = float(input(msg_invalid))

tax = float(input(msg_tax))
while tax <= 0:
    tax = float(input(msg_invalid))
tax = tax / 100 

months = int(input(msg_months))
while months <= 0:
    months = int(input(msg_invalid))

amount = capital * pow(1 + tax, months)

print(f"{msg_result}{amount:.2f}")
