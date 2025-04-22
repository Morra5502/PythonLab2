import tkinter as tk
from tkinter import ttk
from tkinter.scrolledtext import ScrolledText

class ConveyorView:
    
    def __init__(self, root, viewmodel):
        self.root = root
        self.vm = viewmodel
        self.vm.set_update_callback(self.update_result)
        
        self.setup_ui()
    
    def setup_ui(self):
        """Создание интерфейса"""
        self.root.title("Расчет конвейерных линий")
        
        # Входные параметры
        input_frame = ttk.LabelFrame(self.root, text="Параметры")
        input_frame.pack(padx=10, pady=5, fill='x')
        
        ttk.Label(input_frame, text="Годовая производительность (Пг), м³:").grid(row=0, column=0)
        self.pg_entry = ttk.Entry(input_frame)
        self.pg_entry.grid(row=0, column=1)
        
        # ... другие поля ввода (аналогично)
        
        # Кнопки
        btn_frame = ttk.Frame(self.root)
        btn_frame.pack(pady=5)
        
        ttk.Button(btn_frame, text="Рассчитать", command=self.on_calculate).pack(side='left')
        
        # Результаты
        self.result_text = ScrolledText(self.root, height=10)
        self.result_text.pack(padx=10, pady=5, fill='both', expand=True)
    
    def on_calculate(self):
        """Обработчик нажатия кнопки"""
        try:
            # Получаем данные из View
            self.vm.Pg = float(self.pg_entry.get())
            # ... другие параметры
            
            # Вызываем расчет в ViewModel
            self.vm.calculate()
            
        except ValueError:
            self.result_text.delete(1.0, tk.END)
            self.result_text.insert(tk.END, "Ошибка ввода данных!")
    
    def update_result(self):
        """Обновление результатов по коллбэку"""
        self.result_text.delete(1.0, tk.END)
        self.result_text.insert(tk.END, self.vm.result_text)