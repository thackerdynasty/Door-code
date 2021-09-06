import random
print("Hello! Let's play crack the code!")
print("I am going to pick a five digit code. Your job is to crack it!")
doorcode = random.randint(10000,99999)
correctcode = False
while not correctcode:
    usercode = int(input("Guess."))
    if usercode == doorcode:
        correctcode = True
    else:
        print("Wrong code! Try again.")
print("You got it right!")
