from package1 import add_sub_mult_div

print("Введите действие:")
action = input()

if action == "add":
    print("Введите первое число:")
    a = int(input())
    print("Введите второе число:")
    b = int(input())
    print("a + b = " + add_sub_mult_div.add(a, b))
elif action == "subtraction":
    print("Введите первое число:")
    a = int(input())
    print("Введите второе число:")
    b = int(input())
    print("a - b = " + add_sub_mult_div.subtraction(a, b))
elif action == "mulptiply":
    print("Введите первое число:")
    a = int(input())
    print("Введите второе число:")
    b = int(input())
    print("a * b = " + add_sub_mult_div.multiple(a, b))
elif action == "division":
    print("Введите первое число:")
    a = int(input())
    print("Введите второе число:")
    b = int(input())
    if b == 0:
        print("На ноль делить нельзя")
    print("a // b = " + add_sub_mult_div.div(a, b))
elif action == "log2":
    print("Введите число:")
    a = int(input())
    if a < 0:
        print("Число a не может быть отрицательным")
        exit(200)
    print("log2(a) = ", add_sub_mult_div.logariphm_two(a))
elif action == "logE":
    print("Введите число:")
    a = int(input())
    if a < 0:
        print("Число a не может быть отрицательным")
        exit(200)
    print("logE(a) = ", add_sub_mult_div.logariphm_natural(a))
elif action == "sqrt":
    print("Введите число:")
    a = int(input())
    if a < 0:
        print("Число a не может быть отрицательным")
        exit(200)
    print("sqrt(a) = ", add_sub_mult_div.sqrt(a))
elif action == "sqrt3":
    print("Введите число:")
    a = int(input())
    print("sqrt3(a) = ", add_sub_mult_div.sqrt3(a))
elif action == "sqrtN":
    print("Введите число a:")
    a = int(input())
    print("Введите степень корня:")
    n = int(input())
    if n % 2 == 0 and a < 0:
        print("Число a не может быть отрицательным")
    print("sqrtN(a) = ", add_sub_mult_div.sqrtN(a, n))
