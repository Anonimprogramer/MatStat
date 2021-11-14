from numpy import sqrt
import matplotlib.pyplot as plt


def load(filename):
    univariate_sample = []
    with open(filename, "r") as file:
        for line in file:
            univariate_sample.extend(list(map(float, line.split())))
    return univariate_sample


def variation_range_of_univariate_sample(univariate_sample):
    variation_range_of_univariate_sample = univariate_sample
    variation_range_of_univariate_sample.sort()
    return variation_range_of_univariate_sample


def distribution_function_grapic(variation_range):
    unique_elements = variation_range
    unique_elements = set(unique_elements)
    current = 0
    common_count = len(variation_range)

    y = []
    x = []
    for k in unique_elements:
        x.append(k)
        x.append(k)
        y.append(current / common_count)
        current += variation_range.count(k)
        y.append(current / common_count)

    x.extend([0, 5])
    y.extend([0, 1])
    x.sort()
    y.sort()

    plt.plot(x, y, lw=1)
    plt.grid()
    ax = plt.gca()
    plt.xlim([0, 5])
    plt.ylim([0, 1.2])
    plt.show()


def equiinterval_method_grapic(variation_range):
    n = int(sqrt(len(variation_range)))
    delta = (variation_range[len(variation_range) - 1] - variation_range[0]) / n
    delta_lists = []
    for i in range(1, 11):
        delta_lists.append([])
        for value in variation_range:
            if delta * (i - 1) <= value <= delta * i:
                delta_lists[i - 1].append(value)

    x = [0]
    y = [0]
    i = 0
    for list in delta_lists:
        x.append(delta * i)
        x.append(delta * (i + 1))
        y.append(len(list) / n / delta)
        y.append(len(list) / n / delta)
        i += 1
    y.append(0)
    x.append(delta * n)

    plt.plot(x, y)
    plt.show()


def equipropable_method_grapic(variation_range):
    n = int(sqrt(len(variation_range)))
    list_a = [variation_range[0]]
    list_b = []
    for i in range(1, 10):
        list_a.append((variation_range[i * n] + variation_range[i * n + 1]) / 2)
        list_b.append((variation_range[i * n] + variation_range[i * n + 1]) / 2)
    list_b.append(variation_range[len(variation_range)-1])

    x = [0]
    y = [0]

    for i in range(n):
        x.append(list_a[i])
        x.append((list_b[i]))
        y.append(1/(n*(list_b[i]-list_a[i])))
        y.append(1 / (n * (list_b[i] - list_a[i])))

    x.append(variation_range[len(variation_range)-1])
    y.append(0)

    plt.plot(x, y)
    plt.show()


