from random import randint
a = 0
number = randint(1,100)
while a != number:
    print number
    a = raw_input ("guess the magic number")
    if a == number:
        print("you guessed lower than the magic number")

    #else:
    #    print("you guessed higher than the magic number")
print ("you guessed the magic number")
