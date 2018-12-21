possible_choices_normal = []
for drink in ['water', 'juice', 'tea']:
    for food in ['ham', 'eggs', 'spam']:
        possible_choices_normal.append([drink, food])

print(possible_choices_normal)



# This could be written with the nested list comprehension as :

possible_choices = [ [drink, food] for drink in ['water', 'juice', 'tea'] for food in ['ham', 'eggs', 'spam'] ]
print(possible_choices)


print()

# Similarly,

coords = []

for x in range(5):
    for y in range(3):
        coordinate = (x, y)
        coords.append(coordinate)
print(coords)

# Can be written as :

compre_coords = [ (x, y) for x in range(5) for y in range(3) ]

print(compre_coords)
