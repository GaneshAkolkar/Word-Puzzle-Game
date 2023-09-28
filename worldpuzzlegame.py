import random

# List of words for the game
word_list = ["FATHER", "BARK", "CRY", "GREEN", "AEROPLANE", "APPLE", "MANGO", "PIZZA", "TIGER", "ELEPHANT"]

# Function to shuffle the word list and return 5 random words
def get_random_words():
    random.shuffle(word_list)
    return word_list[:5]

# Function to check if the user's input is correct
def check_word(user_input, correct_word):
    if user_input.upper() == correct_word:
        return True
    else:
        return False

# Initialize the score
score = 0

# Main game loop
for round_num in range(1, 6):
    print(f"Round {round_num}:")
    words_to_guess = get_random_words()
    
    for word in words_to_guess:
        scrambled_word = ''.join(random.sample(word, len(word)))
        print(f"Arrange the letters to form a valid word:")
        print(scrambled_word)
        
        user_input = input().strip()
        
        if check_word(user_input, word):
            print("Correct")
            score += 1
        else:
            print("Wrong")
            score -= 1

# Print the final score
print(f"Game over! Your final score is: {score}")
