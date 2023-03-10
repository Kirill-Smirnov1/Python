# 3. Вы пользуетесь общественным транспортом? Вероятно, вы расплачивались за проезд и получали билет с номером.
# Счастливым билетом называют такой билет с шестизначным номером, где сумма первых трех цифр равна сумме последних трех. 
# Т.е. билет с номером 385916 – счастливый, т.к. 3+8+5=9+1+6. Вам требуется написать программу, которая проверяет счастливость билета.
# in
# 385916
# out
# yes
# in
# 123456
# out
# no
n = int(input("Введите номер билета:"))
x1 = n // 1000
x2 = n % 1000
summa1 = 0
summa2 = 0
while x1 > 0 and x2 > 0:
    y1 = x1 % 10
    y2 = x2 % 10
    summa1 = summa1 + y1
    summa2 = summa2 + y2
    x1 = x1 // 10
    x2 = x2 // 10
if summa1 == summa2:
    print(f'Билет с номером {n} счастливый!')
else:
    print(f'Билет с номером {n} несчастливый.')
