#if elif petlja
import random
secret = random.randint(1,30)

while True:
    guess = int(input("Pogodi jedan broj izmedju 1 i 30: "))

    if guess == secret:
        print("Bravo! Trazeni broj je bio: " + str(secret))
        break
    elif guess > secret:
        print("Fulao si, probaj manji broj")
    elif guess< secret:
        print("Fulao si probaj veći broj")
    else:
        print("Nisam prepoznao broj")