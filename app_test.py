def some_func(x):
    return x + x

def test_answer():
    assert some_func(1) == 2
    assert some_func(2) == 4
    assert some_func(3) == 6
