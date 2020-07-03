#while petlja

secret = 18

while True:
    guess = int(input("Pogodi jedan broj izmedju 1 i 30: "))

    if guess == secret:
        print("Bravo!")
        break
    else:
        print("Sorry, fulao si")