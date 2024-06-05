import os
import platform

def is_windows():
    return platform.system() == 'Windows'


def get_config_folder_path(app_name):

    if is_windows():
        username = os.getlogin()
        config_dir = os.path.join('C:\\Users', username, 'AppData', 'Roaming', app_name, "config")
        # If the Python debugger is running, the path will be in something like:
        # C:\Users\Username\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.11_qbz5n2kfra8p0\LocalCache\Roaming

    else:
        config_dir = os.path.expanduser(os.path.join("~", ".config", app_name))

    # Create the directory if it doesn't exist
    if not os.path.exists(config_dir):
        os.makedirs(config_dir)

    return config_dir


def get_appdata_folder_path(app_name):

    if is_windows():
        username = os.getlogin()
        appdata_folder_path = os.path.join('C:\\Users', username, 'AppData', 'Roaming', app_name)
        # If the Python debugger is running, the path will be in something like:
        # C:\Users\Username\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.11_qbz5n2kfra8p0\LocalCache\Roaming
    else:
        appdata_folder_path = os.path.expanduser(os.path.join("~", ".appdata", app_name))

    # Create the directory if it doesn't exist
    if not os.path.exists(appdata_folder_path):
        os.makedirs(appdata_folder_path)

    return appdata_folder_path


def get_config_value(config_folder_path, name):

    if not os.path.exists(config_folder_path):
        os.makedirs(config_folder_path)

    file_path = os.path.join(config_folder_path, name + '.txt')
    
    try:
        with open(file_path, 'r') as file:
            contents = file.read()
        return contents
    except FileNotFoundError:
        print(f"File '{name}' not found in the specified folder '{config_folder_path}'")
        return None
    except Exception as ex:
        print(f"Error occurred while reading '{name}': {ex}")
        return None


def set_config_value(config_folder_path, name, value):

    if not os.path.exists(config_folder_path):
        os.makedirs(config_folder_path)

    # Create the directory if it doesn't exist
    if not os.path.exists(config_folder_path):
        os.makedirs(config_folder_path)

    file_path = os.path.join(config_folder_path, name + '.txt')

    try:
        with open(file_path, 'w') as file:
            file.write(value)
        print(f"Successfully set the value in '{name}'")
    except Exception as ex:
        print(f"Error occurred while setting value in '{name}': {ex}")
