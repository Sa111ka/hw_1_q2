import random

min = 1
max = 1000
quantity = int(input("Введіть число : "))

def get_numbers_ticket(min, max, quantity):
    if min > quantity or max < quantity:
        return []
    numbers = []
    for i in range(quantity):
        number = random.randint(min, max)
        numbers.append(number)
    return numbers

result = get_numbers_ticket(min, max, quantity)
print(result)

















