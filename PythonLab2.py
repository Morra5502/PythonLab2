import tkinter as tk
from View.main_window import ConveyorView
from ViewModel.vm import ConveyorViewModel

def main():
    root = tk.Tk()
    vm = ConveyorViewModel()
    ConveyorView(root, vm)
    root.mainloop()
    

if __name__ == "__main__":
    main()