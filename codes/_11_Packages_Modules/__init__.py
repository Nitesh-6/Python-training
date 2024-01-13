char = chr(97)  # here 97 is the ASCII value it converts to char
print(char)
val = "sai"
val = ascii(val)  # it converts the value to object
print(val)
num = bin(20)  # it converts the number to binary
print(num)
num1 = [1, 2, 3, 4]
num2 = [2, 3, 4, 5]  # it applies the function to each and every value that iterates
val = list(map(lambda n1, n2: n1 + n2, num1, num2))  # lambda is an anonymous function which has no name
print(val)
val = list(filter(lambda x: x % 2, num1))  # it accepts two arguments function, iterable(list, tuple, sets) and return true/false
print(val)
