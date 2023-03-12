# Higher or Lower Game
import random

from higher_lower_art import vs, logo
from higher_lower_data import data

# print title art

def compare_followers(celeb_a, celeb_b):
    if celeb_b['follower_count'] > celeb_a['follower_count']:
        return 'b'
    if celeb_a['follower_count'] > celeb_b['follower_count']:
        return 'a'
    
def get_celeb():
    return random.choice(data)

def game():
    print(logo)
    game_over = False
    score = 0
    celeb_a = get_celeb()
    celeb_b = get_celeb()

    while game_over == False:
    # pull two random celebrities from data object
        celeb_a = celeb_b
        celeb_b = get_celeb()

        while celeb_a == celeb_b:
            celeb_b = get_celeb()
        print(f"Compare A: {celeb_a['name']}, {celeb_a['description']}, from {celeb_a['country']}")
        print(vs)
        print(f"Compare B: {celeb_b['name']}, {celeb_b['description']}, from {celeb_b['country']}")
        
        answer = input("Who has more followers? Type A or B: ").lower()

        check_answer = compare_followers(celeb_a, celeb_b)

        if answer == check_answer:
            # if right, print score, compare wrong answer to new answer
            score += 1
            print(f"You're right! Current score: {score}")
        else:
            # if wrong, end game with final score
            print(f"Sorry that's wrong. Final score is {score}")
            game_over = True

game()