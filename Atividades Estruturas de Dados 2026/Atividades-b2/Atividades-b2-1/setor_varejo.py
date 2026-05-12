import time

class Node:
    def __init__ (self, data = None):
        self.data = data
        self.next = None
        
    def __str__ (self):
        return f"{self.data}"

class Fila1:
    def __init__ (self):
        self.first = None
        self.last = None
        
    '''
        def __repr__ (self) :
            r = ""
            pointer = self.first
            while (pointer):
                r += f"{pointer.data} "
                pointer = pointer.next
            return r
    '''
    
    def __str__ (self) :
        r = ""
        pointer = self.first
        while (pointer):
            r += f"{pointer.data["nome_item"]} {pointer.data["quantidade_pecas"]}\n"
            pointer = pointer.next
        return r
    
    def __getitem__ (self, index):
        pointer = self.first
        i = 0
        while (pointer):
            i += 1
            if i > index:
                return f"{pointer.data}"
            pointer = pointer.next
            

    def push (self, elem):
        try :
            if elem["id_pedido"] is not None and elem["nome_item"] is not None and elem["quantidade_pecas"] is not None:
                node = Node(elem)
                if self.last is None:
                    self.last = node
                else :
                    self.last.next = node
                    self.last = node
                    
                if self.first is None:
                    self.first = node
                return elem
            else:
                print("Valor inserido em formato incorreto.\n O valor correto é : {id: valor_do_id, nome: nome, quantidade_de_pecas: qtde_de_pecas")
                return elem
        except ValueError:
            print(ValueError)
            return elem
            
    def pop (self):
        if self.first is not None:
            elem = self.first.data
            self.first = self.first.next
            return elem
    
    def peek (self):
        if self.first is not None:
            return self.first.data
    
    '''
    def showQueue (self):
        pointer = self.first
        while (pointer):
            time.sleep(0.5)
            print(f"{pointer.data["nome_item"]} {pointer.data["quantidade_pecas"]}\n")
            pointer = pointer.next
    '''
