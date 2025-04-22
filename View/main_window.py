# View/main_window.py
import tkinter as tk
from tkinter import ttk, messagebox
from tkinter.scrolledtext import ScrolledText

class ConveyorView:
    def __init__(self, root, viewmodel):
        self.root = root
        self.vm = viewmodel
        self.vm.set_update_callback(self.update_result)
        
        self.setup_ui()
    
    def setup_ui(self):
        self.root.title("Расчет требуемого количества линий конвейера")
        
        # Основной фрейм для ввода параметров
        main_frame = ttk.LabelFrame(self.root, text="Параметры расчета")
        main_frame.pack(padx=10, pady=5, fill=tk.BOTH, expand=True)
        
        ttk.Label(main_frame, text="Требуемая годовая производительность цеха (м³):").grid(row=0, column=0, sticky=tk.W, padx=5, pady=5)
        self.pg_entry = ttk.Entry(main_frame)
        self.pg_entry.grid(row=0, column=1, padx=5, pady=5)
        
        ttk.Label(main_frame, text="Число часов работы в сутки:").grid(row=1, column=0, sticky=tk.W, padx=5, pady=5)
        self.hours_entry = ttk.Entry(main_frame)
        self.hours_entry.insert(0, "8")
        self.hours_entry.grid(row=1, column=1, padx=5, pady=5)
        
        ttk.Label(main_frame, text="Объем одной формовки (м³):").grid(row=2, column=0, sticky=tk.W, padx=5, pady=5)
        self.volume_entry = ttk.Entry(main_frame)
        self.volume_entry.grid(row=2, column=1, padx=5, pady=5)
        
        ttk.Label(main_frame, text="Тип технологической линии:").grid(row=3, column=0, sticky=tk.W, padx=5, pady=5)
        self.line_type_combo = ttk.Combobox(main_frame, values=[
            "Агрегатно-поточные и стендовые линии",
            "Конвейерные линии",
            "Цехи по приготовлению бетона"
        ])
        self.line_type_combo.set("Конвейерные линии")
        self.line_type_combo.grid(row=3, column=1, padx=5, pady=5, sticky=tk.EW)
        
        ttk.Label(main_frame, text="Тип изделия:").grid(row=4, column=0, sticky=tk.W, padx=5, pady=5)
        self.product_type_combo = ttk.Combobox(main_frame, values=[
            "Изделия однослойные несложной конфигурации",
            "Изделия однослойные сложной конфигурации",
            "Изделия многослойные, крупногабаритные"
        ])
        self.product_type_combo.set("Изделия однослойные несложной конфигурации")
        self.product_type_combo.grid(row=4, column=1, padx=5, pady=5, sticky=tk.EW)
        
        ttk.Label(main_frame, text="Объем бетона в одной формовке:").grid(row=5, column=0, sticky=tk.W, padx=5, pady=5)
        self.volume_range_combo = ttk.Combobox(main_frame, values=["до 3,5", "от 3,5 до 5,0"])
        self.volume_range_combo.set("до 3,5")
        self.volume_range_combo.grid(row=5, column=1, padx=5, pady=5, sticky=tk.EW)
        
        ttk.Label(main_frame, text="Коэффициент использования оборудования:").grid(row=6, column=0, sticky=tk.W, padx=5, pady=5)
        self.coeff_entry = ttk.Entry(main_frame)
        self.coeff_entry.insert(0, "0.95")
        self.coeff_entry.grid(row=6, column=1, padx=5, pady=5)
        
        # Кнопки
        btn_frame = ttk.Frame(self.root)
        btn_frame.pack(pady=5)
        
        ttk.Button(btn_frame, text="Рассчитать", command=self.on_calculate).pack(side=tk.LEFT, padx=5)
        ttk.Button(btn_frame, text="Сохранить в word", command=self.save_to_word).pack(side=tk.LEFT, padx=5)
        
        # Результаты
        self.result_text = ScrolledText(self.root, height=10)
        self.result_text.pack(padx=10, pady=5, fill=tk.BOTH, expand=True)
    
    def on_calculate(self):
        try:
            # Получаем данные из View и передаем в ViewModel
            self.vm.productivity_per_year = float(self.pg_entry.get())
            self.vm.hours_per_day = float(self.hours_entry.get())
            self.vm.volume_forms = float(self.volume_entry.get())
            self.vm.line_type = self.line_type_combo.get()
            self.vm.product_type = self.product_type_combo.get()
            self.vm.volume_range = self.volume_range_combo.get()
            self.vm.coeff_usability = float(self.coeff_entry.get())
            
            # Вызываем расчет
            self.vm.calculate()
        except ValueError as e:
            messagebox.showerror("Ошибка", "Проверьте правильность введенных данных!")
    
    def update_result(self):
        self.result_text.delete(1.0, tk.END)
        self.result_text.insert(tk.END, self.vm.result_text)
    
    def save_to_word(self):
        self.g = r
