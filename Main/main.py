import tkinter as tk
from Views.MainWindow import ConveyorView
from ViewModels.ConveyorViewModel import ConveyorViewModel

def main():
    root = tk.Tk()
    vm = ConveyorViewModel()
    ConveyorView(root, vm)
    root.mainloop()
    

if __name__ == "__main__":
    main()