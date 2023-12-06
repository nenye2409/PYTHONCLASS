price1 = 45000
price2 = 30000
price3 = 85000
report = 'I sold 2 shirt for {}, a shoe for {}, a suit for {}'
print(report.format(price1,price2,price3))
print(f'I sold 2 shirt for {price2}, a shoe for {price1} and a suit for {price3}')
word = 'Python is fun'
print(word.upper())
print(word.lower())
print(word.capitalize())
print(word.title())
print(word.split())

num1 = int(24.10)
print(num1)
print(float(num1))
print(str(num1))
print(str(10.2))
print(int('45'))

#name = input('Enter your name:')
#age = int(input('Enter your age:'))

#Arithmetic operators
num1 = int(input('Enter first number:'))
num2 = int(input('Enter second number:'))
print(f'{num1} + {num2} = {num1 + num2}') 
print(f'{num1} - {num2} = {num1 - num2}')
print(f'{num1} * {num2} = {num1 * num2}')
print(f'{num1} / {num2} = {num1 / num2}')
print(f'{num1} % {num2} = {num1 % num2}')
print(f'{num1} // {num2} = {num1 // num2}')
print(f'{num1} ** {num2} = {num1 ** num2}')

# exercise
# Mr bob bought p bags for 500000 and sold each bag aat 20000
# a what is the number of bags bought b. what is the profit
costprice = 500000
sellingprice = 20000
number_of_bags = costprice / sellingprice
profit = (number_of_bags * sellingprice) - costprice
print(f'''The number of bags bought is {number_of_bags} and Mr bob's profit is {profit}''')

