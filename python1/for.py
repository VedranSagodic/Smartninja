#for petlja

secret = 25

for x in range(5):
    guess = int(input("Pogodi jedan broj između 1 i 30:"))

    if guess == secret:
        print("Bravo")
        break
    else:
        print("Sorry, fulao si")