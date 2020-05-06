def sumar(a, b):
    c = a + b
    return c

def restar(a, b):
    return a-b

def multiplicar(a, b):
    return a*b

def div_entera(a, b):
    if b == 0:
        print("Error division sobre cero")
        return
    return a//b

def division(a, b):
    if b == 0:
        print("Error division sobre cero")
        return
    return a/b

def modulo(a, b):
    if b == 0:
        print("Error division sobre cero")
        return
    return a%b

def potencia(a, b):
    return a**b

def main():
    print("Ingresa dos valores")
    x = int(input())
    y = int(input())

    print("1.Sumar\n2.Restar\n3.División entera")
    print("4.División\n5.Modulos\n6.Potencia\n7.Multiplicar")
    op = int(input())

    if op == 1:
        print(sumar(x, y))
    elif op == 2:
        print(restar(x, y))
    elif op == 3:
        print(div_entera(x, y))
    elif op == 4:
        print(division(x, y))
    elif op == 5:
        print(modulo(x, y))
    elif op == 6:
        print(potencia(x, y))
    elif op == 7:
        print(multiplicar(x, y))
    else:
        print("Opcion no válida")

if __name__=="__main__":
    main()