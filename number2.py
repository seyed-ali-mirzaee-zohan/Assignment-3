import random
print(" ** Your chosen number must be between 0 and 50 ** ")
n=int(input("Please indicate how many numbers in your list : "))
list_of_numbers = random.sample(range(0, 50), n)
print(list_of_numbers)