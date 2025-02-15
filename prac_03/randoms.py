# import random
#
# print(random.randint(5, 20))  # line 1
# print(random.randrange(3, 10, 2))  # line 2
# print(random.uniform(2.5, 5.5))  # line 3

import random

print(random.randint(5, 20))  # line 1
# Possible output: 11
# Smallest possible number: 5
# Largest possible number: 20

print(random.randrange(3, 10, 2))  # line 2
# Possible output: 7
# Smallest possible number: 3
# Largest possible number: 9
# Could line 2 have produced a 4? No, because step is 2, producing 3, 5, 7, or 9.

print(random.uniform(2.5, 5.5))  # line 3
# Possible output: 3.392804997708324
# Smallest possible number: 2.5
# Largest possible number: 5.5

# Code to produce a random number between 1 and 100 inclusive:
print(random.randint(1, 100))
