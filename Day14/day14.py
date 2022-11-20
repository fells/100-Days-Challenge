# FINAL PROJECT
# We have to write a higher or lower game so it can compare both of the challengers by comparing their stats

import random
import celebrities
import logos
def random_celebrity():
    """Gets a random celebrity from the pool"""
    random_celebrity_index = random.choice(celebrities.data)
    return random_celebrity_index

def extract_data(celebrity):
    """Format the celebrity data"""
    name = celebrity['name']
    description = celebrity['description']
    country = celebrity['country']

    return f"{name}, a {description}, from {country}"

def compare_guess(guess, celebrity_a,celebrity_b):
    """Check if the user's guess is correct or not"""
    if celebrity_a > celebrity_b:
        return guess == "a"
    else:
        return guess == "b"
def compare_game():
    print(logos.logo)
    score = 0
    game_should_continue = True
    celebrity_A = random_celebrity()
    celebrity_B = random_celebrity()

    while game_should_continue:
        celebrity_A = celebrity_B
        celebrity_B = random_celebrity()

        while celebrity_A == celebrity_B:
            celebrity_B = random_celebrity()

        print(f"Compare A: {extract_data(celebrity_A)}")
        print(logos.versus)
        print(f"Compare B: {extract_data(celebrity_B)}")
        guess = input("Who has more followers ? Type 'A' or 'B':\n").lower()

        celebrity_A_follower = celebrity_A["follower_count"]
        celebrity_B_follower = celebrity_B["follower_count"]
        is_correct = compare_guess(guess, celebrity_A_follower, celebrity_B_follower)

        print(logos.logo)
        if is_correct:
            score += 1
            print(f"You're right! Current score: {score}.")
        else:
            game_should_continue = False
            print(f"Sorry, that's wrong. Final score: {score}.")

compare_game()