# dict keys : Unique, Immutable
# Dictionary: Mutable
# set       : Mutable :  Elements inside set should be  Unique, Immutable
# list,dict,set : mutable
set1 = {1, 1, 1, 2, 3, 4, 4, 4}
print(set1)
set2 = {[1, 2, 3], {1: 1}, {1, 2, 3}}  # list dict set are mutable

# set3 = { int, float, boolean, string, tuple}
# set4 = {list, dict, set}  Not Allowed

'''
-- Elements must be immutable (int,float,boolean,string tuple)
                          -- XXX list dict set
-- Unique (Duplicates not allowed)
-- Set is mutable
-- It doesn't follow indexing.
-- It follows hashing algorithm
-- While storing elements, it wont follow any order 
-- Both homo/heterogeneous data allowed(But Immutable)

'''
# Example
s1 = {1, 2, 2, 2, 2, 4, 3, 5, 2, 7, 6}
print("Set 1 : ", s1)
# s1 = { [1, 2, 3] }  # list
# s1 = { {'eid': 100, 'name': 'Madhu'} } # dict
# s1 = {1, 2, 3, {1, 2, 3} } # int int int set

# Immutable : Elements inside set are Immutables

# Set is mutable stucture

s1 = {1, 1, 3.5, True, 'Hello', (1, 2, 3)}  # int boolean string tuple

print("Set is Mutable : ", s1)
s1 = {{1, 2, 3}, {1: 1, 2: 2}, [1, 2, 3]}  # set dict list


