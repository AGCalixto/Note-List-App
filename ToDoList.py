from tkinter import Toplevel, Text
from customtkinter import CTkButton, CTkLabel, CTkCheckBox
from Storage import load_list, save_list
from tkinter import Frame, IntVar, Checkbutton

# Load Saved To-Do List
todolist = load_list()


def refresh_todolist(Tab1Frame):
    # In case of error
    global todolist
    if todolist is None:
        print('⚠️ Warning: todolist is None! Resetting to an empty list.')
        todolist = []

    # Show updated To-Do List
    for widget in Tab1Frame.winfo_children():
        widget.destroy()

    for index, task in enumerate(todolist):
        display_todolist(task, index, Tab1Frame)


def display_todolist(task, index, Tab1Frame):
    task_text, completed = task
    # Display the list with
    # cross-out, edit and delete buttons
    FinalFrame2 = Frame(Tab1Frame, bg='#665656', width=320)
    FinalFrame2.pack(pady=5, fill='both', expand=True)

    def CrossOut():
        todolist[index] = (task_text, v.get() == 1)
        save_list(todolist)
        refresh_todolist(Tab1Frame)

    def delete_point():
        todolist.pop(index)
        save_list(todolist)
        refresh_todolist(Tab1Frame)

    def edit():
        AddPoint(Tab1Frame.master, Tab1Frame, task_text, index)

    # -------------C-R-O-S-S-O-U-T--B-U-T-T-O-N--------------------------------
    v = IntVar(value=1 if completed else 0)

    Check_butt = CTkCheckBox(FinalFrame2, text='✔',
                             variable=v, width=3,
                             font=('Times New Roman', 14, 'bold'),
                             command=CrossOut,
                             bg_color='Black',
                             text_color='LightBlue',
                             checkbox_width=20,
                             checkbox_height=20)
    Check_butt.pack(side='left', padx=1, pady=5)

    # ---------D-E-L-E-T-E--B-U-T-T-O-N--------------------------------
    CTkButton(FinalFrame2, text='❌', width=30,
              font=('Times New Roman', 14, 'bold'),
              command=delete_point).pack(side='right', padx=1, pady=5)

    # -------------E-D-I-T--B-U-T-T-O-N--------------------------------
    CTkButton(FinalFrame2, text='->', width=30,
              font=('Times New Roman', 14, 'bold'),
              command=edit).pack(side='right', padx=1, pady=5)

    # --------------D-I-S-P-L-A-Y--T-A-S-K--T-E-X-T---------------------------
    displayed_text = ''.join([c+'\u0336' for c in task_text]) if completed else task_text
    text_color = 'gray' if completed else 'white'

    CTkLabel(FinalFrame2, text=displayed_text,
             wraplength=280,
             font=('Times New Roman', 16),
             bg_color='#665656', width=295,
             text_color=text_color,
             anchor='w', padx=10).pack(side='left', pady=5, padx=5)


def AddPoint(Window, Tab1Frame, existing_text='', todolist_index=None):
    # Create or Edit an Existing Point.
    PointWindow = Toplevel(Window)
    PointWindow.geometry('450x450')
    PointWindow.config(bg='#665656')
    PointWindow.title('Bullet')
    PointWindow.resizable(width=False, height=False)

    PointWindow.bind('<Control-s>', lambda event: save_point())

    Final_Label = CTkLabel(PointWindow, text='Press Save to add a bullet!',
                           font=('Times New Roman', 16, 'italic'),
                           bg_color='#665656')
    Final_Label.pack(side='top')

    # The place where user can write text
    NoteText = Text(PointWindow,
                    font=('Times New Roman', 18), width=45, height=11, wrap='word')
    NoteText.pack(side='top', pady=5, padx=10)

    # If editing, pre-fill the text field
    if existing_text:
        NoteText.insert(1.0, existing_text)

    def save_point():
        new_text = NoteText.get(1.0, 'end').strip()
        if not new_text:
            return

        if todolist_index is not None:
            todolist[todolist_index] = (new_text, todolist[todolist_index][1])
        else:
            todolist.append((new_text, False))

        save_list(todolist)
        refresh_todolist(Tab1Frame)
        PointWindow.destroy()

    # Button for saving the text
    SaveButton = CTkButton(PointWindow,
                           text='Save',
                           font=('Times New Roman', 14, 'bold'),
                           command=save_point)
    SaveButton.pack(side='bottom', pady=5)
