import random
import time

w = ["cat","dog","fox","monkey","mouse","panda","frog","snake","wolf"]
n = 1
print("[typing game] press enter when you ready!")
input()
startTime = time.time()

q = random.choice(w)
while n <= 5:
    print("Question:", n)
    print(q)
    x = input()
    if q == x:
        print("Pass!")
        n += 1
        q = random.choice(w)
    else:
        print("typing error! try again!")

endTime = time.time()
et = endTime - startTime
et = format(et,".2f")
print("time of typing:",et,"second")

