class Conjunto():
    def __init__(self, nome):
        self.lista = []
        self.nome = nome

       
    def inserir(self, dados):
        if not dados in self.lista:            
            self.lista.append(dados)            
        else:
            self.lista.append(dados)       
            
        
    def show(self):
        if len (self.lista)== 0:
            print (' Conjunto Vazio: ' + ' ={ }')
        else:
            aux = ','.join(self.lista)              
            print(self.nome+'={'+ aux + '}')





