numbersArr = list()
sizeArr = int(input("Enter the size of the array: "))

for i in range(sizeArr):
  valueArr = int(input(f"Enter the value of the matrix in position {i}: "))
  numbersArr.append(valueArr)

print("Array: ", numbersArr)