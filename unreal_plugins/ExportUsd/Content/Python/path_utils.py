"""Util module to query path info"""
import configparser
import unreal

PROJECT_CFG_FOLDER = unreal.Paths.project_config_dir()
EDITOR_CFG_FILE = PROJECT_CFG_FOLDER + "DefaultEditor.ini"
ENGINE_CFG_FILE = PROJECT_CFG_FOLDER + "DefaultEngine.ini"
GAME_CFG_FILE = PROJECT_CFG_FOLDER + "DefaultGame.ini"
INPUT_CFG_FILE = PROJECT_CFG_FOLDER + "DefaultInput.ini"

def get_usd_export_folder():
    """Get the usd export folder from the Editor cfg file."""
    section_name = "UsdExport"
    key_name= "UsdExportFolderPath"

    # Get info from the "DefaultEditor.ini"
    config = configparser.ConfigParser()
    config.read(EDITOR_CFG_FILE)
    try:
        # might have to replace the '/' based on the OS.
        return config[section_name][key_name]
    except KeyError:
        unreal.log_error(
            f"Error parsing DefaultEditor.ini info for section {section_name} and key {key_name}"
        )
        return None

def get_otio_export_folder():
    """Get the otio export folder from the Editor cfg file."""
    section_name = "UsdExport"
    key_name= "OtioExportFolderPath"

    # Get info from the "DefaultEditor.ini"
    config = configparser.ConfigParser()
    config.read(EDITOR_CFG_FILE)
    try:
        # might have to replace the '/' based on the OS.
        return config[section_name][key_name]
    except KeyError:
        unreal.log_error(
            f"Error parsing DefaultEditor.ini info for section {section_name} and key {key_name}"
        )
        return None
