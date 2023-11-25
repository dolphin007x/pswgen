# pswgen
a password generator, built in plain, simple Python

# logic

a random choice is made between a random character, a random letter or a random number

if the choice is a letter, another randomised choice is made regarding its case

then, the random character generating function is run **n** number of times, where n is the length of the password (default = 12), then, 

it is all joined together and returned
