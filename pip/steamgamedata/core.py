import requests
import json
import os

def pull(appid):
    """
    Fetch game data from the Steam API using the provided app ID.
    
    Args:
        appid (int): The app ID of the game to fetch data for.

    Returns:
        dict: The game data returned from the Steam API, or None if an error occurred.
    """
    url = f"http://store.steampowered.com/api/appdetails?appids={appid}"
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an exception for HTTP errors
        data = response.json()
        
        if not data[str(appid)]['success']:
            print(f"Error fetching data: {data[str(appid)]['error']}")
            return None
        
        return data[str(appid)]['data']

    except requests.exceptions.RequestException as e:
        print(f"Error fetching data: {e}")
        return None

def write(filename, data):
    """
    Write the fetched game data to a JSON file.
    
    Args:
        filename (str): The name of the file to write data to.
        data (dict): The game data to write to the file.
    """
    if data is None:
        print("No data to write.")
        return
    
    try:
        with open(filename, 'w') as f:
            json.dump(data, f, indent=4)
    except Exception as e:
        print(f"Error writing to file: {e}")

def save_data(appid, filename):
    """
    Fetch and save game data from the Steam API to a JSON file.
    
    Args:
        appid (int): The app ID of the game to fetch data for.
        filename (str): The name of the file to write data to.
    """
    game_data = pull(appid)
    write(filename, game_data)