# Steam Game Data

A project to fetch and save game data from the Steam API. This project provides a Python package (pip version) for fetching and saving game data.

## Features

- Fetch game data from the Steam API using the app ID.
- Save the fetched data in a JSON format.

## Project Structure

```
steamgamedata/
├── pip/                    # Python version
│   ├── steamgamedata/      # Package source code
│   │   ├── __init__.py      # Init file to make the directory a package
│   │   └── core.py          # Core module with pull and write functions
│   ├── requirements.txt     # Project dependencies for pip
│   └── setup.py             # Package setup script for pip installation
```

## Python Version (Pip)

### Installation

To install the Python package, navigate to the `pip` directory and run:

```bash
pip install .
```

### Usage

To use the Python package, you can pull game data and write it to a JSON file as follows:

```python
import steamgamedata

appid = 620  # Example for Portal 2
game_data = steamgamedata.pull(appid)  # Fetch game data using steamgamedata
steamgamedata.write("gamedata.json", game_data)  # Save data to a JSON file using steamgamedata
```

## JavaScript Version (NPM) 🚧

Currently being worked on. No guides are available as the syntax is not 100% clear yet.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
