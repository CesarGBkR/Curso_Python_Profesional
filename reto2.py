def make_division_by(n:int):
    assert type(n) == int, "Solo puedes usar números enteros"
    def make_division_value(x:int):
        assert type(n) == int, "Solo puedes usar números enteros"
        return x / n
    return make_division_value

division_by_3 = make_division_by(3)
print(division_by_3(18))

division_by_5 = make_division_by(5)
print(division_by_5(100))

division_by_18 = make_division_by('a')
print(division_by_18(54))