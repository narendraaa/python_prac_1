diction = {'x':10, 'b':20, 'c':30,'d':5,'a':1}
item = list(diction.items())
# print(item)
for i in range(len(item)):
    for j in range(len(item)-i-1):
        if item[j][0] > item[j+1][0]:
            item[j],item[j + 1] = item[j+1],item[j]
sorted_dict = {}
for k,v in item:
    sorted_dict[k]=v
print(f'sorted by Keys : {sorted_dict}')
print()
####SOTED BY VLAUES
section = {'x':10, 'b':20, 'c':30,'d':5,'a':1}
item = list(section.items())
# print(item)
for i in range(len(item)):
    for j in range(len(item)-i-1):
        if item[j][1] > item[j+1][1]:
            item[j],item[j + 1] = item[j+1],item[j]
sorted_dict1 = {}
for k,v in item:
    sorted_dict1[k]=v
print(f'SORTED BY VALUES : {sorted_dict1}')
