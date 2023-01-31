##Задача 2
##Найдите сумму цифр трехзначного числа.
##Пример:

##123 -> 6 (1 + 2 + 3)
##100 -> 1 (1 + 0 + 0)

number = int(input("Введите трехзначное число: "))

third = (number % 10)
second = ((number // 10) %10)
first = (number // 100)

print(first+second+third)

sum = first + second + third

print (f"Сумма цифр в числе {number} равна {first} + {second} + {third} = {sum}")