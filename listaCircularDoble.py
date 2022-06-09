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
            self.primero.anterior = self.primero.siguiente = self.ultimo
        else:
            nuevo.anterior = self.ultimo
            nuevo.siguiente = self.primero
            self.ultimo.siguiente = nuevo
            self.primero.anterior = nuevo
            self.ultimo = nuevo
            
    # Método para imprimir listado
    def imprimir(self):
        print("\nLista completa: ")
        aux = self.primero
        # Imprime cada dato de la lista
        if(aux != None):
            if (aux.siguiente == aux.anterior):
                print (aux.numero)
            else:
                while(aux.siguiente != self.primero):
                    print (aux.numero)
                    aux = aux.siguiente
                print (aux.numero)

    # Método para buscar números que están en la lista
    def buscarNumero(self, numero):
        aux = self.primero
        # Imprime el número buscado, el anterior y el siguiente
        if(self.primero == self.ultimo):
            if (aux.numero == numero):
                print (f"anterior: {aux.anterior.numero}, actual: {aux.numero}, siguiente: {aux.siguiente.numero}.")
        else:
            while (aux.anterior != self.ultimo.numero):
                if (aux.numero == numero):
                    print (f"anterior: {aux.anterior.numero}, actual: {aux.numero}, siguiente: {aux.siguiente.numero}.")
                    break
                aux = aux.siguiente
