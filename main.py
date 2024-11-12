def somar(num1,num2):
    return num1 + num2

def subtrair(num1,num2):
    return num1 - num2

def multiplicar(num1,num2):
    return num1 * num2

def dividir(num1,num2):
    if num2 == 0:
        return "Não é possível dividir por 0"
    else:
        return num1 / num2

num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))

print(somar(num1,num2))

def checaIdade(nome:str, idade:int):
    if idade >= 18:
        return f"Olá {nome} você já pode ser preso"
    else:
        return f"Olá {nome} você vai pra FEBEM"


print(checaIdade(nome="abel", idade=29))
print(checaIdade(nome="joao", idade=14))
print(checaIdade(idade=18, nome="maria"))
print(checaIdade(nome="Ana", idade=19))
print(checaIdade(nome="qualquer coisa", idade=15))


def calcularMedia(nota1, nota2, nota3, nota4):
    return (nota1 + nota2 + nota3 + nota4 ) / 4

nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
nota3 = float(input("Digite a terceira nota: "))
nota4 = float(input("Digite a quarta nota: "))

media = calcularMedia(nota1,nota2,nota3,nota4)

if media >= 7:
    print(f"Aprovado com a média {media}")
else:
    print(f"Reprovado com a média {media}")
