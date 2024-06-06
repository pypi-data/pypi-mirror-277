from package1 import add_sub_mult_div


def test_add():
    assert add_sub_mult_div.add(1, 3) == 4
def test_sub():
    assert add_sub_mult_div.subtraction(5, 2) == 3
def test_multiply():
    assert add_sub_mult_div.multiple(5, 5) == 25
def test_div():
    assert add_sub_mult_div.div(10, 5) == 2
def test_log2():
    assert add_sub_mult_div.logariphm_two(4) == 2
def test_logNatural():
    assert round(add_sub_mult_div.logariphm_natural(4), 2) == 1.39
def test_sqrt():
    assert add_sub_mult_div.sqrt(4) == 2
def test_sqrt3():
    assert add_sub_mult_div.sqrt3(8) == 2
def test_sqrtN():
    assert add_sub_mult_div.sqrtN(32, 5) == 2