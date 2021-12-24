import univariate_sample as us
import bivariate_sample as bs

print("-----univariate_input------")
univariate_sample = us.load("univariate_input.txt")

variety_range = us.variation_range_of_univariate_sample(univariate_sample)
print("Variation row X")
print(variety_range)

us.distribution_function_grapic(variety_range)

us.equiinterval_method_grapic(variety_range)

us.equipropable_method_grapic(variety_range)

print(us.expectation(variety_range), "- m")

print(us.dispersion(variety_range), "- D")

us.confidence_interval_MAT(variety_range)

us.confidence_interval_DIS(variety_range)

us.distribution_function_grapic_and_other_function(variety_range)

us.hypotize_of_normal_law(variety_range)

print("-----bivariate_input------")
x = []
y = []
bs.load(x, y, "bivariate_input.txt")
print("Mx-", us.expectation(x))
print("My-", us.expectation(y))
print("Dx-", us.dispersion(x))
print("Dy-", us.dispersion(y))
print(bs.correlation_moment(x,y),"- correlation moment")
print(bs.correlation_coefficent(x,y),"-correlation coefficient")
print(bs.interval_correlation_mark(x,y)," -correlation coefficient with gamma = 0,95")
bs.hypotize_of_lack_correlation(x,y)
bs.dispersion_diargram_and_regression_line(x,y)

