import random

subjects = ['fred', 'ana', 'max', 'mom']
verbs = ['likes', 'eats', 'makes', 'moves']
objects = ['an apple', 'a cat', 'a robot', 'me']

for i in range(0, 4):
    print random.choice(subjects), random.choice(verbs), random.choice(objects)

