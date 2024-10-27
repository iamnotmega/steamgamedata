# Steam Game Data

A project to fetch and save game data from the Steam API. This project provides two implementations: a Python package (pip version) and a JavaScript package (npm version).

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
└── npm/                    # JavaScript version
    ├── package.json         # NPM package file
    └── index.js             # Main script for NPM version
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

## JavaScript Version (NPM)

### Installation

To install the JavaScript package, navigate to the `npm` directory and run:

```bash
npm install
```

### Usage

To use the JavaScript package, you can fetch game data and save it as follows:

```javascript
const steamgamedata = require('./index');

const appid = 620; // Example for Portal 2
const gameData = steamgamedata.pull(appid); // Fetch game data using steamgamedata
steamgamedata.write("gamedata.json", gameData); // Save data to a JSON file using steamgamedata
```

### Running the Main Script

To run the main script, use:

```bash
node index.js
```

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
