num1 = int(input("Entrt 1 : "))
operator =input("Entrt + - * / : ")
num2 =int(input("Entrt 1 : "))

statement = ""
results = 0

if operator == "+" :
    results = num1 + num2
    statement = "addition result is "
elif operator == "-" :
    results = num1 - num2 
    statement = "subtraction result is "
elif operator == "*" :
    results = num1 * num2 
    statement = "multiplication result is "
elif operator == "/" :
    results = num1 / num2
    statement = "divison result is "
else :
       results = ""
       statement = "soory i dont understand"

print(statement + str(results))            