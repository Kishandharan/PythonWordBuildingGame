import random
f1 = open("dictionary.txt", "r")
words = [i.replace("\n", "") for i in f1.readlines()]
userChoice = ""
compChoice = ""

userChoice = input("You: ")
lastletter1 = userChoice[-1]
filtered_words = list(filter(lambda x: True if x.startswith(lastletter1) else False, words))
compChoice = random.choice(filtered_words)
lastletter2 = compChoice[-1] 
print("Comp:", compChoice)

for i in range(0, 10, 1):
	userChoice = input("You: ")
	if userChoice.startswith(lastletter2) and (userChoice in words):
		lastletter1 = userChoice[-1]
		filtered_words = list(filter(lambda x: True if x.startswith(lastletter1) else False, words))
		compChoice = random.choice(filtered_words)
		lastletter2 = compChoice[-1] 
		print("Comp:", compChoice)
	else:
		break
print("------- GAME OVER -------")
