""" x = 3
y = float(3)
print(x,y)
values = [1,2.23,5,7,2,30,15]
print(values)
for i in values:
    print(values[0])
    print(values[7]) """
""" day_of_the_week = input("What day is it?")
if day_of_the_week == "Friday":
    print("correct")
else:
    print("incorrect") """
""" test = input('How many letters in test?')
if test == '4':
    print('Correct')
else:
    print('Incorrect')
x = "test"
y= x.split( )
z = y[0]
print(y)
print(z) """
""" temp = 75
if temp > 68:
    print('warm')
elif temp == 68:
    print('perfect')
else:
    print('cold') """
##odd or even number
""" number = input("Number?")
if int(number) % 2 == 0:
    input("even")
else:
    input("odd") """

""" values = [0,15,20,25]
input(values) """
##tipcalculator
""" initialbill = input("What is your bill?")
service = input("How was the service?")
if service == ("bad"):
    input("0%")
    input(1 * (initialbill * 1))
elif service == ("okay"):
    input("15%")
    input(float(initialbill) * (1 + (0.01 * 15)))
    x = round(114.99999999999999)
    print(x)
elif service == ("good"):
    input("20%")
    input(float(initialbill) * (1 + (0.01 * 20)))
elif service == ("great"):
    input("25%")
    input(float(initialbill) * (1 + (0.01 * 25))) """

##Factor calculator
""" number = (input("Pick a number"))
for x in range(int(number)):
    if (x) > 0  and (int(number) % x == 0):
        input(x) """
##GCF calculator

number_x = int(input("Pick a number"))
number_y = int(input("Pick a second number"))
list_i = []
for i in range(2, min(int(number_y), int(number_x)) + 1):
    if ((int(number_x)) % i == 0) and ((int(number_y)) % i == 0):
        list_i.append(i)

print(max(list_i))