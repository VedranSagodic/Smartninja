#program koji čita iz datoteke

with open("ninja.txt", "r") as ninja_file:
    contents = ninja_file.read()
    print (contents)


print("")

with open("ninja.txt", "r") as ninja_file:
        ninja_lines = ninja_file.readlines()

        for line in ninja_lines:
            print (line)


print("")



with open("ninja2.txt", "w") as ninja_file_2:
    ninja_file_2.write("Hello, ovo je nova datoteka!")
print("")
with open("ninja.txt", "a") as ninja_file:
    ninja_file.write("Drugi puta upisujem u prvu datoteku")

