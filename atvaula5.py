# Faça uma função que recebe o nome da pessoa, uma hora do dia (ignore os minutos) e faça um cumprimento de acordo com a hora, por exemplo: "Bom dia, fulano", "Boa tarde, fulano", "Boa noite, fulano".

def saudacao(nome:str, hora:int):
    if hora < 0 or hora > 23:
        return "Horário Inválido"
    elif hora >= 4 and hora <= 12:
        return f"Bom dia, {nome}!"
    elif hora >= 13 and hora <= 18:
        return f"Boa tarde, {nome}!"
    else:
        return f"Boa noite, {nome}!"

nome = input("Digite seu nome: ")
hora = int(input("Digite a hora em inteiro: "))

print(saudacao(nome=nome,hora=hora))