from math import pow
from math import sqrt

from random import randint
from random import shuffle
from random import choice

result_1 = pow (2,4)
print("result_1 is", result_1)

result_2 = sqrt (16)
print("result_2", result_2)

result_3 = randint(0,100)
print("result_3 is", result_3)

names = ["Amaryllis", "Gidson", "Emily", "Reina", "Derin", "Elena", "Inacio"]
print("Original names: ",names)

shuffle(names)
print("Names after shuffling: ",names)

result_4 = choice(names)
print("Chosen name is: ",result_4)