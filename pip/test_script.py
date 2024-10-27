import steamgamedata

# Define the app ID for the game you want to fetch data for (e.g., Portal 2).
appid = 620  # Example app ID for Portal 2
filename = "gamedata.json"  # File where the game data will be saved

# Fetch game data using steamgamedata.pull
game_data = steamgamedata.pull(appid)

# Check if the game_data is not empty before writing
if game_data:
    # Write the fetched game data to a JSON file using steamgamedata.write
    steamgamedata.write(filename, game_data)
    print(f"Game data has been written to {filename}.")
else:
    print("No game data was fetched. Nothing was written.")
