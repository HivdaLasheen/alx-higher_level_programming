#!/usr/bin/python3
# Heba M Lasheen <270@holbertonschool.com>
import random
 
number = random.randint(-10, 10)

if number < 0:
    print("{:d} is negative".format(number))
elif number > 0 :
    print("{:d} is positive".format(number))
else:
    print("{:d} is zero".format(number))
