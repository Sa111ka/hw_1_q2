import random
min = 1
max = 1000
quantity = int(input("Введіть число : "))

def get_numbers_ticket(min, max, quantity):
    if min > quantity or max < quantity:
        return []


numbers = random.randint(min, max) 
for i in range(quantity):
    numbers = random.randint(min, max)
    print(numbers)


















