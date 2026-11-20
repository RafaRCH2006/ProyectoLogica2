class Conjunto:
    def __init__(self, elementos=None):
        self.elementos = []
        
        if elementos is not None:
            for elemento in elementos:
                self.agregar(elemento)
                
    def pertenece(self, elemento):
        for actual in self.elementos:
            if actual == elemento:
                return True
        return False
    
    def agregar(self, elemento):
        if not self.pertenece(elemento):
            self.elementos.append(elemento)