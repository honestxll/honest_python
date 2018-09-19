char_list = ['a', 'b', 'c', 'd', 'e', 'd']

a_set = set(char_list)

print(type(a_set))

a_set.add('x')
a_set.remove('x')
a_set.discard('x')
# a_set.clear()


b_set = {'a', 'e', 'f'}

print(a_set.difference(b_set))
print(a_set.intersection(b_set))
