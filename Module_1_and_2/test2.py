result = None
operand = None
operator = None
wait_for_number = True
result = float(input('number '))
while wait_for_number:
    operator = input('operator ')
    if operator == "=":
        break
    elif operator == "+" or operator == "-" or operator == "*" or operator == "/":
        try:
            operand = float(input('next number '))
        except ValueError:
            print(f"{operand} is not a number. Try again")
            operand = float(input('next number '))
        if operator == "+":
            result += operand
        elif operator == "-":
            result -= operand
        elif operator == "*":
            result = result * operand
        elif operator == "/":
            result = result / operand
    else:
        print(f"{operator} is not '+' or '-' or '/' or '*'. Try again")
        continue
print(result)