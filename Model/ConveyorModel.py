
class ConveyorModel:
    def calculate_lines(productivity_per_year, line_prod, coeff_usability):
        return productivity_per_year / (line_prod * coeff_usability)
    
    def calculate_line_productivity(days_per_year, hours_per_day, volume_forms, time_of_cycle):
        return 60 * days_per_year * hours_per_day * volume_forms / time_of_cycle
    
    def get_forming_cycle(product_type, volume_range):
        cycles = {
            'Изделия однослойные несложной конфигурации': {'до 3,5': 12, 'от 3,5 до 5,0': 22},
            'Изделия однослойные сложной конфигурации': {'до 3,5': 18, 'от 3,5 до 5,0': 28},
            'Изделия многослойные, крупногабаритные': {'до 3,5': 25, 'от 3,5 до 5,0': 35}
        }
        return cycles[product_type][volume_range]
    
    def get_working_days(line_type):
        days = {
            'Агрегатно-поточные и стендовые линии': 253,
            'Конвейерные линии': 247,
            'Цехи по приготовлению бетона': 253
        }
        return days[line_type]