import string
lower_case = string.ascii_lowercase
upper_case = string.ascii_uppercase
letters = string.ascii_letters



def alphabet_position(letter):
    #This will return the index of an upper_case/lower_case letter
    if letter in lower_case:
        return lower_case.find(letter)

    elif letter in upper_case:
        return upper_case.find(letter)

def rotate_string(text, rot):
    rotated = 0
    msg = ""
    for char in text:
        #Line 25 - 29 will chack to make sure there are only ascii_letters
        if char in letters:
            rotated = alphabet_position(char) + rot
        else:
            #This will return any char that is not an ascii_letter
            msg += char
        #These lines will  pull in the scrambled letters
        if rotated < 26 and char in lower_case:
            msg += lower_case[rotated]
        elif rotated >25 and char in lower_case:
            msg += lower_case[rotated % 26]
        elif rotated < 26 and char in upper_case:
            msg += upper_case[rotated]
        elif rotated >25 and char in upper_case:
            msg += upper_case[rotated % 26]


    return msg