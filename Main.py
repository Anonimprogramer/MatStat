import univariate_sample as us

import bivariate_sample as bs

univariate_sample = us.load("univariate_input.txt")

variety_range = us.variation_range_of_univariate_sample(univariate_sample)

us.distribution_function_grapic(variety_range)

us.equiinterval_method_grapic(variety_range)

us.equipropable_method_grapic(variety_range)

print(us.expectation(variety_range), "- точечное мат ожидание")

print(us.dispersion(variety_range), "- точечная дисперсия")

us.confidence_interval_MAT(variety_range)

us.confidence_interval_DIS(variety_range)

us.distribution_function_grapic_and_even_distributin_function(variety_range)

us.distribution_function_grapic_and_other_function(variety_range)

us.hypotize_of_normal_law(variety_range)

print("А вот тут как бы одиночная выборка закончилась, начинается двумерная,типа пары какие-то,хз матеша это какой-то "
      "кибербуллинг одиноких людей, я имею ввиду что дальше?Семейство первообразных?(если что,то я просто рофлю)")

x = []
y = []
bs.load(x, y, "bivariate_input.txt")
print(bs.correlation_moment(x,y),"- оценка корреляционного момента")
print(bs.correlation_coefficent(x,y),"-точечная оценка коэффициент корреляции")
print(bs.interval_correlation_mark(x,y),"- интервальная оценка коэффициента корреляции с надежностью γ = 0,95")
bs.hypotize_of_lack_correlation(x,y)
bs.dispersion_diargram_and_regression_line(x,y)
