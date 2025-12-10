"""
Dado uma lista de pessoas, as armazene em um array, em seguida leia mais uma pessoa e exibida a posição dela dentro do array. Caso a pessoa não for localizada, retorne -1.
"""

t = int(input())

people = list()
for i in range(t):
  person = input("")
  people.append(person)

valueSearched = input("")
position = -1
for i in range(t):
  if people[i] == valueSearched:
    position = i
    break

print(position)




