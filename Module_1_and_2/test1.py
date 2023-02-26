result = None
operand = None
operator = None 
wait_for_number = True

while True:
    try:
        b=input()
        result=float(b)
        break
    except ValueError:
        print(f'{b} is not a number. Try again')
        continue


while True:

    if operator=='=':
        print(f'Result:{result}')
        break 

    while True:
        operator=input()
        if operator not in ('+', '-', '*', '/', '='):
            print(f'{operator} is not + or - or * or /. Try again')
            continue
        else:
            break

    if operator=='=':
        print(f'Result:{result}')
        break             

    while True:
        try:
            a=input()
            operand=float(a)
            break
        except ValueError:
            print(f'{a} is not a number. Try again')
            continue
    
    
    if operator=='+':
            result+=operand
    elif operator=='-':
            result-=operand
    elif operator=='*':
        result*=operand
    elif operator=='/':
        try:
            result/=operand
        except ZeroDivisionError:
            print('Delenie na 0')
    if operator=='=':
        print(f'Result:{result}')
        break 