# 16. Comprehensions

print('16.1. list comprehensions')

multiples = [i for i in range(30) if i % 3 == 0]
print(multiples)

print('\n16.2. dict comprehensions')
mcase = {'a': 10, 'b': 34, 'A': 7, 'Z': 3}

mcase_frequency = {
    k.lower(): mcase.get(k.lower(), 0) + mcase.get(k.upper(), 0)
    for k in mcase.keys()
}
print(mcase_frequency)

# mcase_frequency == {'a': 17, 'z': 3, 'b': 34}
inverse = {v: k for k, v in mcase.items()}
print(inverse)

print('\n16.3. set comprehensions')
squared = {x**2 for x in [1, 1, 2]}
print(squared)

print('\n16.4. generator comprehensions')
multiples_gen = (i for i in range(30) if i % 3 == 0)
print(multiples_gen)
# Output: <generator object <genexpr> at 0x7fdaa8e407d8>
for x in multiples_gen:
  print(x)
  # Outputs numbers