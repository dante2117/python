
number_one = float(input("Введите x: "))

number = int(input("Введите количество операций: "))

for i in range(number):

 operation = input("\n Введите операцию: \n + Сложение \n - Вычитание \n * Умножение \n / Деление \n")


 if(operation == "+"):
    number_two = float(input("Введите y: "))
    number_one = number_one+number_two
    print(f"Ответ: {number_one}")

 elif(operation == "-"):
    number_two = float(input("Введите y: "))
    number_one = number_one-number_two
    print(f"Ответ: {number_one}") 

 elif(operation == "*"):
    number_two = float(input("Введите y: "))
    number_one = number_one*number_two
    print(f"Ответ: {number_one}") 

 elif(operation == "/"):
   while (1 == 1):
     number_two = float(input("Введите y: "))
     if (number_two == 0):
         print("На 0 делить нельзя! Вернитесь на шаг назад")
     else:
         number_one = number_one/number_two
         print(f"Ответ: {number_one}")  
         break  
 else:
   print("Такой операции не существует")
