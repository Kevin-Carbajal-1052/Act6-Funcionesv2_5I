print("Mas sobre funciones")
# Aqui se escriben las funciones
def suma(a,b):
    s=a+b
    return s

def resta(a,b):
    r=a-b
    return r

def multi(a,b):
    m=a*b
    return m

def division(a,b):
    d=a/b
    return d

# Llamadas a funciones
print("--Calculando suma--")
n1=int(input("Ingresa el primer numero: "))
n2=int(input("Ingresa el segundo numero: "))
suma1=suma(n1,n2)
print(f"La suma de {n1} + {n2} es:",suma1,"\n")

print("--Calculando resta--")
r1=int(input("Ingresa el primer valor: "))
r2=int(input("Ingresa el segundo valor: "))
resta1=resta(r1,r2)
print(f"La resta de {r1} - {r2} es:",resta1,"\n")

print("--Calculando multiplicacion--")
m1=int(input("Ingresa el primer numero: "))
m2=int(input("Ingresa el segundo numero: "))
mul=multi(m1,m2)
print(f"La multiplicacion de {m1} * {m2} es:",mul,"\n")

print("--Calculando division--")
d1=float(input("Ingresa el primer valor: "))
d2=float(input("Ingresa el segundo valor: "))
div=division(d1,d2)
print(f"La division de {d1} y {d2} es:",div)