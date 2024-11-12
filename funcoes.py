# Função lambda

#dobrar = lambda num : num * 2

#print(dobrar(num=int(input("Digite o número: "))))

# ----------------------------------

#checarIdade = lambda idade : "Maior de idade" if idade >= 18 else "Menor de idade"

#print(checarIdade(idade=10))
#print(checarIdade(idade=29))

# ----------------------------------

# checarNum = lambda n : "Par" if n % 2 == 0 else "Ímpar"

# while True:
#     menu = input("""
# Escolha uma opção:
# 1 - Checar um número
# 2 - Sair
# """)
#     match menu:
#         case "1":
#             print(checarNum(n=int(input("Digite o número: "))))
#         case "2":
#             print("Fim do programa...")
#             break
#         case _:
#             print("Opção inválida!")

# ---------------------------------

semaforo = lambda cor : "Siga" if cor.lower() == "verde" else "Atenção" if cor.lower() == "amarelo" else "Pare" if cor.lower() == "vermelho" else "Cor inválida"

print(semaforo(cor="verde"))
print(semaforo(cor="amarelo"))
print(semaforo(cor="vermelho"))
print(semaforo(cor="Vermelho"))
print(semaforo(cor="roxo"))