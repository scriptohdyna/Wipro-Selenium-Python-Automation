import configparser
import os

PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CONFIG_FILE_PATH = os.path.join(PROJECT_ROOT, "config", "config.ini")


def get_config():
    if not os.path.exists(CONFIG_FILE_PATH):
        raise FileNotFoundError(
            f"Could not find config file at: {CONFIG_FILE_PATH}. "
            "Make sure config/config.ini exists in the project root."
        )
    config = configparser.ConfigParser()
    config.read(CONFIG_FILE_PATH)
    return config


def get_base_url():
    return get_config().get("environment", "base_url")


def get_browser_name():
    return get_config().get("browser", "name")


def get_bool(section, key, fallback=False):
    return get_config().getboolean(section, key, fallback=fallback)


def get_int(section, key, fallback=0):
    return get_config().getint(section, key, fallback=fallback)


def get_path(key):
    relative_path = get_config().get("paths", key)
    return os.path.join(PROJECT_ROOT, relative_path)
