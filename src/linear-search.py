# Linear Search Algorithm
"""
Entendendo e implementando a busca linear
"""

arr = [10, 5, 11, 7, 1]
numberSearched = int(input("Enter the number to be searched: "))
resultPosition = -1
for i in range(len(arr)):
  if arr[i] == numberSearched:
    resultPosition = i
    break

if resultPosition < 0:
  print("The element was not found!")
else:
  print(f"The element found in position {resultPosition}º")