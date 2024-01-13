# Variables
'''
if we want to use value in one place,
then directly use the value
'''
print(10)
print(10+20)

'''
if we want to use value in multiple places,
then assign the value to a variable 
'''
x = 10
print(x)
print(x+20)

res = x+20
print(res)
print(res+100)


print("Addition is : ", 10+20)


# Ideal approach

x = 40
y = 50
res = x+y
print("Addition is : ", res)
res = x-y
print("Subtraction is : ", res)
mul = x*y
print("Multiplication is : ", res)

x = 10
y = 20
res = x+y
print("Addition is : ", res)

# Syntax of for loop
'''
for var in <sequence>:
    # body 
                      0123456789  : Indexing
#Sequence:  String   "Hello World"
            List     [10,43,12,65,23]
            Tuple    [1,5,3,7,3,1,7]
            range    range(1,101) 
            ---------------------------
            bytearray
            buffers
'''

print("-----Single usage------")
           # 0123456789
for char in 'Hello World':
    print("Character : ", char)

print("-----Multiple usage-----")

msg = 'Hello World'
for char in msg:
    print("Character : ", char, char.upper())

print("Further usage : ", msg)