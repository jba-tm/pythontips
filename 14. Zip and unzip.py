# 14. Zip and unzip
from pprint import pprint

print('zip')
first_name = ['Joe','Earnst','Thomas','Martin','Charles']

last_name = ['Schmoe','Ehlmann','Fischer','Walter','Rogan','Green']

age = [23, 65, 11, 36, 83]

pprint(list(zip(first_name,last_name, age)))

for first_name, last_name, age in zip(first_name, last_name, age):
    print(f"{first_name} {last_name} is {age} years old")


print('\nUnzip')
full_name_list = [('Joe', 'Schmoe', 23),
                  ('Earnst', 'Ehlmann', 65),
                  ('Thomas', 'Fischer', 11),
                  ('Martin', 'Walter', 36),
                  ('Charles', 'Rogan', 83)]

first_name, last_name, age = list(zip(*full_name_list))
print(f"first name: {first_name}\nlast name: {last_name} \nage: {age}")
