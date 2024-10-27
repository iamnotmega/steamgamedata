## Test script to test pip functionality.

import json  # Import json for pretty printing
from steamgamedata import pull  # Import the pull function from the steamgamedata module

# Correct app ID
appid = 400  # Use 400 for Portal

# Fetch game data using steamgamedata
try:
    game_data = pull(appid)  # Call the pull function

    # Debug: Pretty print the entire response
    print(json.dumps(game_data, indent=4))  # Format with indentation

    # Check if 'steam_appid' is in the data and matches the requested appid
    if 'steam_appid' in game_data:
        if game_data['steam_appid'] == appid:
            print(f"Game Name: {game_data['name']}")  # Print the game name
        else:
            print(f"App ID {appid} not found in the response data.")
    else:
        print("Key 'steam_appid' not found in the response data.")
except KeyError as e:
    print(f"Key error encountered in the response data: {str(e)}")
except NameError as e:
    print(f"Error: {str(e)}. Make sure the module is correctly imported.")
