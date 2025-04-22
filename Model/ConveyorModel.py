class ConveyorModel:
    
    def calculate_lines(productivityPerYear, lineProd, coeffUsability):
        return productivityPerYear / (lineProd * coeffUsability)
    
    def calculate_line_productivity(coeffUsability, daysPerYear, hoursAtDay, volumeForms, timeOfCycle):
        return 60 * coeffUsability * daysPerYear * hoursAtDay * volumeForms / timeOfCycle
    
    def get_forming_cycle(product_type, concrete_volume):
        cycles = {
            'type1': {'low': 12, 'medium': 22},
            'type2': {'low': 18, 'medium': 28},
            'type3': {'low': 25, 'medium': 35}
        }
        return cycles[product_type][concrete_volume]