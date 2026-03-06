import time
import random

print("Program starting")

for i in range (0,100):
	smt = random.randint(0,3)
	if smt == 2 or smt == 0:
		(print("Random number salt : " + str(random.randint(0,1000))))
	if i % 2 == 0:
		print("Even number: " + str(i))
	else:
		print("Odd number: " + str(i))
	time.sleep(1)


print("Completed couting")
