import random

def mixer(game_name, misconduct):
    """This is an internal function that will be used to actually mix up the game titles and the misconducts that the bigger function
    for this assignment will use."""
    game_array = game_name.split() ##splits the game name into an array
    if len(game_array) == 1: ##if the game title only has 1 word in it, it puts the misconduct at the end of it
        game_array.append(misconduct)
    placement = random.randint(0, len(game_array)) ##picks a random word in the game title for the misconduct to replace
    game_array[placement] = misconduct
    mixed_game_name = game_array.join(" ")
    return mixed_game_name
