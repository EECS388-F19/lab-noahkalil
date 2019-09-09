#!/bin/python3
from random import randint

def lab0():
	print("Noah")
	num1 = randint(0,100)
	print(num1)
	num2 = randint(0,100)
	print(num2)
	sum = num1 + num2
	print("Sum = %d" % sum)
	avg = (num1 + num2) / 2
	print("Average = %d" % avg)

if __name__ == "__main__":
	lab0()
