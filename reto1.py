# Filtrar numero primo con tipado estático

def es_primo(number: int) -> bool:

    results_list = [i for i in range(2, number+1) if number % i == 0]
    result_final = len(results_list) == 1
    if result_final:
        print(True)
    else:
        print(False)

def run():
    es_primo(55)


if __name__ == '__main__':
    run()