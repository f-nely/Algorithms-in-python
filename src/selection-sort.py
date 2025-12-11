"""
Algoritmos de ordenação: selection sort
"""

arr = [10, 5, 11, 7, 1]
""" sizeArr = len(arr)
for i in range(sizeArr):
  lowestIndex = i
  for j in range(int (i + 1), sizeArr):
    if arr[j] < arr[lowestIndex]:
      lowestIndex = j
  temp = arr[lowestIndex]
  arr[lowestIndex] = arr[i]
  arr[i] = temp
  print("Vetor: ", arr) """

""" vet = [15, 10, 5, 7, 0, 1]
def selection_sort(arr):
  size = len(arr)
  for j in range(size - 1):
    min_index = j
    for i in range(j, size):
      if arr[i] < arr[min_index]:
          min_index = i
    if arr[j] > arr[min_index]:
      aux = arr[j]
      arr[j] = arr[min_index]
      arr[min_index] = aux
  
selection_sort(vet)
print(vet) """

def selection_sort(arr):
  for i in range(0, len(arr) - 1):
    cur_min_idx = i
    for j in range(i + 1, len(arr)):
      if arr[j] < arr[cur_min_idx]:
        cur_min_idx = j
    arr[i], arr[cur_min_idx] = arr[cur_min_idx], arr[i]    

vet = [2, 6, 5, 1, 3, 4]
selection_sort(vet)
print(vet)