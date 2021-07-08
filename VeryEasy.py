def min (x,y):
    if ( x < y ):
        return x
    else: 
        return y 


num1 = int(input("Please enter a number: "))
num2 = int(input("Now enter another number: "))

answer = min(num1, num2)

print(f'{answer} is the minimum') 
