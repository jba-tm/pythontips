# 15. Object introspection
from pprint import pprint

print('15.1. dir')
my_list = [1,2,3,]

print(dir(my_list))

print('\n15.2. type and id')

print(type(''))
# Output: <type 'str'>

print(type([]))
# Output: <type 'list'>

print(type({}))
# Output: <type 'dict'>

print(type(dict))
# Output: <type 'type'>

print(type(3))
# Output: <type 'int'>


name = 'Yasoob'
print(id(name))


print('\n15.3. inspect module')
import inspect
pprint(inspect.getmembers(str))
print(name.translate('o'))