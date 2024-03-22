entrada = input("Informe a palavra: ")
checker = list(entrada)

validation = [ ]

for letter in range(len(checker) -1, -1, -1):
   validation.append(checker[i])

if validation == checker:
   print(f"A palavra informada é um palíndromo!/n{checker} = {validation}!")

else:
   print("A palavra digitada não é um palíndromo.")
