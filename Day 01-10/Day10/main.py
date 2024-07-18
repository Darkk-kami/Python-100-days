from art import logo
from func import operations

print(logo)

stop_calc = False

num1 = float(input('what is the first number?:'))

for sym in operations:
    print(sym)

while not stop_calc:   
    operator = input("Pick an operation: ")
    num2 = float(input('what is the next number?:'))

    for sym in operations:
        if operator == sym:
            fx = operations[operator]
            ans = fx(num1, num2)
    
    print(f'{num1} {operator} {num2} = {ans}')
    num1 = ans

    if input(f"Type 'y' to continue calculating with {ans} or type 'n' to exit.: ").lower() == "n":
        stop_calc = True       
 