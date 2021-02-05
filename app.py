import random
# Get the user guess
def get_guess():
    return list(input("What's your 3 digit guess guess: "))

# Generate computer code. three digits e.g 123
def generate_code():
    # Creating a list of every number from 0 - 9 and to cast it as a string
    # str(num)
    digits = [str(num) for num in range(10)]

    # shuffle the digits
    random.shuffle(digits)
    
    # Then grap the first 3 after the shuffle
    return digits[:3]

# Generate the clues
def generate_clues(code, user_guess):
    if user_guess == code:
        return "Code Cracked"
    clues = []


    # With enumerate => (enumerate(user_guess)), we go into the user guess
    # Then we use tuple and parking to park two thing. the actual index location "ind" and the number itself "num"
    for ind,num in enumerate(user_guess):
        # now we're saying if the number is == to the code[ind], we're going to the index location (user_guess)
        if num == code[ind]:
            clues.append("Match")
        elif num in code:
            clues.append("you're close")

    if clues == []:
        return ["Nope"]
    else:
        return clues
#Run game logic
print("Welcome code breaker!")
secet_code = generate_code()
clue_report = []

while clue_report != "Code Cracked":
    guess = get_guess()

    clue_report = generate_clues(guess, secet_code)
    print("Here's the result of your guess: ")
    for clue in clue_report:
        print(clue)