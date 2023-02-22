result = None
operand = None
operator = None 
wait_for_number = True

while True:
    try:
        a=input()
        operand=float(a)
    except ValueError:
        print(f'{a} is not a number. Try again')
        continue
    
    
    while True:
        operator=input()
        if operator not in ('+', '-', '*', '/', '='):
            print(f'{operator} is not + or - or * or /. Try again')
            continue
        else:
            break
    
    if operator=='+':
        if result==None:
            result=0
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
    elif operator=='=':
        print(f'Result:{result}')
        break