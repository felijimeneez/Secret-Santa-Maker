import random
import os

def draw_santa (players):
    player_amount = len(players)
    # Length check
    if not players or player_amount == 1:
        return "List should have at least 2 players"
    
    players_copy = players[:]

    output_folder = "output"
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    
    #Iterate over every participant and assign them a secret santa
    for player in players:

        invalid_santa = True

        while invalid_santa:
            secret_santa = random.choice (players_copy)
            
            if player != secret_santa:
                invalid_santa = False
        
        # Create the files in the output folder
        filename = os.path.join(output_folder, f"{player}_secret_santa.txt")

        with open (filename, "w") as file:
            file.write(f"You are the secret santa of {secret_santa}!")
            print (f"{player} is somebody's secret santa!")
        
        players_copy.remove(secret_santa)
        player_amount = len(players_copy)

        

        