from datetime import datetime

def execution_time(func):
    def wrapper(*args, **kwargs):
        initial_time = datetime.now()
        func(*args, **kwargs)
        final_time = datetime.now()
        time_elapsed = final_time - initial_time
        print("Pasaron " + str(time_elapsed.total_seconds()) + " segundos")
    return wrapper

@execution_time
def random_funct():
    for i in range (1, 10000000):
        pass
@execution_time
def suma(a: int ,b: int):
    print(a + b)

@execution_time
def saludo(name: str):
    print("Hola " + name)

random_funct()
suma(222, 146)
saludo("Cesar")
