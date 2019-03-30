import random

n = int(input("How many quiz you want? :"))

def make_question():
    a = random.randint(1,100)
    b = random.randint(1,100)
    op = random.randint(1,3)

    q = str(a)

    if op == 1:
        q = q + "+"
    if op == 2:
        q = q + "-"
    if op == 3:
        q = q + "*"

    q = q + str(b)

    return q

sc1 = 0
sc2 = 0

for x in range(n):
    q = make_question()
    print(q)
    ans = input("=")
    r = int(ans)

    if eval(q) == r:
        print("Correct!")
        sc1 = sc1 + 1
    else:
        print("Wrong!")
        sc2 = sc2 + 1


print("count of correct answer :", sc1, "/","count of wrong answer :", sc2)
if sc2 == 0:
    print("You are a GINIUS!!")
