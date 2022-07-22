def make_repeater_of(n: int):
    assert type(n) == int, "Solo puedes usar números enteros"
    def repeater(string: str):
        assert type(string) == str, "Solo puedes usar cadenas de carácteres"
        print(string * n)
    return repeater


repeat3 = make_repeater_of(3)
repeat5 = make_repeater_of(5)
repeat7 = make_repeater_of(7)

mi_Nombre_3_Veces = repeat3("Cesar")
mi_Nombre_5_Veces = repeat5("Cesar")
mi_Nombre_7_Veces = repeat7("Cesar")