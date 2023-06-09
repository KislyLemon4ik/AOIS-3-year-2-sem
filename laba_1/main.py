from converting import converting, refund
from amount import amount
from diff import diff
from mult import mult
from splitting import splitting
from fl import floating_sum, float_to_decimal_conversion, convert_string_to_list
import time

while True:

    print("Выберите операцию:")
    print("0 --> Выход")
    print("1 --> Сумма")
    print("2 --> Разность")
    print("3 --> Произведение")
    print("4 --> Деление")
    print("5 --> Получить сумму")
    choice = input("--> ")
    if choice == "0":
        break
    elif choice == '1':
        num1 = int(input("Введите первое число: "))
        num2 = int(input("Введите второе число: "))
        print(converting(num1), '+', converting(num2), '=', amount(num1, num2))
        print(num1, '+', num2, '=', refund(amount(num1, num2)))
    elif choice == '2':
        num1 = int(input("Введите первое число: "))
        num2 = int(input("Введите второе число: "))
        print(converting(num1), '-', converting(num2), '=', diff(num1, num2))
        print(num1, '-', num2, '=', refund(diff(num1, num2)))
    elif choice == '3':
        num1 = int(input("Введите первое число: "))
        num2 = int(input("Введите второе число: "))
        print(converting(abs(num1)), '*', converting(abs(num2)), '=', mult(int(abs(num1)), int(abs(num2))))
        print(abs(num1), '*', abs(num2), '=', refund(mult(int(abs(num1)), int(abs(num2)))))
    elif choice == '4':
        num1 = int(input("Введите первое число: "))
        num2 = int(input("Введите второе число: "))
        print(converting(abs(num1)), '/', converting(abs(num2)), '=', splitting(int(abs(num1)), int(abs(num2))))
        print(num1, '/', num2, '=', refund(splitting(int(abs(num1)), int(abs(num2)))))
    elif choice == '5':
        num1 = int(input("Введите первое число: "))
        num2 = int(input("Введите второе число: "))
        print(convert_string_to_list(floating_sum(max(num1, num2), min(num1, num2))))
        print(float_to_decimal_conversion(floating_sum(max(num1, num2), min(num1, num2))))

    time.sleep(2)