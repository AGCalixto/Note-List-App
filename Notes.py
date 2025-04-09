from tkinter import Toplevel, Text
from customtkinter import CTkButton, CTkLabel
from Storage import load_notes, save_notes
from tkinter import Frame

# Load Saved Files
notes = load_notes()


def refresh_notes(Tab2Frame):
    # Show updated notes.
    for widget in Tab2Frame.winfo_children():
        widget.destroy()

    for index, note_text in enumerate(notes):
        display_note(note_text, index, Tab2Frame)


def display_note(note_text, index, Tab2Frame):
    # Display notes with edit and delete buttons.
    FinalFrame = Frame(Tab2Frame, bg='#665656', width=320)
    FinalFrame.pack(pady=5, fill='both', expand=True)

    def delete_note():
        notes.pop(index)
        save_notes(notes)
        refresh_notes(Tab2Frame)

    def edit():
        AddNote(Tab2Frame.master, Tab2Frame, note_text, index)

    # ---------D-E-L-E-T-E--B-U-T-T-O-N--------------------------------
    CTkButton(FinalFrame, text='❌', width=30,
              font=('Times New Roman', 14, 'bold'),
              command=delete_note).pack(side='right', padx=1, pady=5)

    # -------------E-D-I-T--B-U-T-T-O-N--------------------------------
    CTkButton(FinalFrame, text='->', width=30,
              font=('Times New Roman', 14, 'bold'),
              command=edit).pack(side='right', padx=1, pady=5)

    # --------------D-I-S-P-L-A-Y--N-O-T-E-S---------------------------
    CTkLabel(FinalFrame, text=note_text,
             wraplength=280,
             font=('Times New Roman', 16),
             bg_color='gray', width=295,
             anchor='w', padx=10).pack(side='left', pady=5, padx=5)


def AddNote(Window, Tab2Frame, existing_text='', note_index=None):
    # Creates or edits an existing note.
    NoteWindow = Toplevel(Window)
    NoteWindow.geometry('450x450')
    NoteWindow.config(bg='#665656')
    NoteWindow.title('Note')
    NoteWindow.resizable(width=False, height=False)

    CTkLabel(NoteWindow, text='Press Save whenever you are finished!',
             font=('Times New Roman', 16, 'italic'),
             bg_color='#665656').pack(side='top')

    # The place where user can write text
    NoteText = Text(NoteWindow, font=('Times New Roman', 18), width=45, height=11)
    NoteText.pack(side='top', pady=5, padx=10)

    # If editing, pre-fill the text field
    if existing_text:
        NoteText.insert(1.0, existing_text)

    def save_note():
        new_text = NoteText.get(1.0, 'end').strip()
        if new_text:
            if note_index is not None:
                notes[note_index] = new_text
            else:
                notes.append(new_text)
            save_notes(notes)
            refresh_notes(Tab2Frame)
        NoteWindow.destroy()

    # Button for saving the text
    SaveButton = CTkButton(NoteWindow,
                           text='Save',
                           font=('Times New Roman', 14, 'bold'),
                           command=save_note)
    SaveButton.pack(side='bottom', pady=5)
