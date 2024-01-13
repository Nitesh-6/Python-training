
'''
# REQ: so and so......
           1. CRUD     :  CREATE RETRIEVE UPDATE DELETE
           2. STATE    :  (Data types, Data structures)
           3. BEHAVIOR :  (Operators, DM, Loops)
'''
eid = 10
sal = 10.5
is_bool = True
ename = 'Madhu Nettem'  # '@!#!@#3213213{}<>?<VCXVEWREWRSDFSDF'

e_ids = [14, 12, 52, 33, 33, 14, 25, 86]  #   []  ()  {}
     #   0    1   2   3   4   5   6   7
print("List data structure :", e_ids)

'''List properties'''

'''
List properties:
==================
# 1. Follows indexing mechanism while storing elements(Sequence)
# 2. List is Mutable ***
# 3. List allows Duplicate elements
# 4. Maintains Insertion order wrt Memory 
# 5. List will allow both Homogeneous and Heterogenous data
'''

# 1. Follow indexing mechanism
list1 = [12, 22, 13, 54, 35]
      #  0   1    2   3   4

print("List : ", list1)
print("List : ", list1[1])  # Indexing
print("List : ", list1[1:2])  # Slicing


# 2. List is Mutable ***
print("----List is MUTABLE-----")  # Insert, Update, Delete ops
        # 0   1   2   3   4   5
list1 = [12,  22, 13, 54, 35]
print("Before list : ", list1)
list1[2] = 300   # Update
print("After list1  : ", list1)
list1.insert(1, 100)
print("After list2  : ", list1)
del list1[3]
print("After list3  : ", list1)
del list1

# 3. List will allow both homogeneous and heterogenous data
    # Homo
print("----------Homogeneous---------")
list1 = [1, 2, 3, 4, 5, 6]
print('Integers is list : ', list1)

list1 = [1.5, 3.2, 5.6, 4.8]
print('Float is list   : ', list1)

list1 = [True, False, True, False]
print('Boolean is list : ', list1)


'''
| 1 2 3 |
| 4 5 6 |   M[2][2]  = 5
| 7 8 9 |

 [1, 2, 3]
 [4, 5, 6], 
 [7, 8, 9]   M[1][2]  = 2
 '''
list1 = ['hello', 'world', 'welcome', 'python']
print('Strings is list : ', list1)

print("Index value : ", list1[1])
print("Index value : ", list1[1][2])

list1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print('Lists   in list : ', list1)
print('Lists   in list : ', list1[0])
print('Lists   in list : ', list1[2][0])

list1 = [(1, 2, 3), (4, 5, 6), (7, 8, 9)]
print('Tuples  in list : ', list1)
print('Tuples  in list : ', list1[1])
print('Tuples  in list : ', list1[2][1])

list1 = [{1: 1, 2: 2}, {'id': 100, 'name': 'Madhu'}]
print('Dict    is list : ', list1)

list1 = [{1, 2, 3}, {4, 5, 6}]
print('Set is list : ', list1)

# Heterogenous Data
list1 = [100, 14.5, False, 'Hello', [1, 2, 3], (1, 2, 3), {1: 1, 2: 2}, {1, 2, 3}]
   #       0    1     2       3         4          5            6           7
   #                                             list1[5][1]        list1[6][2]
print("---Hetero-------", list1)
list2 = [1, 2, 3]
list3 = [True, 1, 1.5]




# 4. List allows duplicate elements
list1 = [10, 10, 20]
print("Duplicates in list : ", list1)

# 5. Maintains Insertion order wrt memory location
list1 = [1, 2, 3, 4, 5, 6]
print("Insertion order: ", list1)





'''
When to use list data structure:
---------------------------------
- Handle group of elements
- Homogeneous/Heterogeneous, 
- Mutable Structures **
- With Duplicate values 
'''
