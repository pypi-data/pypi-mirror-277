# Clase para definir la funci�n objetivo basada en funciones con c�digo de cobra

class  ObjectiveFunction:
    def __init__(self, model, objective_function):
        self.model = model
        self.objective_function = objective_function

    def evaluate(self, parameters):
            # Implementaci�n espec�fica para evaluar la funci�n objetivo
        pass
    def set_objective_function(self, objective_function):
        # Implementaci�n espec�fica para establecer la funci�n objetivo
        # La funci�n objetivo tiene que ser una funci�n de python con c�digo de cobra
        self.objective_function = objective_function
        pass