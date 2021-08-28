from ClasePila import Pila
if __name__=='__main__':
    unaPila= Pila(6)
    unaPila.insertar(5)
    unaPila.insertar(2)
    unaPila.insertar(8)
    unaPila.insertar(15)
    unaPila.insertar(3)
    unaPila.mostrar()
    print("Suprimir el ultimo elemento {}".format(unaPila.suprimir()))
    print("Pila luego de suprimir el ultimo elemento")
    unaPila.mostrar()
