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
If you want to add another page add it to modules_config with the name (will be shown in the navbar) and the class.