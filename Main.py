import univariate_sample as us

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
