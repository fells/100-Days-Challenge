# FINAL PROJECT
# We have to write a higher or lower game so it can compare both of the challengers by comparing their stats

import random
import celebrities
import logos
celebrity_checked = []
def random_celebrity():
    """Gets a random celebrity from the pool"""
    random_celebrity_index = random.choice(celebrities.data)
    return random_celebrity_index

def store_celebrities():
    """Store's a celebrity in the new list"""
    celebrity = celebrity_checked.append(random_celebrity())
    return celebrity
def compare_guess(guess, celebrity_a,celebrity_b):
    if guess == "a":
        follower_count_a = celebrity_a['follower_count']
        follower_count_b = celebrity_b['follower_count']
        print(follower_count_a)
        print(follower_count_b)
        if follower_count_a > follower_count_b:
            random_celebrity()
            store_celebrities()
            compare_game()
    elif guess == "b":
        follower_count_a = celebrity_a['follower_count']
        follower_count_b = celebrity_b['follower_count']
        if follower_count_b > follower_count_a:
            random_celebrity()
            store_celebrities()
            compare_game()
    else:
        print("Please choose a valid option")

print(logos.logo)

store_celebrities()
store_celebrities()
celebrity_A = celebrity_checked[0]
celebrity_B = celebrity_checked[1]
def compare_game():
    print(f"compare A: {celebrity_A['name']} a {celebrity_A['description']}, from {celebrity_A['country']}")
    print(logos.versus)
    print(f"compare B: {celebrity_B['name']} a {celebrity_B['description']}, from {celebrity_B['country']}")
    guess = input("Who has more followers ? Type 'A' or 'B':\n").lower()
    compare_guess(guess, celebrity_A, celebrity_B)

compare_game()