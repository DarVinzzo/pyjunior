# cool calculator 2.1
what = input( "What need to do? (+, -, *, /): " )
a = float( input("Type first number: ") )
b = float( input("Type second number: ") )

if what == "+":
    c = a + b
    print("Result:" + str (c))
elif what == "-":
    c = a - b
    print("Result :" + str (c))
elif what == "*":
    c = a * b
    print("Result :" + str (c))
elif what == "/":
    c = a / b
    print("Result :" + str (c)) 

else:
    print("Something is wrong ..." )
