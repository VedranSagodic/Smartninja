#guess the secret number sa spremanjem u datoteku

import random
secret = random.randint(1,30)
attempts = 0

with open("score.txt", "r") as score_file:
    best_score = int(score_file.read())
    print("Top score " + str(best_score))

while True:
    guess = int(input("Pogodi jedan broj izmedju 1 i 30: "))
    attempts += 1

    if guess == secret:

        if attempts < best_score:
            with open("score.txt", "w") as score_file:
                score_file.write(str(attempts))

        print("Bravo! Trazeni broj je bio: " + str(secret))
        print("Attempts needed: " + str(attempts))
        break

    elif guess > secret:
        print("Fulao si, probaj manji broj")
    elif guess< secret:
        print("Fulao si probaj veći broj")
    else:
        print("Nisam prepoznao broj")

