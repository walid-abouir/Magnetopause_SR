from pysr import PySRRegressor


# file_name_to_read = "hall_of_fame_2024-03-05_104520.276.pkl"

# file_name_to_read = "hall_of_fame_2024-03-05_105240.799.pkl"

# file_name_to_read = "hall_of_fame_2024-03-05_112215.263.pkl" #assez bonne dépendance en 1/pd^...

file_name_to_read = "hall_of_fame_2024-03-12_124554.136.pkl" #assez bonne dépendance en 1/pd

model = PySRRegressor.from_file(file_name_to_read)

model.sympy()
# Equation à trouver :
#(10.22+1.29*tanh(0.184*(Bz+8.14)))*Pd^(-1/6.6)