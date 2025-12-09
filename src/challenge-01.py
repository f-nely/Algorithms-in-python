"""
Dado uma lista de pessoas, as armazene em um array e as exibam em uma única linha separadas por espaço
"""

t = int(input())

people = list()
for i in range(t):
  person = input()
  people.append(person)

for p in people:
  print(p, end=" ")

