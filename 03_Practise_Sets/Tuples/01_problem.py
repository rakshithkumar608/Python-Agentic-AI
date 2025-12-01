# Accept 5 numbers from user, store in tuple and print sum, average, max & min

numbers = []

for i in range(5):
  n = int(input("Enter a number:"))
  numbers.append(n)

  t = tuple(numbers)

  print("Tuple:", t)
  print("Sum = ", sum(t))
  print("Average = ", sum(t)/len(t))
  print("Max = ", max(t))
  print("Min = ", min(t))