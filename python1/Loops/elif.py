#if else naredba

mood = "happy"

if mood == "happy":
    print("Drago mi je da si sretan")
elif mood == "sad":
    print("Biti će bolje")
elif mood == "nervous":
    print("Smiri se")
else:
    print("Ne prepoznajem tvoje raspoloženje")

brojA = int(input("Unesi prvi broj: "))
brojB = int(input("Unesi drugi broj: "))
operation = input("Unesi aritmetičku operaciju:")

if operation == "+":
    print(brojA + brojB)
elif operation == "-":
    print(brojA - brojB)
elif operation == "*":
    print(brojA * brojB)
elif operation == "/":
    print(brojA / brojB)

