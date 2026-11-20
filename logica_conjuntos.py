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
    
    def eliminar(self, elemento):
        if self.pertenece(elemento):
            self.elementos.remove(elemento)
            
    def cardinalidad(self):
        return len(self.elementos)
    
    def es_vacio(self):
        return len(self.elementos) == 0
    
    def __eq__(self, otro):
        if not isinstance(otro, Conjunto):
            return False
    
        if self.cardinalidad() != otro.cardinalidad():
            return False
    
        for elemento in self.elementos:
            if not otro.pertenece(elemento):
                return False
        return True
    
    def __str__(self):
        if self.es_vacio():
            return "∅"
        
        return "{" + ", ".join(str(elemento) for elemento in self.elementos) + "}"
    
    