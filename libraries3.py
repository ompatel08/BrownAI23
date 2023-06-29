from m import math
from r import random

result_1 = m.pow (2,4)
print("result_1 is", result_1)

result_2 = m.sqrt(16)
print("result_2", result_2)

result_3 = r.randint(0,100)
print("result_3 is", result_3)

names = ["Amaryllis", "Gidson", "Emily", "Reina", "Derin", "Elena", "Inacio"]
print("Original names: ",names)

r.shuffle(names)
print("Names after shuffling: ",names)

result_4 = r.choice(names)
print("Chosen name is: ",result_4)