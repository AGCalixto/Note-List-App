# Main Application Launcher

from tkinter import ttk, Frame
from customtkinter import CTk, CTkFrame
from GUI import setup_gui


# Initialize the Main Application
class ToDoApp(CTk):
    def __init__(self):
        super().__init__()

        # Initialize the main window
        self.title('To-Do List App')
        self.geometry('400x500')
        self.config(background='#665656')
        self.resizable(width=False, height=False)

        # Use Tabs to separate the app
        self.notebook = ttk.Notebook(self)
        self.notebook.pack(expand=True, fill='both', padx=10, pady=10)

        # Create To-Do List Tab
        self.Tab1Initial = CTkFrame(self, bg_color='#665656')
        self.notebook.add(self.Tab1Initial, text='To-Do')
        # Frame for Design Improvement
        self.Tab1 = Frame(self.Tab1Initial, bg='#665656')
        self.Tab1.pack(side='top', fill='both', expand=True)

        # Create Notes Tab
        self.Tab2Initial = CTkFrame(self, bg_color='#665656')
        self.notebook.add(self.Tab2Initial, text='Notes')
        # Frame for Design Improvement
        self.Tab2 = Frame(self.Tab2Initial, bg='#665656')
        self.Tab2.pack(side='top', fill='both', expand=True)

        # Setup GUI for Both Tabs
        self.setup_tabs()

    def setup_tabs(self):
        # Import GUI functions from To-Do and Notes modules
        setup_gui(self.Tab1, self.Tab2, self)


# Run Application
if __name__ == "__main__":
    app = ToDoApp()
    app.mainloop()
