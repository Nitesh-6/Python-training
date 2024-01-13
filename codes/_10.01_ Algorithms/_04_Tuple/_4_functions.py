# tuple()
# count()
# index()

list1 = [1, 2, 3, 4]
print("Before : ", list1, type(list1))
tup1 = tuple(list1)
print("After : ", tup1, type(tup1))


t1 = (10, 43, 2, 532, 53, 64, 24, 25, 53)
print("Iterate the tuple")
for each in t1:
    print(each)

le = len(t1)
for ind in range(le):  # range(9)
    print(ind, " : ", t1[ind])


# Find index of 64
t1 = (10, 43, 2, 532, 53, 64, 24, 25, 24, 10,  53, 10)

for ind in range(len(t1)):
    if t1[ind] == 64:
        print("Index is : ", ind)

print("Count : ", t1.count(10))

print("Index : ", t1.index(64))


list1 = [1, 2, 3]
print("Before : ", list1)
list1.append(10)
print("After  : ", list1)
# return type

# pop() remove()
print("List pop :", list1.pop(2))
print(list1)
print("List remove :", list1.remove(10))
print(list1)


'''
list vs tuple ****
-----------------
1. list occupies 2 memory blocks, tuple occupies 1 memory block 
2. tuple is faster compare to list during data retrieval operations 
3. For frequent insert, update, delete operations use list 
   For a structure, it should be used as is means go for tuple 
4.  list is mutable and tuple is immutable 
5. Though tuple is immutable, if list presents inside tuple we can perform
    CRUD operations on nested list.
'''