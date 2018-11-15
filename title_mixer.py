import random
from igdb_api_python.igdb import igdb ##getting access to the igdb video game database

igdb = igdb("dc4da56a02c6038e2ea17b7b1ff4ce7d") ##key for using api


def mixer(game_name, misconduct):
    """This is an internal function that will be used to actually mix up the game titles and the misconducts that the bigger function
    for this assignment will use."""
    game_array = game_name.split(" ") ##splits the game name into an array
    if len(game_array) == 1: ##if the game title only has 1 word in it, it puts the misconduct at the end of it
        game_array.append(misconduct)
    placement = random.randint(0, len(game_array) - 1) ##picks a random word in the game title for the misconduct to replace
    game_array[placement] = misconduct ##puts the misconduct in the randomly assigned place
    mixed_game_name = " ".join(game_array) ##joins the list back into a string and saves it as a variable
    print(mixed_game_name)

def bot():
    """The actual "twitter bot" that will use the mixer function above after grabbing a random game from the video game database
    and a random misconduct from a list and putting them into the mixer function. """
    random_game = random.randint(1, 109335) ##grabs a random int
    result = igdb.games(random_game) ##uses the random in as an id for a game
    for game in result.body: ##this is how the api works to grab a game title, not fully sure how it works under the hood
        chosen_game = game["name"] ##stores the game name as it's own variable
    misconduct_list = ["Overwork", "No Severence Pay", "Losing Sleep", "No Time For Family", "Pizza As Payment"] ##pretty self explanatory
    chosen_misconduct = misconduct_list[random.randint(0, len(misconduct_list) - 1)] ##chooses something form the list at random
    return mixer(chosen_game, chosen_misconduct) ##calls the mixer function defined above


bot()


    