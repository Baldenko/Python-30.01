##Задача 8
##Требуется определить, можно ли от шоколадки размером n × m долек отломить k долек, если разрешается сделать один разлом по прямой
## между дольками (то есть разломить шоколадку на два прямоугольника).
##Пример:

##3 2 4 -> yes
##3 2 1 -> no

n = int(input("Сколько долек в длину? "))
m = int(input("Сколько долек в ширину? "))

if n>1 and m>1:
    print ("Ломайте")
else:
    print ("Жуйте так, не ломая")