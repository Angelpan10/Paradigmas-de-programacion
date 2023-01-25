import random

N:int = 10

def generador(N:float) -> None:
    semilla:float = random.uniform(-1,1)
    random.seed(semilla)
    for i in range(N):
        x:float = random.uniform(-1,1)
        y:float = random.uniform(-1,1)
        print("x = ",x,"\t y = ",y)

generador(N)


