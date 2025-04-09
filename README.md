# Note & To-Do List App

A simple, sleek desktop application built with Python and `customtkinter`, allowing users to write notes and manage to-do lists with persistent local storage.

---

## Features

- **Notes Tab**: Write, edit, and delete notes with ease.
- **To-Do Tab**: Add tasks, edit them, delete them, and mark them as complete (cross-out style).
- **Auto-Save**: All data is saved locally using JSON files.
- **User Interface**: Scrollable views, clean layout, and modern widgets.

---

## Tech Information

- **Python 3.12**
- `tkinter` – Standard Python GUI library
- `customtkinter` – For modern-looking UI widgets
- `os` – For file and directory management
- `json` – For saving and loading data

---

## Project Structure

Note-List-App/ ├── Main.py # Entry point of the application ├── GUI.py # Sets up the GUI layout for both tabs ├── ToDoList.py # Handles logic for the To-Do List ├── Notes.py # Handles logic for the Notes ├── Storage.py # Reads from and writes to JSON files ├── list.json # Stores to-do items ├── notes.json # Stores notes └── README.md # Project documentation

# Project Structure

Project/
|- main.py
|- GUI.py
|- ToDoList.py
|- Notes.py
|- Storage.py

# Architecture Overview

## Main.py
- Initializes the app with two tabs: To-Do List and Notes.
- Uses ttk.Notebook to organize tabs.
- Calls setup_gui() from GUI.py to load each tab.

## GUI.py
- Defines the overall layout (labels, frames, buttons).
- Populates the interface using helper functions from ToDoList.py and Notes.py.

## ToDoList.py
- Core functions:
-- refresh_todolist() – Refresh task list display.
-- display_todolist() – Show each task with checkbox, edit, delete options.
-- AddPoint() – Pop-up for adding/editing tasks.

## Notes.py
- Core functions:
-- refresh_notes() – Refresh notes display.
-- display_note() – Show each note with edit/delete buttons.
-- AddNote() – Pop-up for adding/editing notes.

## Storage.py
- Saves and loads data using json.
- Handles local file creation via os module.

# How to Run
- Make sure Python 3.12 is installed. Then, install “customtkinter” if you haven’t installed already:
-- In bash
| pip install customtkinter
- Run the application
| python main.py

Dennis Alejandro Guerra Calix -- AGCalixto
