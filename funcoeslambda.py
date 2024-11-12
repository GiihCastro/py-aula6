# Tradicional

# numeros = [4, 180, 1986, 41, 18, 1, 25693]
# metades = []

# for numero_da_vez in numeros:
#     metades.append(numero_da_vez / 2)

# print(metades)

# ------------------------------------------

# Usando lambda

# numeros = [4, 180, 1986, 41, 18, 1, 25693]
# metades = list(map(lambda n : n / 2 , numeros))
# print(metades)

# ------------------------------------------

idades = [17, 29, 42, 35, 61, 10, 14, 7, 33]
maiores_de_idade = list(filter(lambda idade : idade >= 18, idades))
print(maiores_de_idade)