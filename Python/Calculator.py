
def calc(x, y, ops):

    if ops not in '+-/*':
        return 'Choose operator: "+, -, *, /"!'

    if ops == '+':
        return(str(x) + ' ' + ops + ' ' + str(y) + ' = ' + str(x + y))
    if ops == '-':
        return(str(x) + ' ' + ops + ' ' + str(y) + ' = ' + str(x - y))
    if ops == '*':
        return(str(x) + ' ' + ops + ' ' + str(y) + ' = ' + str(x * y))
    if ops == '/':
        return(str(x) + ' ' + ops + ' ' + str(y) + ' = ' + str(x / y))

while True:

	x = int(input('Birinci rəqəmi daxil edin: '))
	y = int(input('ikinci rəqəmi daxil edin: '))
	ops = input("Seçim edin +, -, *, / ")

	print(calc(x, y, ops))

