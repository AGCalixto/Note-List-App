# Handle saving/loading notes and list in JSON Files
import json
import os

NOTES_FILE = 'notes.json'
LIST_FILE = 'list.json'


# Load notes from the Json File
def load_notes():
    if os.path.exists(NOTES_FILE):
        with open(NOTES_FILE, "r") as file:
            return json.load(file)
    return []


# Save notes to file
def save_notes(notes):
    with open(NOTES_FILE, "w") as file:
        json.dump(notes, file, indent=4)


# Load the To-Do List
def load_list():
    try:
        if os.path.exists(LIST_FILE):
            with open(LIST_FILE, "r") as file:
                data = json.load(file)
                return data if isinstance(data, list) else [] # Ensure it's a list
        else:
            return [] # Return empty list if file doesn't exist
    except Exception as e:
        print(f'Error Loading List: {e}')
        return [] # Return an empty list if there's an error



def save_list(todolist):
    try:
        with open(LIST_FILE, "w") as file2:
            json.dump(todolist, file2, indent=4)
    except Exception as e:
        print(f'Error Saving Files {e}')
