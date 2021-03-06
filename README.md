# Troy
This bot is dedicated to Regan, the most toxic RL player I have ever known. This bot name was taken from Shroud's dog, Troy the German Shepherd - Siberian Husky mix

### Plain instructions

1. Make sure you've installed [Python 3.6 64 bit](https://www.python.org/ftp/python/3.6.5/python-3.6.5-amd64.exe). During installation:
   - Select "Add Python to PATH"
   - Make sure pip is included in the installation
2. Open Rocket League
3. Download or clone this repository
3. In the files from the previous step, find and double click on run-gui.bat
4. Click the 'Run' button


## Notes

- Bot behavior is controlled by `src/code.py`

- Bot appearance is controlled by `src/appearance.cfg`

- `run.py` runs the whole match execution, while all "bots code" is managed under `rlbot.cfg`

- Inside `rlbot.cfg`, bots code are included inside `src/config.cfg` which eventually links to `src/appearance.cfg` and `src/code.py`, where the appearance and behaviour is controlled.

- Hence, do not modify anything apart from `src/~`

## Important note
Always use working branch for any future works, and release branch to release the working bot

See https://github.com/RLBot/RLBotPythonExample/wiki for documentation and tutorials.
