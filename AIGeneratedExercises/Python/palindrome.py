entrada = input("Informe a palavra: ")
checker = list(entrada)

validation = [ ]

for letter in checker:
   validation.append(letter)

if validation == checker:
   print(f"A palavra informada é um palíndromo!/n{checker} = {validation}!")