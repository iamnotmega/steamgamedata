import requests

def pull(appid):
    """Fetch game data from Steam API using the provided app ID."""
    url = f"https://store.steampowered.com/api/appdetails?appids={appid}"
    response = requests.get(url)
    
    if response.status_code != 200:
        raise ValueError(f"Error fetching data: {response.status_code}")
    
    data = response.json()

    # Check if the request was successful and if the app ID exists in the data
    if str(appid) in data and data[str(appid)]['success']:
        return data[str(appid)]['data']  # Return the game data
    else:
        raise ValueError(f"Failed to retrieve data for appid {appid}")

def write(appid, filename):
    """Save game data to a JSON file."""
    try:
        game_data = pull(appid)  # Fetch game data using steamgamedata
        with open(filename, 'w') as f:
            json.dump(game_data, f, indent=4)
        print(f"Game data for app ID {appid} written to {filename}.")
    except Exception as e:
        print(f"An error occurred: {e}")
