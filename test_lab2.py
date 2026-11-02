import lab2

def test_find_min_max():
    inputlist = [33, 22, 27, 25, 29, 31, 21]
    expected = [21, 33]
    result = lab2.find_min_max(inputlist)

    assert(result == expected)

def test_calc_average():
    inputlist = [33, 23, 27, 25, 29, 31, 21]
    expected = 27
    result = lab2.calc_average(inputlist)

    assert(round(result,3) == round(expected,3))


def test_find_median_odd_number():
    inputlist = [33, 23, 26, 25, 29, 31, 21]
    expected = 26
    result = lab2.calc_median_temperature(inputlist)
    assert(result == expected)



def test_find_median_even_number():
    inputlist = [33, 23, 26, 25, 29, 31, 21,37]
    expected = 27.5
    result = lab2.calc_median_temperature(inputlist)
    assert(result == expected)