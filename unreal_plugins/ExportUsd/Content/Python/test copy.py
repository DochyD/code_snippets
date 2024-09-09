"""Test file so I can run quick snippet inside unreal"""
import os
import path_utils
import unreal

import unreal

# Get all actors in the current level
all_actors = unreal.EditorLevelLibrary.get_all_level_actors()

test = unreal.EditorLevelLibrary.get_all_level_actors
# Loop through the actors and print their names and types
for actor in all_actors:
    actor_name = actor.get_name()
    actor_type = actor.get_class().get_name()
    folder_path = actor.get_folder_path()
    if actor_type == "StaticMeshActor":
        # Check if the actor is in a folder
        if folder_path:
            print(f"Name: {actor_name}, Type: {actor_type}, Folder: {folder_path}")
        else:
            print(f"Name: {actor_name}, Type: {actor_type}, Folder: [Root]")