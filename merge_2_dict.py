print("Exercise 2: Merge two Python dictionaries into one")
dict1 = {'Ten': 10, 'Twenty': 20, 'Thirty': 30}
dict2 = {'Thirty': 30, 'Fourty': 40, 'Fifty': 50}
# for i,a in dict1.items():
#     dict2[i]=a
# print(dict2)
dict1.update(dict2)
print(dict1)