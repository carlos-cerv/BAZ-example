from collections import defaultdict

dogs=['Sparky', 'Hunter', 'Loki', 'Astro', 'Sparky', 'Rocky', 'Rocky', 'Toby', 'Chelsea',
      'Maple', 'Maya', 'Loki', 'Sparky', 'Toby', 'Sparky', 'Dexter', 'Fido', 'Sparky']

dog_dict=defaultdict(int)
for dog in dogs:
  dog_dict[dog] += 1

print('Rocky->', dog_dict['Rocky'])
print('Sparky->', dog_dict['Sparky'])
print(list(dog_dict.keys()))

# Comment

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
