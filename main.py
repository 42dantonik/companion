import os
import sys
import subprocess

from PyQt6.QtWidgets import QApplication

from main_window import MainWindow


def run_as_detached():
    """Run the script as a detached process."""
    if sys.platform == "win32":
        # Windows-specific detached process creation
        DETACHED_PROCESS = 0x00000008
        subprocess.Popen(
            [sys.executable, __file__],  # Relaunch the script
            creationflags=DETACHED_PROCESS,
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL,
            stdin=subprocess.DEVNULL,
        )
    else:
        # Unix-based detached process
        subprocess.Popen(
            [sys.executable, __file__],
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL,
            stdin=subprocess.DEVNULL,
            start_new_session=True,
        )
    print("Script started in detached mode.")
    sys.exit()


if __name__ == "__main__":
    # Check if the script should run detached
    if "--detach" in sys.argv:
        run_as_detached()

    # Initialize the application
    # db = SQLiteDB(DB_PATH)
    # app_state = AppState(db)

    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())