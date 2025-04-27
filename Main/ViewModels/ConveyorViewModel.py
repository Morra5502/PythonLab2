from Models.ConveyorModel import ConveyorModel
from Models.ReportGeneratorModel import ReportGeneratorModel


class ConveyorViewModel:
    def __init__(self):
        self.conveyorModel = ConveyorModel
        self.reportGeneratorModel = ReportGeneratorModel

        # Параметры для расчета
        self._productivity_per_year = 0.0
        self._hours_per_day = 8.0
        self._volume_forms = 0.0
        self._product_type = "Изделия однослойные несложной конфигурации"
        self._volume_range = "до 3,5"
        self._working_days = 247.0
        self._coeff_usability = 0.95
        
        # Результаты
        self._result_text = ""
        self._update_callback = None
    
    #region get set
    @property
    def productivity_per_year(self):
        return self._productivity_per_year
    
    @productivity_per_year.setter
    def productivity_per_year(self, value):
        self._productivity_per_year = value
    
    
    @property
    def hours_per_day(self):
        return self._hours_per_day
    
    @hours_per_day.setter
    def hours_per_day(self, value):
        self._hours_per_day = value
    
    @property
    def volume_forms(self):
        return self._volume_forms
    
    @volume_forms.setter
    def volume_forms(self, value):
        self._volume_forms = value
    
    @property
    def product_type(self):
        return self._product_type
    
    @product_type.setter
    def product_type(self, value):
        self._product_type = value
    
    @property
    def volume_range(self):
        return self._volume_range
    
    @volume_range.setter
    def volume_range(self, value):
        self._volume_range = value
    
    @property
    def working_days(self):
        return self._working_days
    
    @productivity_per_year.setter
    def working_days(self, value):
        self._working_days = value
    
    @property
    def coeff_usability(self):
        return self._coeff_usability
    
    @coeff_usability.setter
    def coeff_usability(self, value):
        self._coeff_usability = value
    
    @property
    def result_text(self):
        return self._result_text
    
    def set_update_callback(self, callback):
        self._update_callback = callback
    
    #endregion
    
    def calculate(self):
        try:
            time_of_cycle = self.conveyorModel.get_forming_cycle(self._product_type, self._volume_range)
            
            # Расчеты
            line_prod = self.conveyorModel.calculate_line_productivity(
                self._working_days, self._hours_per_day, self._volume_forms, time_of_cycle
            )
            number_of_lines = self.conveyorModel.calculate_lines(
                self._productivity_per_year, line_prod, self._coeff_usability
            )
            
            number_of_lines_rounded = int(number_of_lines) + 1 if number_of_lines > int(number_of_lines) else int(number_of_lines)
            
            # Формирование результата
            self._result_text = (
                f"Результаты расчета:\n"
                f"Рабочих дней в году: {self.hours_per_day}\n"
                f"Цикл формования: {time_of_cycle} мин\n"
                f"Годовая производительность линии: {line_prod:.2f} м³\n"
                f"Требуемое количество линий: {number_of_lines:.2f}\n"
                f"Рекомендуемое количество: {number_of_lines_rounded}"
            )
        
        except Exception as e:
            self._result_text = f"Ошибка: {str(e)}"

        if self._update_callback:
                self._update_callback()

    def save_to_word(self):
        if(self._result_text == ""):
            self._result_text = "Нечего сохранять в файл"
            if self._update_callback:
                self._update_callback()
            self._result_text = ""
            return
        
        self.reportGeneratorModel.save_to_word(self, self._result_text)