def addition(x,y):
  return(x + y)
def subtraction(x,y):
  return(x - y)
def multiplication(x,y):
  return(x * y)
def division(x,y):
  retrun(x / y)

number_1 = int(input("Please enter first number:"))

print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")

choice = input("Please select your desired option by pressing (1/2/3/4)")

number_ 2 = int(input("Please enter second number:"))

if choice == 1:
  print(number_1, "+", number_2, "=", addition(number_1, number_2))
if choice == 2:
  print(number_1, "-", number_2, "=", subtraction(number_1, number_2))
if choice == 3:
  print(number_1, "x", number_2, "=", multiplication(number_1, number_2))
if choice == 4:
  print(number_1, "/", number_2, "=", division(number_1, number_2))
