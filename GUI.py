# To Handle the GUI layout
# Set up the user interface
from customtkinter import CTkButton, CTkLabel, CTkScrollableFrame
from Notes import AddNote, refresh_notes
from ToDoList import AddPoint, refresh_todolist


def setup_gui(Tab1, Tab2, Window):
    # ----------------------T-O-D-O--T-A-B------------------------------
    CTkLabel(Tab1, text='📝 To-Do List',
             font=('Times New Roman', 20, 'bold'),
             bg_color='#665656').pack(side='top')

    # Description
    CTkLabel(Tab1, text='Tap on the bottom side of the page to edit it!',
             font=('Times New Roman', 16, 'italic'),
             bg_color='#665656').pack(side='top')

    Tab1Frame = CTkScrollableFrame(Tab1, bg_color='#c2a776', height=150)
    Tab1Frame.pack(side='top', pady=10, fill='both', expand=True)
    Tab1Frame.pack_propagate(False)

    # Edit Button
    CTkButton(Tab1, text='Add Task', font=('Times New Roman', 14, 'bold'),
              command=lambda: AddPoint(Window, Tab1Frame)).pack(side='bottom', pady=20)

    # Load Existing To-Do Items
    refresh_todolist(Tab1Frame)

    # ----------------------N-O-T-E-S--T-A-B------------------------------
    CTkLabel(Tab2, text='📒 Your Notes',
             font=('Times New Roman', 20, 'bold'),
             bg_color='#665656').pack(side='top')

    # Description
    CTkLabel(Tab2, text='Touch Edit or Delete next to a note to modify it.',
             font=('Times New Roman', 16, 'italic'),
             bg_color='#665656').pack(side='top')

    Tab2Frame = CTkScrollableFrame(Tab2, bg_color='#c2a776', height=150)
    Tab2Frame.pack(side='top', pady=10, fill='both', expand=True)
    Tab2Frame.pack_propagate(False)

    # Edit Button
    CTkButton(Tab2, text='Add Note', font=('Times New Roman', 14, 'bold'),
              command=lambda: AddNote(Window, Tab2Frame)).pack(side='bottom', pady=20)

    # Load Existing Notes
    refresh_notes(Tab2Frame)
