class Node:
    def __init__ (self, data = None):
        self.data = data
        self.next = None
        
    def __str__ (self):
        return f"{self.data}"

class gerenciarQueue:
    def __init__ (self) :
        self.adminsFirst = None 
        self.alunosFirst = None
        self.sumFirst = None
        
        self.alunosLast = None
        self.adminsLast = None
        self.sumLast = None
        
    def adicionarAdm (self, elem):
        node = Node(elem)
        if self.adminsLast is None:
                self.adminsLast = node
        else:
            self.adminsLast.next = node
            self.adminsLast = node
                    
        if self.adminsFirst is None:
            self.adminsFirst = node
        print(f"O elemento {elem} foi adicionado à fila de administradores.")
                
    def adicionarAluno (self, elem):
        node = Node(elem)
        if self.alunosLast is None:
            self.alunosLast = node
        else :
            self.alunosLast.next = node
            self.alunosLast = node
                
        if self.alunosFirst is None:
            self.alunosFirst = node
        print(f"O elemento {elem} foi adicionado à fila de alunos.")
        
    # Consumo da fila, mas transferindo o first e o last para a responsabilidade da fila combinada
    def processarFila(self, queue = "admins"):
        queueFirst = None
        queueLast = None
        
        if queue == "admins":
            queueFirst = self.adminsFirst
            queueLast = self.adminsLast
            self.adminsLast = None
            self.adminsFirst = None
        else:
            queueFirst = self.alunosFirst
            queueLast = self.alunosLast
            self.alunosLast = None
            self.alunosFirst = None
            
        if self.sumLast is None:
            self.sumLast = queueLast
        else :
            self.sumLast.next = queueLast
            self.sumLast = queueLast
                    
        if self.sumFirst is None:
            self.sumFirst = queueFirst
            
        print(f"Fila {queue} consumida com sucesso.")
    
    #Consumo da fila por completo, apagando todos os nós, mas sem passar para a fila combinada.
    def consumirFila(self, queue = "admins"):
        if queue == "admins":
            pointer = self.adminsFirst
            while (pointer):
                self
                self.adminsFirst = self.adminsFirst.next
                pointer = pointer.next
            queue = "de administradores"
        elif queue == "alunos":
            pointer = self.alunosFirst
            while (pointer):
                self.alunosFirst = self.alunosFirst.next
                pointer = pointer.next
            queue = "de alunos"
        elif queue == "sum":
            pointer = self.sumFirst
            while (pointer):
                self.sumFirst = self.sumFirst.next
                pointer = pointer.next
            queue = "combinada"
        print (f"A fila {queue} foi consumir com sucesso.")
     
    def reorganizarFila(self):
        if self.sumFirst is None and self.sumLast is None: 
            self.sumFirst = self.adminsFirst
            if self.sumLast is not None:
                self.sumLast.next = self.alunosFirst
            self.sumLast = self.alunosFirst
        else:
            print("Fila já preenchida, consuma ela para reorganizá-la.")
    
    def __listarFila (self, queue):
        pointer = None
        secPointer = None
        if queue == "admins":
            pointer = self.adminsFirst
        elif queue == "alunos":
            pointer = self.alunosFirst
        elif queue == "sum":
            pointer = self.sumFirst
            if pointer != self.sumLast:
                secPointer = self.sumLast
        r = ""
        if pointer is None:
            return "Lista vazia"
        while (pointer):
            r += f"{pointer.data}\n "
            pointer = pointer.next
        if secPointer is not None:
            r += "\n"
        while (secPointer):
            r += f"{secPointer.data}\n"
            secPointer = secPointer.next
        return r
        
    def listarFilas (self):
        r = "--------------------------------\nLista combinada: \n"
        r += self.__listarFila("sum")
        r += "\n--------------------------------\nLista de administradores: \n"
        r += self.__listarFila("admins")  
        r += "\n--------------------------------\nLista de alunos: \n"
        r += self.__listarFila("alunos")
        print(r)
        
fila = gerenciarQueue()
fila.adicionarAluno({"nome_arquivo": "Dados de João DaCosta", "total_paginas": 3})
fila.adicionarAdm({"nome_arquivo": "Dados de Deide Piantov", "total_paginas": 5})
fila.listarFilas()