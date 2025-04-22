import tkinter as tk
from Model.ConveyorModel import ConveyorModel

class ConveyorViewModel:
    
    def __init__(self):
        self.model = ConveyorModel()
        
        self.productivityPerYear = 0.0
        self.hoursAtDay = 0.0
        self.volumeForms = 0.0
        self.daysPerYear = 247
        self.coeffUsability = 0.95
        self.product_type = 'type1'
        self.concrete_volume = 'low'
        
        self.result_text = ""
        
        self.update_result_callback = None
    
    def set_update_callback(self, callback):
        self.update_result_callback = callback
    
    def calculate(self):
        try:
            timeOfCycle = self.model.get_forming_cycle(self.product_type, self.concrete_volume)
            lineProd = self.model.calculate_line_productivity(
                self.coeffUsability, self.daysPerYear, self.hoursAtDay, self.volumeForms, timeOfCycle
            )
            numberOfLines = self.model.calculate_lines(self.productivityPerYear, lineProd, self.coeffUsability)
            Nkl_rounded = int(numberOfLines) + 1 if numberOfLines > int(numberOfLines) else int(numberOfLines)
            
            self.result_text = (
                f"Результаты расчета:\n"
                f"Производительность линии: {lineProd:.2f} м³\n"
                f"Цикл формования: {timeOfCycle} мин\n"
                f"Требуемое количество линий: {numberOfLines:.2f}\n"
                f"Рекомендуемое количество: {Nkl_rounded}"
            )
            
            if self.update_result_callback:
                self.update_result_callback()
                
        except Exception as e:
            self.result_text = f"Ошибка: {str(e)}"
            if self.update_result_callback:
                self.update_result_callback()