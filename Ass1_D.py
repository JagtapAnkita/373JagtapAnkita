#Display in Integet and float

N1=int(input("Enter first number: "))
N2=int(input("Enter first number: "))

print("1st number: ",N1)
print("2nd number:",N2)

Div=N1/N2
print("Division in int: ",int(Div))
print("Division in float: ",float(Div))

#creating list and operation on it.

my_list=[]
print("Empty list: ",my_list)

my_list.insert(0,5)
my_list.insert(1,10)
my_list.insert(0,6)

print("After inssertion: ",my_list)

my_list.remove(6)
my_list.append(9)
my_list.append(1)
my_list.sort()
print("List is: ",my_list)

my_list.pop()
my_list.reverse()
print("List is: ",my_list)

