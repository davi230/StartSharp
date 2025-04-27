import tkinter as tk

class frame1(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, parent)
        self.create_widgets()

    def create_widgets(self):
        # Create widgets for the first frame here
        label = tk.Label(self, text="Frame 1")
        label.pack(pady=10)

class frame2(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, parent)
        self.create_widgets()

    def create_widgets(self):
        # Create widgets for the second frame here
        label = tk.Label(self, text="Frame 2")
        label.pack(pady=10)
        
class frame3(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, parent)
        self.create_widgets()

    def create_widgets(self):
        # Create widgets for the third frame here
        label = tk.Label(self, text="Frame 3")
        label.pack(pady=10)
        
class frame4(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, parent)
        self.create_widgets()

    def create_widgets(self):
        # Create widgets for the fourth frame here
        label = tk.Label(self, text="Frame 4")
        label.pack(pady=10)

'''
class frame4(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.create_widgets()

    def create_widgets(self):
        # Create widgets for the fourth frame here
        label = tk.Label(self, text="Frame 4")
        label.pack(pady=10)
'''
        
listFrames = [frame1, frame2, frame3, frame4]                