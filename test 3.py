# крутой калькулятор 1.0
what = input( "Что делать надо?(+, -, *): " )
a = float( input("Введи первую цифру: ") )
b = float( input("Введи второе число: ") )

if what == "+":
    c = a + b
    print("рЕзультатик :" + str (c))
elif what == "-":
    c = a - b
    print("рЕзультатик :" + str (c))
if what == "*":
    c = a * b
    print("рЕзультатик :" + str (c))
else:
    print("Фу переделывай!" )

    input()