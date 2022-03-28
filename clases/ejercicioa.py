class newyork:
    def __del__(self):
        print("Se destruye New York")
    def __init__(self):
        self.edificio = [edificio(name) for name in ["a", "b"]]
        self.empleado = [empleado(name) for name in ["salim", "sñr Martin", "sra. Xing"]]

class edificio: 
    def __del_(self):
        print("destruccion{}".format(self.name))