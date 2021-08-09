# Collections

# defaultdict
import json
from collections import defaultdict
from pprint import pprint

colours = (

    ('Yasoob', 'Yellow'),
    ('Ali', 'Blue'),
    ('Arham', 'Green'),
    ('Ali', 'Black'),
    ('Yasoob', 'Red'),
    ('Ahmed', 'Silver'),
)

f_colours = defaultdict(list)

for name, colour in colours:
    f_colours[name] = colour

pprint(f_colours)

# Problem
# some_dict = {}
# some_dict['colours']['fav'] = 'yellow'

# Solution
tree = lambda: defaultdict(tree)
some_dict = tree()
some_dict['colours']['favourite'] = 'yellow'
pprint(some_dict)
data = json.dumps(some_dict)
print(data)
print(type(data))

# 12.2. OrderedDict
# Problem
print('\nProblem')
colours = {"Red": 198, "Blue": 160, "Green": 170, }
for key, value in colours.items():
    print(key, value)


print('\nSolution')
from collections import OrderedDict

colours = OrderedDict((('Red', 198), ('Green', 170), ('Blue', 160)))
for key, value in colours.items():
    print(key, value)


print('\n12.3. Counter')
from collections import Counter
colours = (
    ('Yasoob', 'Yellow'),
    ('Ali', 'Blue'),
    ('Arham', 'Green'),
    ('Ali', 'Black'),
    ('Yasoob', 'Red'),
    ('Ahmed', 'Silver'),
)
favs = Counter(name for name, colour in colours)
pprint(favs)

print('\n12.4. deque')
from collections import deque
d = deque()
d.append('1')
d.append('2')
d.append('3')

print(len(d))
# Output: 3

print(d[0])
# Output: '1'

print(d[-1])
# Output: '3'

d = deque(range(5))
print(len(d))
# Output: 5

d.popleft()
# Output: 0

d.pop()
# Output: 4

print(d)
# Output: deque([1, 2, 3])
d = deque([0, 1, 2, 3, 5], maxlen=5)
print(d)
# Output: deque([0, 1, 2, 3, 5], maxlen=5)

d.extend([6])
print(d)
#Output: deque([1, 2, 3, 5, 6], maxlen=5)
d = deque([1,2,3,4,5])
d.extendleft([0])
d.extend([6,7,8])
print(d)
# Output: deque([0, 1, 2, 3, 4, 5, 6, 7, 8])

print('\n12.5. namedtuple')
from collections import namedtuple
Animal = namedtuple('Animal', 'name age type')
perry = Animal(name='perry', age='31', type='cat')
print(perry)
print(perry.name)
pprint(perry._asdict())


print('\n12.6. enum.Enum (Python 3.4+)')
