import univariate_sample as us
import relations as re

univariate_sample = us.load("univariate_input.txt")

variety_range = us.variation_range_of_univariate_sample(univariate_sample)
print(variety_range)

us.distribution_function_grapic(variety_range)

us.equiprobable_method_grapic(variety_range)



set = ("n", "i", "s", "t", "y", "r", "a", "k")
re.find_relations(set, set)
