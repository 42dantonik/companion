# Companion app

## Structure
main.main is the entry point.
`python3 main.py`

It creates the MainWindow class. This creates the navbar widget and the central widget.

## Repo structure
├── main.py
├── main_window.py
├── requirements.txt
├── setup.sh
├── modules/
│   ├── home_module.py
│   └── ...
├── data
│   ├── data.db
│   └── themes.py
│   └── app_state.py

## Adding Modules
Create a new file with modules/<name>_module.py as the entry point for the new module.
If the module needs multiple files create a folder for it (modules/<name>/). Create an __init__.py file.
Import the class in main_window.py (e.g. "from modules.home_module import HomeModule") and add it to modules_config with the name (will be shown in the navbar) and the class (e.g. HomeModule).
