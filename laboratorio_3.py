#==============================
# Condicionales
#==============================
precio = 50
#----------
# Si esto
#----------
if precio < 50:
    print("El precio es menor que 50")
#--------------------------
# Si no... si esto otro...
#--------------------------
elif precio > 50:
    print("El precio es mayor a 50")
#---------------------------
# Si nada de lo anterior...
#---------------------------
else:
    print("El precio es 50")

precio = 50
cantidad = 5
total = precio*cantidad
#===========================
# Condicionales anidados
#===========================
if total > 100:
    if total > 500:
        print("Total es mayor que 500")
    else:
        if total < 500 and total > 400:
            print("Total es menor que 500 pero mayor que 400")
        elif total < 500 and total > 300:
            print("Total entre 300 y 500")
        else:
            print("Total entre 100 y 300")
#--------------------------------
# Condicional de igualdad son ==
#--------------------------------
elif total == 100:
    print("Total es 100")
else:
    print("Total menor que 100")

#==============================================
# Contador mientras la condición sea verdadera
#==============================================
num = 0
while num < 5:
    num = num + 1
    print('num = ', num)

num = 0
while num < 5:
    num += 1            # num += 1 es lo mismo que num = num + 1
    print('num = ', num)
    if num == 3:        # condición antes de salir del bucle
        break

num = 0
while num < 5:
    num += 1
    if num > 3:
        continue        # evitar lo que sigue, continuar con las iteraciones

    print('num = ', num)

#========================
# Bucle sobre lista
#========================
nums = [10, 20, 30, 40, 50]
for i in nums:
    print(i)

#========================
# Bucle sobre un string
#========================
for char in 'Hello':
    print(char)

#============================
# Bucle sobre un diccionario
# items = elementos
#============================
numNames = { 1:'One', 2:'Two', 3:'Three'}
for pair in numNames.items():
    print(pair)

#============================
# Bucle sobrediccionario
# key = llave
# value = valor
#============================
for k,v in numNames.items():
    print("key = ", k, "value = ", v)
#========================================================================================
#====================
# Primera función
#====================
def saludo():
    #====================================
    # Documentación rápida de la función
    #====================================
    """Ësta función saluda"""
    print('¡Quiúboles!, ¿Cómo estás?')

#=======================
# Llamado de la función
#=======================
saludo()

#===============================
# Se ejecuta pero no se asigna
#===============================
salida = saludo()

#===================
# Esto no funciona
#===================
print(salida)
#=========================
# Mostrar documentación
#=========================
#help(saludo)

#==========================
# Función con argumento
#==========================
def salu2(nombre):
    """Esta función te saluda por tu nombre"""
    print("¡Qué onda ese!",nombre,"!")
salu2("Julián")
salu2("Angel")

#==========================================
# Ahorrar trabajo del intérprete
# nombre:str la variante nombre es un str
#==========================================
def saludos(nombre:str):
    """ Esta función te saluda por tu nombre estrictamente """
    print("¡Qué onda ese!",nombre,"!")
saludos("Julián")
a = 123
print(type(a))

#====================================
# Función con muchos argumentos
#====================================
def saludos_multiples(nombre1,nombre2,nombre3):
    """Esta función saluda a 3 personas al mismo tiempo"""
    print("Hola ",nombre1,",",nombre2,"y",nombre3)
saludos_multiples("Hugo","Paco","Luis")

#=============================================
# Función con cualquier número de argumentos
#=============================================
def muchos_saludos(*nombres):
    """Esta función saluda a todos los que quieras"""
    i = 0
    #===================================
    # end= es para ponerlo de corrido
    #===================================
    print("Hola ", end="")
    while len(nombres) > i:
        # Ultimo nombre
        if (i==len(nombres)-1):
            print(nombres[i])
        else:
            # Cualquier otro nombre
            print(nombres[i], end=", ")
        i+=1

muchos_saludos("Bosco","Angel","David","Tamara","Mili","Edwin","Lev","Luis","Abigail")
def greet(firstname, lastname):
    print('Hello', firstname, lastname)

#=================================================
# Llamar a la función con argumentos en desorden
#=================================================
greet(lastname='Jobs', firstname='Steve') # Se pueden especificar las variables en desorden

#=======================================
# Función con argumentos escondidos **
#=======================================
def greet(**person):
    #=====================================================
    # persona tiene características firstname y lastname
    #=====================================================
    print('Hello ', person['firstname'], person['lastname'])

greet(firstname='Steve', lastname='Jobs')
greet(lastname='Jobs', firstname='Steve')
greet(firstname='Bill', lastname='Gates', age=55) # Se pueden pasar más parámetros de los necesarios

#==================================
# Función con valores por defecto
#==================================
def greet(name = 'Guest'):
    print('Hello', name)

greet() # Utiliza el valor dado de antemano
greet('Steve')

#=========================
# Función con resultado
#=========================
def suma(a,b):
    return a + b

#====================================
# Programación funcional
# Se pueden funciones en funciones
#====================================
total=suma(5 , suma(10, 20))
print(total)

#==================================================
# Cálculo lambda
# nombre de la función = lambda variable : función
#==================================================
x_al_cuadrado = lambda x : x * x
al = x_al_cuadrado(5)
print(al)

#=============================
# Lambda de varias variables
#=============================
suma = lambda x1, x2, x3: x1+x2+x3
print(suma(99,98,97))

sumas = lambda *x: x[0]+x[1]+x[2]+x[3]

print(sumas(100,200,300,400))

#=========================================
# Uso de una función anónima
# El argumento va afuera entre paréntesis
#=========================================
print((lambda x: x*x)(6)) # Función

#==================================
# Función con variable global
# EVITE EL EXESO !!!!!!
#==================================
name = 'Steve'
def greet():
    global name #Para utilizar una variable global (que viene de fuera del bloque)
    name = 'Bill'
    print('Hello ', name)

greet()

#===============================
# Algoritmo 1
#===============================
# Serie exponencial
# Factorización de x
# Negativos con función inversa
#===============================
n= 200
x = -100.0
flag = False
if x<0:
    flag= True
    x =-x
s= 1.0
for i in range(n,0,-1):
    s *= x/float(i)
    s +=1.0
if flag ==True:
    s= 1/s
print(s)

