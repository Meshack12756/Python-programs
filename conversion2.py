date_learn = input("When did you start going to school? ")
print(type(date_learn))#checks for data type
learn_years = 2024 - int(date_learn)#conversion
print(type(learn_years))
print("your learning progress is currently ",learn_years," years")
