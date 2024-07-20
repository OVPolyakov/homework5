immutable_var = 1,2,True,"Hello"
print(immutable_var)
#immutable_var = 3,4, True, 'Hello'
#immutable_var[0] = 1
#print(immutable_var)
# Кортежи в Python являются неизменяемыми, поэтому при попытке их изменить будет выдавать ошибку.
mutable_list = [3,4,True, 'Hi']
print(mutable_list)
mutable_list[0] = 5
mutable_list[1] = 6
mutable_list[2] = False
mutable_list[3] = 'By'
print(mutable_list)