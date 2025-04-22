from Model.ConveyorModel import ConveyorModel
class ConveyorViewModel:
    def __init__(self):
        self.model = ConveyorModel
        
        # Параметры для расчета
        self._productivity_per_year = 0.0
        self._hours_per_day = 8.0
        self._volume_forms = 0.0
        self._line_type = "Конвейерные линии"
        self._product_type = "Изделия однослойные несложной конфигурации"
        self._volume_range = "до 3,5"
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
    def line_type(self):
        return self._line_type
    
    @line_type.setter
    def line_type(self, value):
        self._line_type = value
    
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
        #try:
        days_per_year = self.model.get_working_days(self._line_type)
        
        time_of_cycle = self.model.get_forming_cycle(self._product_type, self._volume_range)
        
        
        # Расчеты
        line_prod = self.model.calculate_line_productivity(
            days_per_year, self._hours_per_day, self._volume_forms, time_of_cycle
        )
        number_of_lines = self.model.calculate_lines(
            self._productivity_per_year, line_prod, self._coeff_usability
        )
        number_of_lines_rounded = int(number_of_lines) + 1 if number_of_lines > int(number_of_lines) else int(number_of_lines)
        
        # Формирование результата
        self._result_text = (
            f"Результаты расчета:\n"
            f"Рабочих дней в году: {days_per_year}\n"
            f"Цикл формования: {time_of_cycle} мин\n"
            f"Годовая производительность линии: {line_prod:.2f} м³\n"
            f"Требуемое количество линий: {number_of_lines:.2f}\n"
            f"Рекомендуемое количество: {number_of_lines_rounded}"
        )
        
        #except Exception as e:
            #self._result_text = f"Ошибка: {str(e)}"

        if self._update_callback:
                self._update_callback()
