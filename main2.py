import random

def gen_pass(pass_length):
    elements = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
    password = ""
    for i in range(pass_length):
        password += random.choice(elements)
    return password
def choose_btw(choice1,choice2):
    ChooseList = [choice1, choice2]
    Choose_is = random.choice(ChooseList)
    return Choose_is
def check(Name,Factor):
    Posib = random.randint(1,2)
    if Posib == 1:
        return 1
    else:
        return 2
