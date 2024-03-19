my_list = []
list2 = [50, 60, 70]

my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)

my_list.insert(1, 15)
my_list.extend(list2)

my_list.pop()
my_list.sort()

print("The index of the value 30 is:", my_list.index(30))