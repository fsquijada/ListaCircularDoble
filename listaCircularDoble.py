class nodoListaCircular:
    def __init__(self, numero):
        self.numero = numero
        self.anterior = None
        self.siguiente = None

class ListaNumeros:    
    # Constructor
    def __init__(self):
        self.primero = None
        self.ultimo = None

    # Método para insertar en la lista
    def insertar(self, numero):
        nuevo = nodoListaCircular(numero)

        if (self.primero == None):
            self.primero = self.ultimo = nuevo
            self.primero.anterior = self.primero.siguiente = self.ultimo.numero
        else:
            nuevo.anterior = self.ultimo.numero
            nuevo.siguiente = self.primero.numero
            self.primero.anterior = self.ultimo.siguiente = nuevo
            self.ultimo = nuevo
            
    # Método para imprimir listado
    def imprimir(self):
        print("\nLista completa: ")
        aux = self.primero
        # Imprime cada carrito desde el que está para salir hasta el del fondo
        if(aux != None):
            if (aux.siguiente == aux.anterior):
                print (aux.numero)
            else:
                while(aux.siguiente != self.primero.numero):
                    print (aux.numero)
                    aux = aux.siguiente
                print (aux.numero)

    # Método para buscar números que están en la lista
    def buscarNumero(self, numero):
        aux = self.primero
        # Imprime el número buscado, el anterior y el siguiente
        if(self.primero == self.ultimo):
            if (aux.numero == numero):
                print (f"anterior: {aux.anterior}, actual: {aux.numero}, siguiente: {aux.siguiente}.")
        else:
            while (aux.anterior != self.ultimo.numero):
                if (aux.numero == numero):
                    print (f"anterior: {aux.anterior}, actual: {aux.numero}, siguiente: {aux.siguiente}.")
                    break
                aux = aux.siguiente