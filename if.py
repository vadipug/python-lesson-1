#Оператор условий

brand = 'Volvo'   # бренд
engine_volme = 1.5  # объем двигателя
hoursepower = 79  # мощность двигателя
sunroof = False  # наличие люка

# if hoursepower < 80:
#     print ('No Tax')

# if hoursepower < 80:print('No Tax')
# else:print('TAX')

#Проверка условий if/elif/elif/else

# tax = 0
# if hoursepower < 80:
#     tax = 0
# elif hoursepower < 100:
#     tax = 10000
# elif hoursepower < 150:
#     tax = 20000
# else:
#     tax = 50000
# print(tax)

# Проыерка условий  if для присваивания

cool_car = 0

cool_car = 1 if sunroof == 1 else 0

print(cool_car)