 MATHS FUNCTIONS
x=22.11
print(x)
print(round(x))
print(abs(-22.11))

import math
print(math.ceil(5.9))
print(math.floor(5.9))


USING IF  ELSE STATEMENT 

price=1000000
has_good_credit="true"
if has_good_credit:
    down_payment=0.1 * price
else:
    down_payment=0.2 * price
print(f"down_payment: ${down_payment}")


LOGICAL OPERATOR

has_high_income="flase"
has_good_credit="flase"
if has_high_income and has_good_credit:
    print("eligible for loan")
 
 
 GUESSING GAME
 
 secert_number=5
guess_count=0
guess_limit=4
while guess_count < guess_limit:
    guess=int(input("guess:" ))
    guess_count+=1
    if guess==secert_number: 
        print("you won")
		
