"""

"""

# FINAL PROJECT
import logo
import random

def CalculateScore(cards):
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)

    return sum(cards)


def Compare(player_score, computer_score):
    if player_score == computer_score:
        return "It's a draw 🙄"
    elif computer_score == 0:
        return "Lose, opponent has a Blackjack 😟"
    elif player_score == 0:
        return "Awesome, you won with a Blackjack ♠️♥♣️♦"
    elif player_score > 21:
        return "You went over. You lose 😟"
    elif computer_score > 21:
        return "Opponent went over. You win ♠️♥♣️♦"
    elif player_score > computer_score:
        return "Awesome, you won with a Blackjack ♠️♥♣️♦"
    else:
        return "You lose 😟"

def DealCard():
    """Returns a random card from the deck"""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card

def Blackjack():
    print(logo.logo)
    player = []
    computer = []
    is_game_over = False

    for _ in range(2):
        player.append(DealCard())
        computer.append(DealCard())

    while not is_game_over:
        player_score = CalculateScore(player)
        computer_score = CalculateScore(computer)

        print(f"Your cards: {player}, your current score: {player_score}")
        print(f"Computer first card: {computer[0]}")

        if player_score == 0 or computer_score == 0 or player_score > 21:
            is_game_over = True
        else:
            draw_card = input("Do you want to draw another card ? 'Y' 'N':\n").lower()
            if draw_card == "y" or draw_card == "yes":
                player.append(DealCard())
            else:
                is_game_over = True

    while computer_score != 0 and computer_score < 17:
        computer.append(DealCard())
        computer_score = CalculateScore(computer)

    print(f"Your final hand {player}, final score: {player_score}")
    print(f"Computer final hand: {computer}, final score: {computer_score}")
    print(Compare(player_score, computer_score))

    restart = input("Do you want to play again ? 'Y' 'N':\n").lower()
    if restart == "y" or restart == "yes":
        Blackjack()
Blackjack()
