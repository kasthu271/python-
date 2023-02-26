RANGE FUNCTION ( " USING FOR LOOP ")

numbers=range(40)
for number in numbers:
    print(number)
numbers=range(3,6)
for number in numbers:
    print( number)
	
	GUESSING GAME 
	
	import random

random_number= random.randint(1,10)

guess=int(input("choose  a number from 1 to 10: " ))

if guess==random_number:
    print("you got it:")
elif guess<random_number:
    print("to low:")
else:
    print("to high:")

print(f"random Number was : {random_number} ")
