from pysr import PySRRegressor

file_name_to_read = "hall_of_fame_2024-02-16_170832.052.pkl"

model = PySRRegressor.from_file(file_name_to_read)

#print(model)

model.sympy()